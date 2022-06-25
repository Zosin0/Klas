function handleSubmit() {
    const email = document.getElementById('email-recover').value;

    localStorage.setItem("EMAIL_RECOVER", email)

    return;
}
