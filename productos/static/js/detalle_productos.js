function add_to_cart(){
    $.ajax({
    url: '/productos/add_cart/',
    method : 'POST',
    success: function() {
    alert('Añadido al carrito')
    }
    }); }