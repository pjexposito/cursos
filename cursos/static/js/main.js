function showInfoBox(message) {
    const infoBox = document.getElementById('info-box');
    infoBox.textContent = message;
    infoBox.classList.add('show');
    setTimeout(() => {
        infoBox.classList.remove('show');
    }, 5000); // 5000ms = 5 segundos
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
    observer.observe(marker);
});