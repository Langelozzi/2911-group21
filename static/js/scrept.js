//import revJson from "/data/reviews.json" assert {type: 'json'};
const button = document.querySelector('.form-check-input');
//button.addEventListener('click', modeswitch);
var modeflag = 'light';


var review_obj={
    /*rating*/0:"",
    /*title*/1:"",
    /*course*/2:"",
    /*instructor*/ 3:"",
    /*contant*/ 4:"",
};


/*
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
    console.log(review_obj)
}

function editPost(){
    console.log(review_obj)
    var inputContainDiv = document.querySelector(".container")
    var inputfield =inputContainDiv.getElementsByTagName('input');
    var textarea = inputContainDiv.getElementsByTagName('textarea');
    inputfield[0].value = review_obj[1]
    inputfield[1].value = review_obj[2]
    inputfield[2].value = review_obj[3]
    inputfield[3].value = review_obj[0]
    textarea.value = review_obj[4]

    for (i = 0; i<5;i++){
        review_obj[i] = ''
    }
}
*/

function darkmode() {
    button.removeEventListener('click', darkmode);
    document.querySelector('body').style.backgroundColor = "#0E0E0E";
    document.querySelector('.horizonnav').style.backgroundColor = "#2A2A2A";
    document.querySelector('.logoimg').setAttribute('src','../static/img/logoDM.png')
    document.querySelector('.posting').style.backgroundColor = "#2A2A2A";
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
    document.querySelector('body').style.backgroundColor = "#03376b";
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

function deleteprompt(page) {
  let text = "Are you sure you want to delete your review?\nPress OK to continue";
  let popup = confirm(text)
  if (popup == true) {
    location.href = "/delete";
  } else {
    if (page == "edit") {
      location.href = "/edit";
    } else if (page == "home") {
      location.href = "/userhome";
    }
  }
  //have to return because the button is in a form and when a form is submitted, it ignores any other requests
  // such as changing pages
  return false
}