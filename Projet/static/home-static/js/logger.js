function Logger(id) {
    this.id = id;
    this.screen = document.getElementById(id);
}

Logger.prototype.log = function (data) {
    this.screen.innerHTML += data + "<br />";
    console.log(data);
};

var logger;

function main() {
    logger = new Logger("screen");
}
