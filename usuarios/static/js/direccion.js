function go_to_cart(){
    var url = $("#btn_carrito").attr("data-url");
    location.href=url;
}

function go_to_ingrediente(){
    var url_ref = $("#btn_ingrediente").attr("data-url").substring(1)
    var url = new URL(location.href+url_ref);
    url.href += '?ingrediente';
    location.href=url;
}

function go_to_alimento(){
    var url_ref = $("#btn_alimento").attr("data-url").substring(1)
    var url = new URL(location.href+url_ref);
    url.href += '?alimento';
    location.href=url;
}

function go_to_kit(){
    var url_ref = $("#btn_kit").attr("data-url").substring(1)
    var url = new URL(location.href+url_ref);
    url.href += '?kit';
    location.href=url;
}

function go_to_producto(){
    var url = $("#btn_producto").attr("data-url");
    location.href=url;
}

function go_to_pedidos(){
    var url = $("#btn_pedidos").attr("data-url");
    location.href=url;
}