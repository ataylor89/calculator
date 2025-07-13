$(document).ready(function() {
    $("#inputform").on("submit", eval);
});

function eval(e) {
    e.preventDefault();
    console.log("Calling the eval function...");

    $.post('/evaluate', $('#inputform').serialize(), function(data) {
        $('#result').html(data['result']);
    });
}
