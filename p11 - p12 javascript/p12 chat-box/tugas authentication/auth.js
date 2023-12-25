let authentication = () => {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
 
    if (username === 'AbdullahQaidMuaadz' && password === 'student-nf23') {
        // lanjut ke halaman setelah login
        window.location.href = 'success.html';
        alert('Login Berhasil');
    } else {
        alert('Username atau Password salah');
    }
}
