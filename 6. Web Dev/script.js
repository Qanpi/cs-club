const buttonElement = document.getElementById("btn");
let degrees = 0;

buttonElement.addEventListener("click", doStuff)

function doStuff() {
    degrees += 360;
    buttonElement.style.transform = `rotate(${degrees}deg)`;
}

