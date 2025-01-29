const categoryLink = document.querySelector('.category-link');
const navCatContainer = document.querySelector('.nav__categories--container');
const nav = document.querySelector('.nav');
const searchIcon = document.querySelectorAll('.nav-search-icon');
const searchBar = document.querySelectorAll('.nav__searchbar');
const crossIcon = document.querySelectorAll('.searchbar-icon');
const overlay = document.querySelectorAll('.nav__searchbar-overlay');
const cartIcon = document.querySelector('.nav-cart-icon');
const hideCartIcon = document.querySelector('.cart-icon');
const cartSlider = document.querySelector('.nav__cart__slider');
const modalIcon = document.querySelector('.mobile__nav--icon');
const hideModalIcon = document.querySelector('.modal-cancel');
const modalContainer = document.querySelector('.mobile__nav--modal');
const modalOverlay = document.querySelector('.modal-overlay');


const showCategories = function () {
    navCatContainer.classList.remove('hidden');
    navCatContainer.removeAttribute('inert');
};

const hideCategories = function () {
    navCatContainer.classList.add('hidden');
    navCatContainer.setAttribute('inert', '');
};

const showSearchbar = function(){
    searchBar.forEach(bar => {
        bar.classList.remove('hide-searchbar');
    });
    searchBar.forEach(bar => {
        bar.removeAttribute('inert');
    });
    overlay.forEach(layer => {
        layer.classList.remove('hide-overlay');
    });
    overlay.forEach(layer => {
        layer.removeAttribute('inert')
    });
}

const hideSearchbar = function(){
    searchBar.forEach(bar => {
        bar.classList.add('hide-searchbar');
    })
    searchBar.forEach(bar => {
        bar.setAttribute('inert', '');
    })
    overlay.forEach(layer => {
        layer.classList.add('hide-overlay');
    });
    overlay.forEach(layer => {
        layer.setAttribute('inert', '')
    });
}

const showCart = function(){
    cartSlider.classList.remove('hide-cart');
    cartSlider.removeAttribute('inert');
}

const hideCart = function(){
    cartSlider.classList.add('hide-cart');
    cartSlider.setAttribute('inert', '');
}

const showModal = function(){
    modalContainer.classList.remove('hidden');
    modalContainer.removeAttribute('inert');
    modalOverlay.classList.remove('hide');

}

const hideModal = function(){
    modalContainer.classList.add('hidden');
    modalContainer.setAttribute('inert', '');
    modalOverlay.classList.add('hide');
}

searchIcon.forEach(icon => {
    icon.addEventListener('click', showSearchbar);
})
crossIcon.forEach(icon => {
    icon.addEventListener('click', hideSearchbar);
})

categoryLink.addEventListener('mouseover', showCategories);
nav.addEventListener('mouseleave', hideCategories);
cartIcon.addEventListener('click', showCart);
hideCartIcon.addEventListener('click', hideCart);
modalIcon.addEventListener('click', showModal);
hideModalIcon.addEventListener('click', hideModal);
