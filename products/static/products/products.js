'use strict'


const productInput = document.querySelector('.add-product-input');
console.log(productInput)

productInput.addEventListener('input', function(e){
    console.log(this.value)
})