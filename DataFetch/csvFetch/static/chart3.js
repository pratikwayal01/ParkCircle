const chart3 = document.getElementById('chart3').getContext('2d');
const myChart3 = new Chart(chart3, {
    type: 'pie',
    data: {
        labels: ['webcam', 'keyboard', 'pad', 'desktop', 'tablet', 'phone', 'desk'],
        datasets: [{
            label: 'items',
            backgroundColor: 'rgba(161, 198, 247, 1)',
            borderColor: 'rgb(47, 128, 237)',
            data: [30, 40, 20, 50, 60, 70, 40],
        }]
    },
})