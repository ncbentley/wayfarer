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