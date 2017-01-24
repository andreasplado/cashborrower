$(document).ready(function(){

        toastr.options = {
        "closeButton": true,
        "debug": false,
        "newestOnTop": false,
        "progressBar": false,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "400",
        "timeOut": "1000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    }


    $("p").click(function(){
        $(this).hide();
    });

    $("#btn_login").click(function(){
        usernameTxt = $('#txt_username').val();
        passwordTxt = $('#pw_password').val();
        if(usernameTxt == ""){
            toastr["error"]("Please enter your username!");
        }
        if(passwordTxt == ""){
            toastr["error"]("Please enter your password!");
        }
        if(usernameTxt != "" && passwordTxt !=""){
            data =  JSON.stringify({username : usernameTxt, password : passwordTxt })
            $.ajax({
                type: "POST",
                url: "/api-token-auth/",
                data: data,
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (msg) {
                    toastr["success"]("You logged in successfully!");
                   //do something

                   $(location).attr('href', '/dashboard')
                },
                error: function (errormessage) {
                    console.log(errormessage)
                    toastr["error"]("Provided credentials are wrong!");

                }
            });
        }
    });


});