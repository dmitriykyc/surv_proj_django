"use strict"

window.onload = function () {
    console.log('DOM ready')
    let categoryName = document.querySelectorAll('div[id=name_survey]') //Собираем все эллементы с таким id
    categoryName.forEach(function (item){ //Проходм по каждому
        item.onclick = function (event) { //При клике:

            console.log(event.target.dataset['ffff'])
            // $.ajax()
        }
    })
}