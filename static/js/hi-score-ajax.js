$(document).ready(function() {
    
    $(".stars").each(function() {
        var str = "";
        var num = $(this).data("rat");
        for (i = 0; i < num; i += 1) { str += "&#11088;"; }
        $(this).html(str);
    });

    /*
    $(".cap").each(function() {
        $(this).text($(this).data("emb"));
    });
    */

});