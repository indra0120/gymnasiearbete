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