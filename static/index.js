function query(){

    var inputValue = document.getElementById('manager_name').value;
    if (inputValue == '' || inputValue == null) {
        alert('Please enter a manager name.');
        return;
    }
    var url = '/manager?manager_name=' + encodeURIComponent(inputValue);
    
    fetch (url)
    .then(response => response.text())
    .then(html => {
        document.body.innerHTML = html; // 或将 HTML 插入页面的特定部分
    })
    .catch(error => console.error('Error:', error));
}

function gotoManager(managerName) {

  var url = '/manager?manager_name=' + encodeURIComponent(managerName);
    
  fetch (url)
  .then(response => response.text())
  .then(html => {
      document.body.innerHTML = html; // 或将 HTML 插入页面的特定部分
  })
  .catch(error => console.error('Error:', error));
}

function scrollToLetter(letter) {
    // 隐藏所有的manager列表
    var managerDivs = document.querySelectorAll('[id$="-manager"]');
    for (var i = 0; i < managerDivs.length; i++) {
      managerDivs[i].style.display = 'none';
    }
  
    // 显示对应字母的manager列表
    var targetDiv = document.getElementById(letter + '-manager');
    if (targetDiv) {
      targetDiv.style.display = 'block';
    }
  }
