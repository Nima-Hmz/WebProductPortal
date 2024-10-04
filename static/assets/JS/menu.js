const menuButton = document.getElementById('menuButton');
const mobileMenu = document.getElementById('mobileMenu');


const swiperButtonPrev = document.querySelector('.swiper-button-prev');
const swiperButtonNext = document.querySelector('.swiper-button-next');


// Mobile Menu Toggle
menuButton.addEventListener('click', () => {
    mobileMenu.classList.toggle('translate-x-full');
    mobileMenu.classList.toggle('translate-x-0');
    try {
        swiperButtonPrev.classList.toggle('hidden');
        swiperButtonNext.classList.toggle('hidden');
    } catch (e) {
        return
    }
});

// Close the mobile menu when clicking on a menu item
const menuItems = mobileMenu.querySelectorAll('a');
menuItems.forEach(item => {
    item.addEventListener('click', () => {
        mobileMenu.classList.add('translate-x-full');
    });
})
    ///////////////////////////////////////////////////////
    ;