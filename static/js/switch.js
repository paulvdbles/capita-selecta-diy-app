document.addEventListener('DOMContentLoaded', function () {

    var switches = document.getElementsByClassName('switch');
    var deleteButtons = document.getElementsByClassName('delete');

    for (var i = 0; i < switches.length; i++) {
        switches[i].addEventListener('click', switchClicked);
    }

    for (var i = 0; i < deleteButtons.length; i++) {
        deleteButtons[i].addEventListener('click', deleteButtonClicked);
    }

    function switchClicked() {
        var state = $(this).attr('checked');

        if (typeof state !== typeof undefined && state !== false) {
            $(this).removeAttr('checked');
            turnLightOff(this);
        }
        else {
            $(this).attr('checked', 'checked');
            turnLightOn(this);
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
            console.log("Light turned on!");
        });

        posting.fail(function () {
            console.log("Error: light didn't turned on!");
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
            console.log("Light turned off!");
        });

        posting.fail(function () {
            console.log("Error: light didn't turned off!");
        });
    }

    function deleteButtonClicked() {
        var ip = $(this).attr('ip');

        var posting = $.ajax({
            method: "POST",
            url: '/ajax/delete_light/',
            data: {'light_ip': ip},
            dataType: 'json'
        });

        $(this).closest('.tr').remove();

        posting.done(function () {
            console.log("Light deleted!");
        });

        posting.fail(function () {
            console.log("Error: light wasn't deleted!");
        });
    }
});