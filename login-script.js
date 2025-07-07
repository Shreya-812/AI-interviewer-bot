const conatiner = document.querySelector('.container');
const registerBtn = document.querySelector('.register-btn');
const loginBtn = document.querySelector('.login-btn');

registerBtn.addEventListener('click', () => {
    conatiner.classList.add('active');
});

loginBtn.addEventListener('click', () => {
    conatiner.classList.remove('active');
});