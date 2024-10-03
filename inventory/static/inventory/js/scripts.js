
// inventory/static/inventory/js/scripts.js

document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.getElementById("menu-toggle");
    const wrapper = document.getElementById("wrapper");

    menuToggle.addEventListener("click", function(e) {
        e.preventDefault();
        wrapper.classList.toggle("toggled");
    });
});
