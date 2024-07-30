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
                var timeElapsed = Date.now() - startTime;
                if (timeElapsed >= 5000) {  // 15000 ms = 15 segundos
                    showInfoBox(`Has alcanzado el final del curso`);
                    if ("vibrate" in navigator) {
                        navigator.vibrate([200, 100, 200]);  // Vibrar con un patrón: vibrar 200ms, parar 100ms, vibrar 200ms
                    }
                    observer.unobserve(entry.target);  // Deja de observar después de la primera intersección y el tiempo transcurrido
                }
            }
        });
    });

    var marker = document.getElementById("final-marker");
    observer.observe(marker);
});