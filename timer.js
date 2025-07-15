const moment = require('moment');

function displayTime() {
    const currentTime = moment().format('hh:mm:ss A');
    console.log(currentTime);
    // Update the time every second
    setTimeout(displayTime, 1000);
}

displayTime();
