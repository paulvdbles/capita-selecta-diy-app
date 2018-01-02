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

        $.ajax({
            type: "POST",
            url: '/ajax/switch_light/',
            data: {'light_ip': lamp.id},
            dataType: 'json'
        });
    }

    function turnLightOff(lamp) {
        console.log("Turn light off");

        $.ajax({
            type: "POST",
            url: '/ajax/switch_light/',
            data: {'light_ip': lamp.id},
            dataType: 'json'
        });
    }
});