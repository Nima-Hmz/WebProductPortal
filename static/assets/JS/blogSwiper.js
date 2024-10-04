
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        '730': {
            slidesPerView: 3,
            spaceBetween: 20,
        }
    }
});

const onCloseMenu = () => {
    onClickMenuButton()
}





