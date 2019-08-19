


var notification;
if (location.protocol === 'https:') {
    notification = new WebSocket('wss://' + window.location.host + '/notifications/');
}
else {
    notification = new WebSocket('ws://' + window.location.host + '/notifications/');
}

notification.onopen = function open() {
    console.log('notification connection created for NotificationWebsocket.');
};
notification.onmessage = function message(event) {
    var data = JSON.parse(event.data);
    console.log("Socket response from NotificationWebsocket => ", data);
};
if (notification.readyState === WebSocket.OPEN) {
    notification.onopen();
}
