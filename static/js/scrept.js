const button = document.querySelector('.form-check-input');
button.addEventListener('click', modeswitch);
var modeflag = 'light';




function id_set(){
    const reviewpost = document.querySelector('.posting')
    var review_post = reviewpost.querySelectorAll('.container-fluid')
    for(i=0; i< review_post.length; i++){
        review_post[i].setAttribute('id', i)
    }
}


window.onload = id_set;



function darkmode() {
    button.removeEventListener('click', darkmode);
    document.querySelector('body').style.backgroundColor = "#0E0E0E";
    document.querySelector('.horizonnav').style.backgroundColor = "#272120";
    document.querySelector('.logoimg').setAttribute('src','../static/img/logoDM.png')
    let alist = document.querySelectorAll('a');
    for (i = 0; i < alist.length; i++) {
        alist[i].style.color = "#FFFFFF"
    }
    let contSelect = document.querySelector(".container")
    let lablelist = contSelect.querySelectorAll('label');
    for (i = 0; i< lablelist.length;i++){
        lablelist[i].style.color = "#FFFFFF"
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
    let contSelect = document.querySelector(".container")
    let lablelist = contSelect.querySelectorAll('label');
    for (i = 0; i< lablelist.length;i++){
        lablelist[i].style.color = "#000000"
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

