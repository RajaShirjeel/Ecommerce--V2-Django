'use strict'


const productInput = document.getElementById('add-product-input');
const csrfToken = document.querySelector(`meta[name=csrf-token]`).getAttribute('content');
const container = document.querySelector('.form-product-suggestions');
const list = document.querySelector('.form-suggestion-list');

const handleFocus = function(e){
    setTimeout(() => {
        if (container.classList.contains('input-hidden')) return;
        container.classList.add('input-hidden')
    }, 100)

}


const hideSuggestions = function() {
    container.classList.add('input-hidden')
}


// make api call to django view
const fetchResults = async function(query){
    try{
        const response = await fetch('send-products', {
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrfToken
            },
            method: 'POST',
            body: JSON.stringify({'query': query})
        })

        const content = await response.json();
        const {products} = content;
        console.log(products)
        list.innerHTML = ''
        if (products.length == 0) {
            hideSuggestions();
            return;
        }

        if (productInput.value == '') hideSuggestions();

        products.forEach((p) => {
            const li = document.createElement('li');
            li.classList.add('product-li-item');
            li.textContent = p;
            list.appendChild(li)
        })

        container.classList.remove('input-hidden');
    }
    catch(e){
        console.log(e)
    }

}


const debounce = function(func, delay){
    let countdown;
    return function(...args){
        clearTimeout(countdown);
        countdown = setTimeout(() => {
            func(...args);
        }, delay)
    }
}


const handleDebounce = debounce((e) => {
    const query = e.target.value.trim();
    console.log(query)
    fetchResults(query);
}, 300)


list.addEventListener('click', (e) => {
    productInput.value = e.target.textContent;
})


if (productInput){
    productInput.addEventListener('keyup', handleDebounce);
    productInput.addEventListener('focusout', handleFocus)
}




