#!/usr/bin/node


$('DIV#toggle_header').click(function() {
    if ($('header').hasClass('red'))
        $('header').addClass('green').removeClass('red')
    else
        $('header').addClass('red').remove('green')
});