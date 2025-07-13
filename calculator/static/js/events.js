$(document).ready(function() {
    $("#inputform").on("submit", eval);
});

function eval(e) {
    e.preventDefault();

    $.post('/evaluate', $('#inputform').serialize(), function(data) {
        $('#result').html(data['result']);
    });
}
