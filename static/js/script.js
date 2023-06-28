/* jshint esversion: 11 */

const burgerIcon = document.querySelector("#burger-menu");
const navbarMenu = document.querySelector("#nav-links");

burgerIcon.addEventListener("click", () => {
    navbarMenu.classList.toggle("is-active");
    burgerIcon.classList.toggle("is-active");
});
