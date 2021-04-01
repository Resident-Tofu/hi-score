$(document).ready(function() {

    // If like button clicked, increment likes for review and hide button
    $('#like_btn').click(function(){
        var reviewid;
        reviewid = $(this).attr("data-reviewid");
         $.get('/hi-score/like-review/', {review_id: reviewid}, 
         function(data){
                   $('#like_count').html(data);
                   $('#likes').hide();
               });
    });
    
    // Display 1 to 5 stars according to the review's rating
    $(".stars").each(function() {
        var str = "";
        var num = $(this).data("rat");
        for (i = 0; i < num; i += 1) { str += "&#11088;"; }
        $(this).html(str);
    });

    // If using captions from youtube video, get the XML for them and parse
    $(".cap").each(function() {
        // Maybe update model so it just stored id?
        var str = $(this).data("emb");
        var vid = str.slice(str.lastIndexOf("/") + 1);
        var captions = $(this);

        $.ajax({
            type: "GET",
            url: "https://video.google.com/timedtext?lang=en&v=" + vid,
            crossDomain: true
        }).done(function(response) {
            var txt = "";

            $(response).find("text").each(function() {
                txt += $(this).text() + " ";
            });
    
            captions.text($("<div />").html(txt).text()); // reference: https://stackoverflow.com/a/22279245
        }).fail(function(response) {
            captions.text(response); // Handle case when captions could not be obtained
        });

    });
});

