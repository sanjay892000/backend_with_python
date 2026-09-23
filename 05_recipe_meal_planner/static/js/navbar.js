// SELECTORS

const header = document.querySelector(".header");
const menu = document.querySelector(".nav-menu");
const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelectorAll(".nav-menu a");

// STICKY NAVBAR

window.addEventListener("scroll", () => {
    if (window.scrollY > 30) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }
});

// MOBILE MENU TOGGLE

menuToggle.addEventListener("click", () => {
    menu.classList.toggle("active");
    menuToggle.classList.toggle("active");

    document.body.classList.toggle("menu-open");
});

// CLOSE MENU AFTER CLICK

navLinks.forEach(link => {

    link.addEventListener("click", () => {

        menu.classList.remove("active");
        menuToggle.classList.remove("active");
        document.body.classList.remove("menu-open");

    });

});

// ACTIVE LINK

navLinks.forEach(link => {

    link.addEventListener("click", function () {

        navLinks.forEach(item => {
            item.classList.remove("active");
        });

        this.classList.add("active");

    });

});

// CLOSE MENU ON WINDOW RESIZE

window.addEventListener("resize", () => {

    if (window.innerWidth > 992) {

        menu.classList.remove("active");
        menuToggle.classList.remove("active");
        document.body.classList.remove("menu-open");

    }

});