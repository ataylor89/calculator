$(document).ready(function() {
    $("#inputform").on("submit", eval);
});

function eval(e) {
    e.preventDefault();

    $.post('/evaluate', $('#inputform').serialize(), function(data) {
        if (data['result'] == null) {
            $('#result').html('The expression is invalid');
        }
        else {
            $('#result').html('The result is ' + data['result']);
        }
    });
}
