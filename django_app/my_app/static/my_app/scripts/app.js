let items = document.querySelectorAll('.header__item'),
path = window.location.pathname;
for (item of items) {
    if (item.firstElementChild.getAttribute('href') == path) {
        item.classList.add('active')
    }
}
