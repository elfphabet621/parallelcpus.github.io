var selected_lan, selected_num;

function formData(){
    var selected_lan = document.querySelector('input[name="selected-lan"]:checked')?.value;
    var selected_num = document.querySelector('input[name="selected-num"]:checked')?.value;

    if(selected_lan == 'en')
        selected_lan = 'engWordList.json'
    else
        selected_lan = 'vietWordList.json'

    if(selected_num == 'top')
        selected_num = 50;
    else
        selected_num = 500;

    const wordList = document.querySelector('.table-cont');
    loadJSON(selected_lan,selected_num, wordList);
}

// function eventListeners(){
//     window.addEventListener('ContentLoaded', () => {
//         loadJSON();
//     });
// }
function loadJSON(selected_lan, selected_num, wordList){
    fetch(selected_lan)
    .then(response => response.json())
    .then(data => {
        let html = '';
        for (line = 0; line <selected_num; line++)
        {
            html += `
                <tr>
                    <td class ="col-w">${data[line].word}</td>
                    <td class="col-c">${data[line].count}</td>
                </tr>
            `;
        }
        wordList.innerHTML = html;
    })
    .catch(error =>{
        alert(`User live server or local server`);
    })
}
