// The function only runs after the page has completely loaded.
window.addEventListener('load', (event) => {
    // Code for the toggle function on the menu.
    // Get the elements from the page.
    const hamButton = document.querySelector('.ham');
    const mainNav = document.querySelector('.navigation');

    // When the menu button is clicked, toggle the responsive class.
    hamButton.addEventListener('click', () => {mainNav.classList.toggle('responsive')}, false);

    // If the window because too big, remove the responsive class
    window.onresize = () => {if (window.innerWidth > 760) mainNav.classList.remove('responsive')};
});
