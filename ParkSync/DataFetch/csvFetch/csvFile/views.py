from django.shortcuts import render
from .models import Parking
import subprocess
import time
# Create your views here.


def table_view(request):
    ctr = Parking.objects.filter(Spot_Status=True).count()
    ctr2 = Parking.objects.filter(Spot_Status=False).count()
    obj = Parking.objects.all().count()
    return render(request, 'index.html', {
        'obj_lst': obj,
        'counter': ctr,
        'counter2': ctr2,
    })
