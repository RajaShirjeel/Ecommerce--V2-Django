const categoryLink = document.querySelector('.category-link');
const navCatContainer = document.querySelector('.nav__categories--container');
const nav = document.querySelector('.nav');
const searchIcon = document.querySelector('.nav-search-icon');
const searchBar = document.querySelector('.nav__searchbar');
const crossIcon = document.querySelector('.searchbar-icon');
const overlay = document.querySelector('.nav__searchbar-overlay');
const cartIcon = document.querySelector('.nav-cart-icon');
const hideCartIcon = document.querySelector('.cart-icon');
const cartSlider = document.querySelector('.nav__cart__slider');


const showCategories = function () {
    navCatContainer.classList.remove('hidden');
    navCatContainer.removeAttribute('inert');
};

const hideCategories = function () {
    navCatContainer.classList.add('hidden');
    navCatContainer.setAttribute('inert', '');
};

const showSearchbar = function(){
    searchBar.classList.remove('hide-searchbar');
    searchBar.removeAttribute('inert');
    overlay.classList.remove('hide-overlay');
    overlay.removeAttribute('inert');
}

const hideSearchbar = function(){
    searchBar.classList.add('hide-searchbar');
    searchBar.setAttribute('inert', '');
    overlay.classList.add('hide-overlay');
    overlay.setAttribute('inert', '');
}

const showCart = function(){
    cartSlider.classList.remove('hide-cart');
    cartSlider.removeAttribute('inert');
}

const hideCart = function(){
    cartSlider.classList.add('hide-cart');
    cartSlider.setAttribute('inert', '');
}



categoryLink.addEventListener('mouseover', showCategories);
nav.addEventListener('mouseleave', hideCategories);
searchIcon.addEventListener('click', showSearchbar);
crossIcon.addEventListener('click', hideSearchbar);
cartIcon.addEventListener('click', showCart);
hideCartIcon.addEventListener('click', hideCart);
