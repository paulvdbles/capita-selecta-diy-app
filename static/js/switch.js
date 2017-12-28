document.addEventListener('DOMContentLoaded', function () {

    var switches = document.getElementsByClassName('switch');

    for (var i = 0; i < switches.length; i++) {
        switches[i].addEventListener('click', printMessage);
    }

    function printMessage() {
        console.log("switch aangeklikt!");

        $.ajax({
            type: "POST",
            url: '/ajax/switch_light/',
            data: {'light_ip': this.id},
            dataType: 'json'
        });
    }
});