const showBtn = document.querySelector('.p-hide');
const passInput = document.querySelector('#id_password');

showBtn.addEventListener('click', () => {
   if (passInput.getAttribute('type') === 'password') {
    passInput.setAttribute('type', 'text');
    showBtn.textContent = 'HIDE';
   } 

   else {
    passInput.setAttribute('type', 'password');
    showBtn.textContent = 'SHOW';
   }


})