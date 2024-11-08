// Serum Creatinine Graph
const creatinineCtx = document.getElementById('creatinineGraph').getContext('2d');
const creatinineGraph = new Chart(creatinineCtx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Serum Creatinine (mg/dL)',
            data: [1.2, 1.3, 1.5, 1.6, 1.7, 1.4, 1.3, 1.5, 1.8, 1.6, 1.9, 1.7],
            borderColor: '#ff6384',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            fill: true,
            tension: 0.4,
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Creatinine Level (mg/dL)'
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Months'
                }
            }
        }
    }
});

// Blood Urea Levels Graph
const ureaCtx = document.getElementById('ureaGraph').getContext('2d');
const ureaGraph = new Chart(ureaCtx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Blood Urea (mg/dL)',
            data: [25, 28, 30, 32, 29, 27, 33, 31, 35, 34, 36, 32],
            borderColor: '#36a2eb',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            fill: true,
            tension: 0.4,
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Urea Level (mg/dL)'
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Months'
                }
            }
        }
    }
});

// GFR Result Graph
const gfrCtx = document.getElementById('gfrGraph').getContext('2d');
const gfrGraph = new Chart(gfrCtx, {
    type: 'doughnut',
    data: {
        labels: ['Normal', 'Mildly Decreased', 'Moderate Decrease', 'Severe Decrease', 'Kidney Failure'],
        datasets: [{
            data: [25, 20, 15, 10, 30],
            backgroundColor: ['#4caf50', '#ffeb3b', '#ff9800', '#f44336', '#d32f2f']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'bottom'
            }
        }
    }
});