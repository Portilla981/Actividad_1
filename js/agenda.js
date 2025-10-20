document.addEventListener("DOMContentLoaded", function() {
    const AgendaElement = document.querySelector(".Agenda-content");

    if (AgendaElement) {
        fetch("/view/componentes/agendar.html")
            .then(response => response.text())
            .then(data => {
                AgendaElement.innerHTML = data;
            })
            .catch(error => console.log("Error cargando la agenda", error));
    }   
});