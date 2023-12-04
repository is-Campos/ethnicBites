function searchProducts() {
    var input, filter, cards, cardContainer, title, i;
    input = document.getElementById("ethnic-search");
    filter = input.value.toLowerCase();
    cardContainer = document.getElementById("cards-container");
    containers = cardContainer.getElementsByClassName("col");
    cards = cardContainer.getElementsByClassName("card-products");
    for (i = 0; i < cards.length; i++) {
        title = cards[i].querySelector(".card-body");
        if (title.innerText.toLowerCase().indexOf(filter) > -1) {
            containers[i].style.display = "";
        } else {
            containers[i].style.display = "none";
        }
    }
}

function filterProductsByCategory(category) {
    var cards, cardContainer, title, i;
    cardContainer = document.getElementById("cards-container");
    containers = cardContainer.getElementsByClassName("col");
    cards = cardContainer.getElementsByClassName("card-products");
    for (i = 0; i < cards.length; i++) {
        title = cards[i].querySelector(".card-body");
        if (title.innerText.toLowerCase().indexOf(category) > -1) {
            containers[i].style.display = "";
        } else {
            containers[i].style.display = "none";
        }
    }
}

function filterProductsByType(type) {
    var cards, cardContainer, title, i;
    cardContainer = document.getElementById("cards-container");
    containers = cardContainer.getElementsByClassName("col");
    cards = cardContainer.getElementsByClassName("card-products");
    for (i = 0; i < cards.length; i++) {
        title = cards[i].querySelector(".card-body");
        if ($(title).attr('type').toLowerCase().indexOf(type) > -1) {
            containers[i].style.display = "";
        } else {
            containers[i].style.display = "none";
        }
    }
    header_product = document.getElementById("header-products")
    switch (type) {
        case 'kit':
            header_product.innerText = "Kits recomendados";
            break;
        case 'ingrediente':
            header_product.innerText = "Ingredientes recomendados";
            break;
        default:
            header_product.innerText = "Platos recomendados";
            break;
    }
}


function go_to_cart(){
    var url = $("#btn_carrito").attr("data-url");
    location.href=url;
}

$(function(){
    filterProductsByType('alimento');
    $('#italiana').click(function (e) {
        if($(this).attr('aria-pressed') === 'false'){
            filterProductsByCategory("california")
        }else{
            filterProductsByCategory("")
        }
        $('#mexicana').removeClass('active'),
        $('#japonesa').removeClass('active'),
        $('#francesa').removeClass('active'),
        $('#kosher').removeClass('active'),
        $('#vegana').removeClass('active')
      });
      
      $('#mexicana').click(function (e) {
        if($(this).attr('aria-pressed') === 'false'){
            filterProductsByType("kit")
        }else{
            filterProductsByType("")
        }
        $('#francesa').removeClass('active'),
        $('#japonesa').removeClass('active'),
        $('#italiana').removeClass('active'),
        $('#kosher').removeClass('active'),
        $('#vegana').removeClass('active')
      });

      $('#japonesa').click(function (e) {
        $('#mexicana').removeClass('active'),
        $('#italiana').removeClass('active'),
        $('#francesa').removeClass('active'),
        $('#kosher').removeClass('active'),
        $('#vegana').removeClass('active')
      });

      $('#francesa').click(function (e) {
        $('#mexicana').removeClass('active'),
        $('#japonesa').removeClass('active'),
        $('#italiana').removeClass('active'),
        $('#kosher').removeClass('active'),
        $('#vegana').removeClass('active')
      });

      $('#vegana').click(function (e) {
        $('#mexicana').removeClass('active'),
        $('#japonesa').removeClass('active'),
        $('#italiana').removeClass('active'),
        $('#francesa').removeClass('active'),
        $('#kosher').removeClass('active')
      });

      $('#kosher').click(function (e) {
        $('#mexicana').removeClass('active'),
        $('#japonesa').removeClass('active'),
        $('#italiana').removeClass('active'),
        $('#francesa').removeClass('active'),
        $('#vegana').removeClass('active')
      });

});