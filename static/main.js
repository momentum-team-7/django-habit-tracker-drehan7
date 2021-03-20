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
