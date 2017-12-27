window.onload = function() {
    var el = document.getElementById("message");
    document.getElementById("delete").addEventListener("click", deleteMessage);

    function deleteMessage() {
         el.parentNode.removeChild(el);
    }
};