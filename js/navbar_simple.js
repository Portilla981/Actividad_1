document.addEventListener("DOMContentLoaded", function () {
    const NavbarSimple = document.querySelector(".navbar_container");
    
    if (NavbarSimple) {
        fetch("/view/componentes/navbar_simple.html")
        .then(response => response.text())
        .then(html => {
            NavbarSimple.innerHTML = html;
        })
        .catch(error => console.error("Error al cargar la navbar", error)); 
    }
});
