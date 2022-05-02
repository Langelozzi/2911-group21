const button = document.querySelector('.form-check-input');
button.addEventListener('click', modeswitch);
var modeflag = 'light';


function darkmode() {
    button.removeEventListener('click', darkmode);
    document.querySelector('body').style.backgroundColor = "#0E0E0E";
    document.querySelector('.horizonnav').style.backgroundColor = "#272120";
    document.querySelector('.logoimg').setAttribute('src','../static/img/logoDM.png')
    let alist = document.querySelectorAll('a');
    for (i = 0; i < alist.length; i++) {
        alist[i].style.color = "#FFFFFF"
    }
    modeflag = 'dark';
}

function lightmode() {
    button.removeEventListener('click', lightmode);
    document.querySelector('body').style.backgroundColor = "#1FA8F4";
    document.querySelector('.horizonnav').style.backgroundColor = "#FFFFFF";
    document.querySelector('.logoimg').setAttribute('src','../static/img/logo.png')
    let alist = document.querySelectorAll('a');
    for (i = 0; i < alist.length; i++) {
        alist[i].style.color = "#000000"
    }
    document.querySelector('.btn').style.color ="#FFFFFF"
    modeflag = 'light';
}

function modeswitch() {
    if (modeflag == 'light') {
        darkmode();
    } else {
        lightmode();
    }
}
