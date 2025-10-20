document.addEventListener("DOMContentLoaded", function() {
    const FormElement = document.querySelector(".form_register--container");

    if (FormElement) {
        fetch("/view/componentes/form_register.html")
            .then(response => response.text())
            .then(data => {
                FormElement.innerHTML = data;
            })
            .catch(error => console.log("Error cargando el formulario", error));
    }   
});