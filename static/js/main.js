function showInfoBox(message, tiempo) {
    const infoBox = document.getElementById('info-box');
    if (infoBox) {
        infoBox.textContent = message;
        infoBox.classList.add('show');
        setTimeout(() => {
            infoBox.classList.remove('show');
        }, tiempo*1000); // 10000ms = 10 segundos
    }
}



document.addEventListener("DOMContentLoaded", function() {
    var startTime = Date.now();
    
    var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            console.log("Intersección detectada:", entry);  // Esto mostrará si el marcador está siendo observado
            if (entry.isIntersecting) {
                var timeElapsed = Date.now() - startTime;
                console.log(`Tiempo transcurrido: ${timeElapsed} ms`);
                
                if (timeElapsed >= 5000) {
                    let url = entry.target.getAttribute("data");
                    console.log(`URL a marcar como completada: ${url}`);
                    
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

                    showInfoBox(`Has alcanzado el final del curso`,10);
                    observer.unobserve(entry.target);
                }
            }
        });
    });

    var marker = document.getElementById("final-marker");
    if (marker) {
        observer.observe(marker);
    } else {
        console.log("Marcador no encontrado en el DOM.");
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

let lastScrollTop = 0;
let scrollTimeout;

window.addEventListener('scroll', function() {
    const currentScrollTop = window.pageYOffset || document.documentElement.scrollTop;

    // Verifica si el usuario está haciendo scroll hacia abajo
    if (currentScrollTop > lastScrollTop) {
        // Detecta si el scroll es rápido
        if (Math.abs(currentScrollTop - lastScrollTop) > 70) {
            // Si hay un temporizador activo, cancélalo
            if (scrollTimeout) {
                clearTimeout(scrollTimeout);
            }

            // Detén el scroll
            document.body.style.overflow = 'hidden';
            showInfoBox('Por favor, lee el curso con atención.',2)
            // Establece un temporizador para reactivar el scroll después de 10 segundos
            scrollTimeout = setTimeout(function() {
                document.body.style.overflow = ''; // Restaura el comportamiento de scroll
                console.log('Scroll reactivado.');
            }, 1000);
        }
    }

    lastScrollTop = currentScrollTop;
});