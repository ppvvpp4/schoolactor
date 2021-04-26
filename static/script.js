window.onload = function(){
    location.href = '?#'
}


document.getElementById('submit_button').onclick = function(){
    var name = document.getElementById('name').value,
        phone = document.getElementById('phone').value,
        email = document.getElementById('email').value,
        question = document.getElementById('commentary').value;


    if (name.length != '' && phone != '' && question != '' && email != '') {

        $.ajax({
            url: '/send_request',
            method: 'post',             
            contentType: "application/json; charset=utf-8",  
            data: JSON.stringify(
            {
                name: name,
                phone: phone,
                email: email,
                question: question
            }),
            success: function(data){   
                document.getElementById('request_status').innerHTML = "Скоро мы свяжемся с вами для ответа на Ваш вопрос."
                
            }
        });

    }
}