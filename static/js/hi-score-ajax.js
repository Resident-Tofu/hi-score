$(document).ready(function() {
    $(".stars").each(function() {
        $(this).text($(this).data("rat"));
    });
    $(".cap").each(function() {
        $(this).text($(this).data("emb"));
    });
});