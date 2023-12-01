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

function go_to_cart(){
    var url = $("#btn_carrito").attr("data-url");
    location.href=url;
}

$(function(){
    $('#italiana').click(function (e) {
        if($(this).attr('aria-pressed') === 'false'){
            filterProductsByCategory("california")
        }else{
            filterProductsByCategory("")
        }
        $('#mexicana').removeClass('active'),
        $('#japonesa').removeClass('active'),
        $('#francesa').removeClass('active')
      });
      
      $('#mexicana').click(function (e) {
        $('#francesa').removeClass('active'),
        $('#japonesa').removeClass('active'),
        $('#italiana').removeClass('active')
      });

      $('#japonesa').click(function (e) {
        $('#mexicana').removeClass('active'),
        $('#italiana').removeClass('active'),
        $('#francesa').removeClass('active')
      });

      $('#francesa').click(function (e) {
        $('#mexicana').removeClass('active'),
        $('#japonesa').removeClass('active'),
        $('#italiana').removeClass('active')
      });
});