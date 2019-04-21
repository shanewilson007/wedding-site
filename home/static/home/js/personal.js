// RSVP Click Buttons
$(function() {
    $('#rsvp1').click(function() {
        $(this).toggleClass('active');

    if ($('#rsvp1').hasClass('active')) {
        $('#popup1').fadeIn();
        $('#popup1').css('display:block');
    }
    });
});

// Accomodations Click Buttons
$(function() {
    $('#details1,#details2,#details3').click(function() {
        $(this).toggleClass('active');

    if ($('#details1').hasClass('active')) {
        $('#popup4').fadeIn();
        $('#popup4').css('display:block');
        }

    else if ($(this).not('.active')) {
        $('#popup4').hide();
    }

    if ($('#details2').hasClass('active')) {
        $('#popup5').fadeIn();
        $('#popup5').css('display:block');
        }

    else if ($(this).not('.active')) {
        $('#popup5').hide();
    }

    if ($('#details3').hasClass('active')) {
        $('#popup6').fadeIn();
        $('#popup6').css('display:block');
        }

    else if ($(this).not('.active')) {
        $('#popup6').hide();
    }
    });
});

// Close Buttons for Popups

$(function() {
    $('button#close').click(function() {
        $('#popup1,#popup4,#popup5,#popup6').hide();
        $('#rsvp1,#details1,#details2,#details3').removeClass('active');
        $('.rsvpBtn').removeClass('selected');
    });
})
