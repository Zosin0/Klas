window.addEventListener('load', () =>{

    const email = localStorage.getItem('EMAIL_RECOVER');

    document.getElementById('email-result').innerHTML = email;
})
