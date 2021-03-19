// let addLogButtons = document.querySelectorAll('add-log-button');
// for (let addButton of addLogButtons) {
//     addButton.addEventListener('click', e => {
//         const addLogUrl = `/home/habit/${e.target.id}/add_log/`
//         fetch(addLogUrl, {
//             headers: {
//                 'Accept': 'application/json',
//                 'X-Requested-With': 'XMLHttpRequest',
//             },
//         })
//             .then(response => response.json())
//             .then(data => {
//                 console.log(data)
//             })
//     })
// }