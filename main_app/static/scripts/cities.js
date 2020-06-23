const executeCityClick = (div) => {
    let x = 0;
    const parent = div.parentNode;
    for (let i = 1; i < parent.children.length; i++) {
        if (parent.children[i] == div) {
            break;
        }
        x += 1;
    }
    window.location.href = `/cities/${x+1}`;
}

$('.city-card').on('click', (event) => {
    executeCityClick(event.target);
});

$('.city-card *').click((event) => {
    event.stopPropagation();
    executeCityClick(event.target.parentNode);
})

$('.add-post').click(() => {
    const cards = $('.city-card');
    let i = 0;
    for (i; i < cards.length; i++) {
        if (cards[i].classList.contains('active')) {
            break;
        }
    }
    $('.select.form-control').val(i + 1);
});