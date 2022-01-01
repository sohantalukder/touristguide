const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');
togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye / eye slash icon
    this.classList.toggle('bi-eye');
});

const toggle2Password = document.querySelector('#toggle2Password');
const confirmpassword = document.querySelector('#confirmpassword');
toggle2Password.addEventListener('click', function (e) {
    // toggle the type attribute
    const newtype = confirmpassword.getAttribute('type') === 'password' ? 'text' : 'password';
    confirmpassword.setAttribute('type', newtype);
    // toggle the eye / eye slash icon
    this.classList.toggle('bi-eye');
});

function Validate() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmpassword").value;
    if (password != confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }
    return true;
}