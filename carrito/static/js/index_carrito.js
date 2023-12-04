function delete_from_cart(p){
    const csrftoken = Cookies.get('csrftoken');
    const product = p.value;
    $.ajax({
    url: 'delete_from_cart/',
    data: { product: product },
    headers: {'X-CSRFToken': csrftoken},
    method : 'POST',
    success: function() {
        productContainer = document.getElementById(product);
        productContainer.remove();
        total = calculate_total();
        if(total==0){
            delete_cart();
        }
        else{
            alert('Producto eliminado del carrito');
        }
        
    }
    }); 
}

function delete_cart(paid=false){
    const csrftoken = Cookies.get('csrftoken');
    $.ajax({
    url: 'delete_cart/',
    headers: {'X-CSRFToken': csrftoken},
    method : 'POST',
    success: function() {
        cart = document.getElementById("cart");
        cart.remove();
        document.getElementById('cart-section-container').classList.add('one-np');
        document.getElementById('payment-section-container').remove();
        document.getElementById("details-container").innerHTML += "<p id='empty-cart'>No hay productos en el carrito</p>";
        if(!paid){
            alert('Carrito vaciado');
        } 
    }
    }); 
}

function update_quantity_cart(p,qty){
    const csrftoken = Cookies.get('csrftoken');
    const product = p;
    const quantity = qty;
    $.ajax({
    url: 'update_quantity_cart/',
    data: { product: product, quantity:quantity },
    headers: {'X-CSRFToken': csrftoken},
    method : 'POST',
    success: function() {
        quantity_container = document.getElementById(p);
        span_cantidad = quantity_container.getElementsByClassName("cantidad");
        if(span_cantidad.length==1){
            span_cantidad[0].innerText=quantity;
        }
        calculate_total();
    }
    }); 
}

function calculate_total(){
    ps = document.getElementsByClassName("product-description");
    total = 0;
    
    for (let p of ps) {
        price = parseFloat(p.querySelector(".precio").innerText);
        qty = parseFloat(p.querySelector(".cantidad").innerText);
        subtotal = price * qty;
        total += subtotal;
    }
    total = total.toFixed(2)
    total_container = document.getElementById("total");
    if(total_container!=null){
        total_container.innerText = total;
    }

    return total;

}

function pay(metodo_pago){
    const csrftoken = Cookies.get('csrftoken');
    var _url = $("#btn_pago").attr("data-url");
    const amount = calculate_total();
    const metodo = metodo_pago.value;
    $.ajax({
    url: _url,
    data: { amount: amount, metodo:metodo },
    headers: {'X-CSRFToken': csrftoken},
    method : 'POST',
    success: function() {
        alert('Pago exitoso');
        delete_cart(true);
    }
    }); 
}

$(function(){
    calculate_total();
});

$(function(){
    $('.btn-number').click(function(e){
        e.preventDefault();
        
        fieldName = $(this).attr('data-field');
        type      = $(this).attr('data-type');
        var input = $("input[name='"+fieldName+"']");
        var currentVal = parseInt(input.val());
        if (!isNaN(currentVal)) {
            if(type == 'minus') {
                
                if(currentVal > input.attr('min')) {
                    input.val(currentVal - 1).change();
                } 
                if(parseInt(input.val()) == input.attr('min')) {
                    $(this).attr('disabled', true);
                }

            } else if(type == 'plus') {

                if(currentVal < input.attr('max')) {
                    input.val(currentVal + 1).change();
                }
                if(parseInt(input.val()) == input.attr('max')) {
                    $(this).attr('disabled', true);
                }

            }
        } else {
            input.val(0);
        }
    });
    $('.input-number').focusin(function(){
        $(this).data('oldValue', $(this).val());
    });
    $('.input-number').change(function() {
        
        minValue =  parseInt($(this).attr('min'));
        maxValue =  parseInt($(this).attr('max'));
        valueCurrent = parseInt($(this).val());
        if(valueCurrent >= minValue && valueCurrent <= maxValue){
            update_quantity_cart($(this).attr('product_id'),valueCurrent);
        }
        name = $(this).attr('name');
        if(valueCurrent >= minValue) {
            $(".btn-number[data-type='minus'][data-field='"+name+"']").removeAttr('disabled')
        } else {
            alert('La cantidad no puede ser menor a 1');
            $(this).val($(this).data('oldValue'));
        }
        if(valueCurrent <= maxValue) {
            $(".btn-number[data-type='plus'][data-field='"+name+"']").removeAttr('disabled')
        } else {
            alert('No hay suficiente en existencia');
            $(this).val($(this).data('oldValue'));
        }
        
    });
    $(".input-number").keydown(function (e) {
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 190]) !== -1 ||
                (e.keyCode == 65 && e.ctrlKey === true) || 
                (e.keyCode >= 35 && e.keyCode <= 39)) {
                    return;
        }
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    });  
});