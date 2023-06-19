function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function update_values(data){
    $(".total").text(data.total + "руб.");
    $('#' + data.id + "_quantity").text(data.quantity);
    $('#' + data.id + "_value").text(data.value + "руб.");
}

function add_item(){
    $('.add_item').each((index, el) => {
    $(el).click(function(e){
        e.preventDefault();

        const id = $(el).data('id');

        $.ajax({
            method: "POST",
            url: "http://127.0.0.1:8000/cart/plus",
            dataType: "json",
            data: {
            "id": id
            },
            success: function(data) {
                console.log(data);

                update_values(data)

            },
            error: function(er) {
                console.log(er);
            }
        });
    });
    });
}

function minus_item(){
    $('.minus_item').each((index, el) => {
    $(el).click(function(e){
        e.preventDefault();

        const id = $(el).data('id');

        $.ajax({
            method: "POST",
            url: "http://127.0.0.1:8000/cart/minus",
            dataType: "json",
            data: {
            "id": id
            },
            success: function(data) {
                console.log(data);
                update_values(data)
            },
            error: function(er) {
                console.log(er);
            }
        });
    });
    });
}

$(document).ready(function(){
    add_item()
    minus_item()
})