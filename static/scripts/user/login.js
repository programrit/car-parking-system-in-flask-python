// user login 
$(document).ready(function(){
    $('.load').hide();
    $('.captcha').prop('disabled',true);
    $('.login').click(function(e){
        e.preventDefault();
        var email = $('.email').val();
        var password = $('.password').val();
        var validate_email = /^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$/;
        var placeholder = document.getElementById('floatingCaptcha').placeholder;
        var captcha_value =$('.captcha_value').val();
        const csrf_token = $('#csrf_token').val();
        if(email == "" || email ==null){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter your email address");
        }else if(!validate_email.test(email)){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter valid email address");
        }else if(password==""|| password==null){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter your password");
        }else if(captcha_value == null || captcha_value==""){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter captcha");
        }else if(captcha_value != placeholder){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Invalid Captcha");
        }else if(csrf_token == "" || csrf_token ==null){
            alertify.set("notifier", "position", "top-right");
            alertify.error("Invalid csrf token");
        }else{
            $(".load").show();
            $(".gradient-custom").hide();
            $(".show_load").css({
              background: "black",
            });
            $.ajax({
                type:"POST",
                url:"user-login",
                headers:{
                    "X-CSRFToken":csrf_token
                },data:{
                    email:email,
                    password:password,
                },success:function(data){
                    if(data=="login"){
                        $('.load').hide();
                        $('.gradient-custom').show();
                        alertify.set('notifier', 'position', 'top-right');
                        alertify.success("Login Successfully");
                        setTimeout(function () {
                            window.location.href = "/"
                        }, 1000);
                    }else if (data =="not verify"){
                        $('.load').hide();
                        $('.gradient-custom').show();
                        setTimeout(function () {
                            window.location.href = "user-signup/email-verification"
                        }, 1000);
                        alertify.set('notifier', 'position', 'top-right');
                        alertify.error("Email not verify! OTP send your email");
                    }else if (data =="not send email"){
                        $('.load').hide();
                        $('.gradient-custom').show();
                        setTimeout(function () {
                            window.location.href = "user-signup/email-verification"
                        }, 1000);
                        alertify.set('notifier', 'position', 'top-right');
                        alertify.error("Email not verify! OTP send failed. Please click resend OTP");

                    }else{
                        $('.load').hide();
                        $('.gradient-custom').show();
                        alertify.set('notifier', 'position', 'top-right');
                        alertify.error(data);
                    }
                },error:function(error){
                    $('.load').hide();
                    $('.gradient-custom').show();
                    alertify.set('notifier', 'position', 'top-right');
                    alertify.error("Something went wrong. Please try again later");
                }
            });
        }
    });
    // login page refresh captcha button
    $(".refresh").click(function(e){
        e.preventDefault();
        const csrf_token = $('#csrf_token').val();
        if(csrf_token == "" || csrf_token ==null){
            alertify.set("notifier", "position", "top-right");
            alertify.error("Invalid csrf token");
        }else{
            $.ajax({
                type:"POST",
                    url:"user-login",
                    headers:{
                        "X-CSRFToken":csrf_token
                    },data:{
                        refresh:true
                    },success:function(data){
                        if(data=="something went wrong"){
                            alertify.set('notifier', 'position', 'top-right');
                            alertify.error(data);
                        }else{
                           $('.captcha').attr('placeholder',data);
                        }
                    }
            });
        }
        
    });
});

$(window).on('load',function(e){
    e.preventDefault();
    $('.load').show();
    $('.gradient-custom').hide();
    $('.show_load').css({
        background:"black"
    });
    $('.load').hide();
    $('.gradient-custom').show();
});