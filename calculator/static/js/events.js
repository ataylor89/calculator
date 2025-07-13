$(document).ready(function() {
    $("#inputform").on("submit", eval);
});

function eval(e) {
    e.preventDefault();

    $.post('/evaluate', $('#inputform').serialize(), function(data) {
        $('#result').html('The result is: ' + data['result']);
    });
}
