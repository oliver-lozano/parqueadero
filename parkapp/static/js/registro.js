function verificar() {
  if(document.getElementById('id_clave').value != document.getElementById('id_clave1').value){
    document.getElementById('nomatch').style.display="block";
  }else{
    document.getElementById('usuform').submit();
  }
}
