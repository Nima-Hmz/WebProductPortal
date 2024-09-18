let imgBorder = document.querySelector(".img-border")
let imgNumber2 = document.querySelector(".img-number-2")
let imgNumber1 = document.querySelector(".img-number1")



if (document.dir === "rtl") {
    imgBorder.style.display = "inline-block"
    imgNumber2.style.display = "inline-block!important"
    imgNumber1.style.width = "210px"
    console.log("mio");

    console.log(imgNumber1);

} else if (document.dir === "ltr") {
    imgBorder.style.display = "none"
    imgNumber1.style.marginLeft = "-140px!important"
    imgNumber1.style.marginRight = "0px"
}

