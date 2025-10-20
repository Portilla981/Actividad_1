document.addEventListener("DOMContentLoaded", function () {
    const navbarBeginer = document.querySelector(".navbar_container");
    
    if (navbarBeginer) {
        fetch("/view/componentes/navbar_sesion.html")
        .then(response => response.text())
        .then(html => {
            navbarBeginer.innerHTML = html;
        })
        .catch(error => console.error("Error al cargar la navbar", error)); 
    }
});
