function add_to_cart(){
    const csrftoken = Cookies.get('csrftoken');
    const product = $("#product-id").attr("value");
    $.ajax({
    url: '/productos/add_cart/',
    data: { product: product },
    headers: {'X-CSRFToken': csrftoken},
    method : 'POST',
    success: function() {
    alert('Añadido al carrito')
    }
    }); }