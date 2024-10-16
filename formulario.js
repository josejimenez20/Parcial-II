function registrarUsuario() {
    const usuario = document.getElementById("usuario").value;
    const clave = document.getElementById("clave").value;
    const nombre = document.getElementById("nombre").value;
    const direccion = document.getElementById("direccion").value;
    const telefono = document.getElementById("telefono").value;

    fetch('/registrar_usuario', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ usuario, clave, nombre, direccion, telefono })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Usuario registrado con éxito');
        } else {
            alert('Error al registrar el usuario');
        }
    })
    .catch(error => console.error('Error:', error));
}
