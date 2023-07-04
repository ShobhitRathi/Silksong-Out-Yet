function updateDateTime() {
    var currentDate = new Date();
    var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' };
    var formattedDateTime = currentDate.toLocaleString('en-US', options);
    document.getElementById("current-date-time").textContent = formattedDateTime;
}

setInterval(updateDateTime, 1000); // Update the date and time every second

window.addEventListener('DOMContentLoaded', (event) => {
    var video = document.getElementById('background-video');

    video.addEventListener('click', function() {
        if (video.paused) {
            video.play();
        } else {
            video.pause();
        }
    });
});

function updateStatistics() {
    var eventDate = new Date("2019-02-14");
    var currentDate = new Date();
    var timeDiff = currentDate - eventDate;

    var days = Math.floor(timeDiff / (1000 * 60 * 60 * 24));
    var weeks = Math.floor(days / 7);
    var hours = Math.floor(timeDiff / (1000 * 60 * 60));
    var minutes = Math.floor(timeDiff / (1000 * 60));
    var seconds = Math.floor(timeDiff / 1000);

    document.getElementById("days-since-reveal").textContent = "Days since last reveal: " + days;
    document.getElementById("weeks-since-reveal").textContent = "Weeks since last reveal: " + weeks;
    document.getElementById("hours-since-reveal").textContent = "Hours since last reveal: " + hours;
    document.getElementById("minutes-since-reveal").textContent = "Minutes since last reveal: " + minutes;
    document.getElementById("seconds-since-reveal").textContent = "Seconds since last reveal: " + seconds;
}

setInterval(updateStatistics, 1000);