//import revJson from "/data/reviews.json" assert {type: 'json'};
const button = document.querySelector('.form-check-input');
button.addEventListener('click', modeswitch);
var modeflag = 'light';

var review_obj={
    /*rating*/0:"",
    /*title*/1:"",
    /*course*/2:"",
    /*instructor*/ 3:"",
    /*contant*/ 4:"",
};



function editGet(){
    var text = [];
    
    
    var entrypoint = document.getElementById('editButton')
    var parent = entrypoint.parentElement.closest('div');
    targetID = parent.id
    let target = document.getElementById(targetID)
    let lis = target.querySelectorAll("li")
    for (i = 0; i<5;i++){
        let li_subtags = lis[i].firstChild;
        let sub_tag_text = li_subtags.textContent;
        text.push(sub_tag_text);
    }
    for (i = 0; i<5;i++){
    review_obj[i] = text[i]
    }
    review_obj[0] = review_obj[0].replace('rating ','')
}

function editPost(){
    var inputContainDiv = document.querySelector(".container")
    var inputfield =inputContainDiv.getElementsByTagName('input');
    



}


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

