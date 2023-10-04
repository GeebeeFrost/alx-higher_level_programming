$.ajax({
  url: "https://swapi-api.alx-tools.com/api/films/?format=json",
  type: "GET",
  dataType: "json",
}).done((res) => {
  let films = res.results;
  films.forEach((film) => {
    $("<li>").text(film.title).appendTo("UL#list_movies");
  });
});
