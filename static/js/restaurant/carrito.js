
function notificacionSuccess(mensaje) {
	Swal.fire({
		title: 'Buen Trabajo!',
		text: mensaje,
		icon: 'success'
	})
}

document.getElementById('btn btn-success').addEventListener('click', function(){
  notificacionSuccess(mensaje);
});

function alerta()
    {
    var mensaje;
    var opcion = confirm("La compra se a realizado !");
    if (opcion == true) {
        mensaje = "Has clickado OK";
	} else {
	    mensaje = "Has clickado Cancelar";
	}
	document.getElementById("btn btn-success").innerHTML = mensaje;
}
