document.addEventListener('DOMContentLoaded', () => {
    var instance = M.Carousel.init(document.querySelector('.carousel'), {
        fullWidth: true
    });
    $('.moveNextCarousel').click(function(e){
        e.preventDefault();
        e.stopPropagation();
        instance.next();
    });
    $('.movePrevCarousel').click(function(e){
        e.preventDefault();
        e.stopPropagation();
        instance.prev();
    });
});

$('#login').click((event) => {
    $('#panel1').addClass('active');
    $('#panel1').addClass('show');
    $('#panel2').removeClass('active');
    $('#panel2').removeClass('show');
    $('#login-link').addClass('active');
    $('#signup-link').removeClass('active');
});

$('#signup').click((event) => {
    $('#panel1').removeClass('active');
    $('#panel1').removeClass('show');
    $('#panel2').addClass('active');
    $('#panel2').addClass('show');
    $('#login-link').removeClass('active');
    $('#signup-link').addClass('active');
});