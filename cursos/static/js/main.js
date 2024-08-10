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


function toggleSection(sectionId, contentId, symbolId) {
    var content = document.getElementById(contentId);
    var symbol = document.getElementById(symbolId);

    if (content.style.maxHeight) {
        // If the section is currently expanded, collapse it
        content.style.maxHeight = null;
        content.style.display = "none";
        symbol.classList.remove('rotado');
    } else {
        // Expand the section
        content.style.display = "block";
        content.style.maxHeight = content.scrollHeight + "px";
        symbol.classList.add('rotado');
    }
}

document.querySelectorAll('.expandible').forEach(function(button) {
    var sectionId = button.id;
    var contentId = 'content' + sectionId.replace('section', '');
    var symbolId = 'symbol' + sectionId.replace('section', '');

    button.addEventListener('click', function() {
        toggleSection(sectionId, contentId, symbolId);
    });
});