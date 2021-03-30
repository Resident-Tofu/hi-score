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
    $(".cap").each(function() {
        //$(this).text($(this).data("emb"));

        // Maybe update model so it just stored id?
        var str = $(this).data("emb");
        var vid = str.slice(str.lastIndexOf("/") + 1);
        var link = "https://video.google.com/timedtext?lang=en&v=" + vid
        $(this).text(link);

        $.ajax({
            type: "POST",
            url: link
        }).done(function(response) {
            $(this).text("YEAH");
        }).fail(function(response) {
            $(this).text("NOPE");
        });

    });
    
});