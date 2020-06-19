$('.city-card').on('click', (event) => {
    let x = 0;
    const parent = event.target.parentNode;
    for (let i = 1; i < parent.children.length; i++) {
        if (parent.children[i] == event.target) {
            break;
        }
        x += 1;
    }
    console.log($('.city-detail'))
    $('.city-detail').addClass('hidden');
    $($('.city-detail')[x]).removeClass('hidden');
    $('.city-card').removeClass('active');
    $(event.target).addClass('active');
})