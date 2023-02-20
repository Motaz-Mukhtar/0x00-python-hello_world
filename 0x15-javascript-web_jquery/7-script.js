#!/usr/bin/node


$.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json'
})

.done(function(data) {
    $('DIV#character').append(`${data.name}`)
})