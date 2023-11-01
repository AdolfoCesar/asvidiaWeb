var dibujando = false;
var xInicio, yInicio;

function dibujoLinea() {
  // Al hacer click en el botón, se activa el dibujo
  dibujando = true;
  
  // Al mover el ratón sobre la pantalla, dibujamos una línea
  $(document).mousemove(function(event) {
    if (dibujando) {
      var x = event.pageX;
      var y = event.pageY;
      
      $("#linea").css({
        left: xInicio < x ? xInicio : x,
        top: yInicio < y ? yInicio : y,
        width: Math.abs(x - xInicio),
        height: Math.abs(y - yInicio),
        border: "1px solid black"
      });
    }
  });
  
  // Al hacer click en la pantalla, iniciamos el dibujo
  $(document).mousedown(function(event) {
    dibujando = true;
    xInicio = event.pageX;
    yInicio = event.pageY;
  });
  
  // Al soltar el click, terminamos el dibujo
  $(document).mouseup(function() {
    dibujando = false;
  });
}