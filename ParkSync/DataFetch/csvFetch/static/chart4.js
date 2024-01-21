const chart4 = document.getElementById('chart4').getContext('2d');
const myChart4 = new Chart(chart4, {
    type: 'bar',
    data: {
        labels: ['monitor', 'laptop', 'desk', 'desktop', 'tablet', 'phone', 'lights'],
        datasets: [{
            label: 'Items',
            backgroundColor: '#b4eaf6',
            borderColor: '#b4eaf6',
            data: [500, 900, 400, 700, 800, 900, 200],
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                }
            }]
        }
    },
})