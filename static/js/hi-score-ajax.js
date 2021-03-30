$(document).ready(function() {
    
    // Display 1 to 5 stars according to the review's rating
    $(".stars").each(function() {
        var str = "";
        var num = $(this).data("rat");
        for (i = 0; i < num; i += 1) { str += "&#11088;"; }
        $(this).html(str);
    });

    // If using captions from youtube video, get the XML for them and parse
    // Reference: https://stackoverflow.com/questions/32142656/get-youtube-captions
    /*
    $(".cap").each(function() {
        $(this).text($(this).data("emb"));
    });
    */

});