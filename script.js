const userNumber = document.getElementById("user-el")
const numberList = [1,2,3,4,5,6,7,8,9]

function getRandomNumber(){
    let sum = "#"

    for (let i = 0;  i < 4; i++){
    let randomNumber = Math.floor(Math.random()* numberList.length)
    let fullNumber =  (numberList[randomNumber])
    sum += fullNumber
    }    
    userNumber.innerHTML = `${sum}`
}

getRandomNumber()
console.log(getRandomNumber())


const pageToggle = document.querySelector('.page-toggle');
const page = document.querySelector('.page');
const pageOverlay = document.querySelector('.page-overlay');

pageToggle.addEventListener('click', function() {
  page.classList.toggle('active');
  pageOverlay.classList.toggle('active');
});



const pageToggle2 = document.querySelector('.hamburger');

pageToggle2.addEventListener('click', function() {
  page.classList.toggle('active');
  pageOverlay.classList.toggle('active');
});