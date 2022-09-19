$( document ).ready(function() {
    
    $( "div#update_header" ).click(function() {
        $("header").empty();
        $("header").text("New Header!!!");
    });
    
});