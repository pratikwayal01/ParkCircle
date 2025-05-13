const chart2 = document.getElementById('chart2').getContext('2d');
const myChart2 = new Chart(chart2, {
    type: 'doughnut',
    data: {
        labels: ['tv', 'desktop', 'tablet', 'camera', 'laptop', 'mobile', 'monitor'],
        datasets: [{
            label: 'products',
            data: [60, 40, 20, 50, 80, 90, 30],
            backgroundColor: ['#b4eaf6', '#efcfff', '#ffe69c', '#79dfc1', '#ffd4cf', '#e284ff', '#a1c6f7', '001f3f', '#39cccc', '#01ff70', '#85144b', '#f012be', '#3d9970', '#111111', '#aaaaaa']
        }]
    },
})