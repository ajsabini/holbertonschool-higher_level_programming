$( document ).ready(function() {
    
        $.get( "https://swapi-api.hbtn.io/api/films/?format=json", function( data ) {
            arrayResults = data.results;
            arrayResults.forEach(element => $("ul#list_movies").append("<li>" + element.title + "</li>"));
        });
 
});