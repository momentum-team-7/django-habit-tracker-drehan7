const deleteLogButtons = document.querySelectorAll('.delete-log-button')
for (let delButton of deleteLogButtons) {
    delButton.addEventListener('click', e => {
        const logContainer = e.target.parentElement.parentElement;
        const delUrl = `/home/habit_info/${logContainer.id}/delete_log/${e.target.id}/`
        fetch(delUrl, {
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
            .then(response => response.json())
            .then(data => {
                if (data['del'] === 'true') {
                    logContainer.remove()
                }
            })

    })
}


// Chart Stuff

const getChartDataY = () => {
    let values = []
    let amounts = document.querySelectorAll('.track-unit-cell')
    amounts.forEach(e => values.push(parseInt(e.innerHTML)))
    return values.reverse()
}
const getChartDataX = () => {
    let values = []
    let amounts = document.querySelectorAll('.date-cell')
    amounts.forEach(e => values.push(e.innerHTML))
    return values.reverse()

}


let ctx = document.querySelector('#myChart').getContext('2d');

let myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: getChartDataX(),
        datasets: [{
            label: 'Habit Progress',
            // backgroundColor: '#fefae0',
            borderColor: 'green',
            data: getChartDataY()

        }]
    },

    options: {}
});