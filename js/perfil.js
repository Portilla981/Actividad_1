document.addEventListener("DOMContentLoaded", function() {
    const PerfilElement = document.querySelector(".perfil_container");

    if (PerfilElement) {
        fetch("/view/componentes/perfil.html")
            .then(response => response.text())
            .then(data => {
                PerfilElement.innerHTML = data;
            })
            .catch(error => console.log("Error cargando la agenda", error));
    }   
});