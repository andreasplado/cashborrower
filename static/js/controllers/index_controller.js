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
        "timeOut": "5000",
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
        var usernameTxt = $('#username').val();
        var passwordTxt = $('#password').val();
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
                    var lol =JSON.stringify(msg);
                    window.localStorage.setItem('token', lol);
                    window.localStorage.setItem('username', usernameTxt);
                    console.log(msg);
                    toastr["success"]("You logged in successfully!");
                   //do something
                   //$(location).attr('href', '/dashboard')
                   //$(location).attr('href', '/dashboard')
                },
                error: function (errormessage) {
                    toastr["error"]("Provided credentials are wrong!");

                }
            });
        }
    });

    $("#btn_register").click(function(){
        var registerUsernameTxt = $('#register_username').val();
        var registerEmailTxt = $('#register_email').val();
        var registerPasswordTxt = $('#register_password').val();
        var registerRepeatPasswordTxt = $('#register_repeat_password').val();

        if(registerUsernameTxt == ""){
            toastr["error"]("Please enter your username that you want to register!");
        }
        if(registerEmailTxt == ""){
            toastr["error"]("Please enter your email that you want to register!");
        }
        if(registerPasswordTxt == ""){
            toastr["error"]("Please enter your password!");
        }
        if(registerRepeatPasswordTxt == ""){
            toastr["error"]("Please repeat your chosen password!");
        }
        if(registerPasswordTxt != registerRepeatPasswordTxt && registerPasswordTxt != ""  && registerRepeatPasswordTxt != ""){
            toastr["error"]("Your passwords do not match!");
        }
        if(registerUsernameTxt!= "" && registerPasswordTxt !=""){
            data =  JSON.stringify({username : registerUsernameTxt, email: registerEmailTxt, password : registerPasswordTxt })
            $.ajax({
                type: "POST",
                url: "/signup/",
                data: data,
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (msg) {
                    toastr["success"]("User registred successfully!");
                   //do something
                   //$(location).attr('href', '/dashboard')
                },
                error: function (errormessage) {
                    toastr["error"]("Error: " + errormessage);
                    console.log(errormessage);
                }
            });
        }
    });
});
