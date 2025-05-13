import cv2
import numpy as np
import csv

from util import get_parking_spots_bboxes, empty_or_not

def calc_diff(im1, im2):
    return np.abs(np.mean(im1) - np.mean(im2))


mask = './mask_1920_1080.png'
video_path = './parking_1920_1080.mp4'

mask = cv2.imread(mask, 0)

cap = cv2.VideoCapture(video_path)

connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)

spots = get_parking_spots_bboxes(connected_components)

spots_status = [None for _ in spots]
diffs = [None for _ in spots]

previous_frame = None

# CSV file path for parking status and location
csv_file_path = 'output.csv'

# Open the CSV file for parking status and location writing
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer for parking status and location
    csv_writer = csv.writer(csvfile)

   
    csv_writer.writerow(['Frame Number', 'Spot Index', 'Spot Status', 'Spot Location'])

    # Continue processing frames
    frame_nmr = 0
    ret = True
    step = 30
    while ret:
        ret, frame = cap.read()

        if frame_nmr % step == 0 and previous_frame is not None:
            for spot_indx, spot in enumerate(spots):
                x1, y1, w, h = spot

                spot_crop = frame[y1:y1 + h, x1:x1 + w, :]

                diffs[spot_indx] = calc_diff(spot_crop, previous_frame[y1:y1 + h, x1:x1 + w, :])

            # print([diffs[j] for j in np.argsort(diffs)][::-1])

        if frame_nmr % step == 0:
            if previous_frame is None:
                arr_ = range(len(spots))
            else:
                arr_ = [j for j in np.argsort(diffs) if diffs[j] / np.amax(diffs) > 0.4]
            for spot_indx in arr_:
                spot = spots[spot_indx]
                x1, y1, w, h = spot

                spot_crop = frame[y1:y1 + h, x1:x1 + w, :]

                spot_status = empty_or_not(spot_crop)

                spots_status[spot_indx] = spot_status

                # Calculate spot location
                spot_location = f"({x1 + w/2}, {y1 + h/2})"

                # Write the frame number, spot index, spot status, and spot location to the CSV file
                csv_writer.writerow([frame_nmr, spot_indx, spot_status, spot_location])

        if frame_nmr % step == 0:
            previous_frame = frame.copy()

        for spot_indx, spot in enumerate(spots):
            spot_status = spots_status[spot_indx]
            x1, y1, w, h = spots[spot_indx]

            if spot_status:
                frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
            else:
                frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 0, 255), 2)

        cv2.rectangle(frame, (80, 20), (550, 80), (0, 0, 0), -1)
        cv2.putText(frame, 'Available spots: {} / {}'.format(str(sum(spots_status)), str(len(spots_status))),
                    (100, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        frame_nmr += 1

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()

print(f"Parking status and location have been saved to {csv_file_path}")
