let authentication = () => {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
 
    if (username === 'admin' && password === 'admin') {
        // lanjut ke halaman setelah login
        window.location.href = 'success.html';
        alert('Login Berhasil');
    } else {
        alert('Username atau Password salah');
    }
}
