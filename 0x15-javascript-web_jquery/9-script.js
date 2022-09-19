$( document ).ready(function() {
        var url = "https://stefanbohacek.com/hellosalut/?lang=fr";
        $.get( url , function( data ) {
            $( "div#hello" ).text( data.hello );
        });
 
});