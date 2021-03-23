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

const deleteHabitButtons = document.querySelectorAll('.delete-habit-button');
for (let delHabitBtn of deleteHabitButtons) {
    delHabitBtn.addEventListener('click', e => {
        const habitContainer = e.target.parentElement.parentElement;
        const delHabitUrl = `/home/${e.target.id}/delete/`
        fetch(delHabitUrl, {
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
            .then(res => res.json())
            .then(data => {
                console.log(data)
                if (data['habit'] == 'deleted') {
                    habitContainer.remove()
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
            // backgroundColor: 'white',
            borderColor: 'green',
            data: getChartDataY()

        }]
    },

    options: {}
});

const progressComment = document.querySelector('.progress-comment')
let goal = document.querySelector('.habit-goal').textContent
const lastThree = getChartDataY().slice(-3).reverse()
console.log(lastThree)
console.log(goal)
if (lastThree.includes(parseInt(goal))) {
    progressComment.textContent = "You're doing Great!"
}
else {
    progressComment.textContent = "Keep pushing!"
}