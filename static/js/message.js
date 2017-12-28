document.addEventListener('DOMContentLoaded', function () {
    document.getElementById("delete").addEventListener("click", deleteMessage);

    function deleteMessage() {
        document.getElementById("message").remove();
    }
});