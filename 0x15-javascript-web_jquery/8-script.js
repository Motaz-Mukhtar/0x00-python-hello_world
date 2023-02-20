#!/usr/bin/node

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (res) {
  $.each(res.results, function (i) {
    $(`<li>${res.results[i].title}</li>`).appendTo('UL#list_movies');
  });
});
