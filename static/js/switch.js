document.addEventListener('DOMContentLoaded', function () {

    var switches = document.getElementsByClassName('switch');

    for (var i = 0; i < switches.length; i++) {
        switches[i].addEventListener('click', switchClicked);
    }

    function switchClicked() {
        var attr = $(this).attr('checked');

        if (typeof attr !== typeof undefined && attr !== false) {
            $(this).removeAttr('checked');
            turnLightOff(this);
        }
        else {
            $(this).attr('checked', 'checked');
            turnLightOn(this)
        }
    }

    function turnLightOn(lamp) {
        console.log("Turn light on");

        var posting = $.ajax({
            method: "POST",
            url: '/ajax/switch_light_on/',
            data: {'light_ip': lamp.id},
            dataType: 'json'
        });

        posting.done(function () {
            console.log("Light turned on!")
        });

        posting.fail(function () {
            console.log("Error: light didn't turned on!")
        });
    }

    function turnLightOff(lamp) {
        console.log("Turn light off");

        var posting = $.ajax({
            method: "POST",
            url: '/ajax/switch_light_off/',
            data: {'light_ip': lamp.id},
            dataType: 'json'
        });

        posting.done(function () {
            console.log("Light turned off!")
        });

        posting.fail(function () {
            console.log("Error: light didn't turned off!")
        });
    }
});