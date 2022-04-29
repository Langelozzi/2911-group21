const button = document.querySelector('.darkmode_switch');
button.addEventListener('click', modeswitch);
var modeflag = 'light';


function darkmode() {
    button.removeEventListener('click', darkmode);
    document.querySelector('body').style.backgroundColor = "#0E0E0E";
    document.querySelector('.horizonnav').style.backgroundColor = "#272120";
    let alist = document.querySelectorAll('a');
    for (i = 0; i < alist.length; i++) {
        alist[i].style.color = "#FFFFFF"
    }
    modeflag = 'dark';
}

function lightmode() {
    button.removeEventListener('click', lightmode);
    document.querySelector('body').style.backgroundColor = "#1FA8F4";
    document.querySelector('.horizonnav').style.backgroundColor = "#0921db";
    let alist = document.querySelectorAll('a');
    for (i = 0; i < alist.length; i++) {
        alist[i].style.color = "#000000"
    }
    modeflag = 'light';
}

function modeswitch() {
    if (modeflag == 'light') {
        darkmode();
    } else {
        lightmode();
    }
}
