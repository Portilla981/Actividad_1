document.addEventListener("DOMContentLoaded", function() {
    const loginElement = document.querySelector(".login-container");

    if (loginElement) {
        fetch("/view/componentes/login.html")
            .then(response => response.text())
            .then(data => {
                loginElement.innerHTML = data;
            })
            .catch(error => console.log("Error cargando el login", error));
    }   
});