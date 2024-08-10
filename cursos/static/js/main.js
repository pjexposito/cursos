function showInfoBox(message) {
    const infoBox = document.getElementById('info-box');
    if (infoBox) {
        infoBox.textContent = message;
        infoBox.classList.add('show');
        setTimeout(() => {
            infoBox.classList.remove('show');
        }, 5000); // 5000ms = 5 segundos
    }
}



document.addEventListener("DOMContentLoaded", function() {
    var startTime = Date.now();


    var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {

                url = entry.target.getAttribute("data");
                var timeElapsed = Date.now() - startTime;
                if (timeElapsed >= 5000) {  // 15000 ms = 15 segundos

                    fetch(url, {
                        method: 'GET',
                        credentials: 'same-origin'
                    })
                    .then(response => {
                        if (response.ok) {
                            console.log("Lección marcada como completada.");
                        } else {
                            console.log("Error al marcar la lección como completada.");
                        }
                    })
                    .catch(error => {
                        console.error("Error:", error);
                    });


                    showInfoBox(`Has alcanzado el final del curso`);

                    observer.unobserve(entry.target);  // Deja de observar después de la primera intersección y el tiempo transcurrido
                }
            }
        });
    });

    var marker = document.getElementById("final-marker");
    if (marker) {
        observer.observe(marker);
    }
});

document.addEventListener("DOMContentLoaded", function() {
    var moreText = document.getElementById("moreText");
    var button = document.getElementById("toggleButton");
    
    if (button) {
        button.addEventListener("click", function() {
            if (moreText.style.maxHeight === "0px" || moreText.style.maxHeight === "") {
                moreText.style.maxHeight = "1800px"; // Ajusta esto según la cantidad de texto que desees mostrar
                button.innerHTML = "Mostrar menos";
            } else {
                moreText.style.maxHeight = "0px";
                button.innerHTML = "Mostrar más";
            }
        });
    }
});


document.addEventListener("DOMContentLoaded", function() {
    const expandible = document.querySelector('.expandible');
    const contenido = document.querySelector('.contenido');
    const simbolo = document.querySelector('.simbolo');
    if (expandible) {
        expandible.addEventListener('click', () => {
            if (contenido.style.maxHeight) {
                contenido.style.maxHeight = null;
            } else {
                contenido.style.maxHeight = contenido.scrollHeight + "px";
            }
            simbolo.classList.toggle('rotado');
        });
}
});

document.addEventListener("DOMContentLoaded", function() {
    const menuIcon = document.getElementById('menuIcon');
    if (menuIcon) {
        menuIcon.addEventListener('click', function() {
            const menu = document.getElementById('dropdownMenu');
            if (menu) {
                menu.classList.toggle('show-menu');
            }
        });
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const logoutLink = document.getElementById('logout-link');
    const logoutForm = document.getElementById('logout-form');

    if (logoutLink && logoutForm) {
        logoutLink.addEventListener('click', function(event) {
            event.preventDefault(); // Evita el comportamiento predeterminado del enlace
            logoutForm.submit(); // Envía el formulario de cierre de sesión
        });
    }
});