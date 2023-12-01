
function add_to_cart(){
    const csrftoken = Cookies.get('csrftoken');
    $.ajax({
    url: '/productos/add_cart/',
    headers: {'X-CSRFToken': csrftoken},
    method : 'POST',
    success: function() {
    alert('Añadido al carrito')
    }
    }); }