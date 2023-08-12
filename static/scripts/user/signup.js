// user signup data 

$(document).ready(function(){
    $('.signup').click(function(e){
        e.preventDefault();
        var name = $('.name').val();
        var email = $('.email').val();
        var phone = $('.phone').val();
        var password = $('.password').val();
        var confirm_password = $('.confirm_password').val();
        const valid_name =/^[a-zA-Z]+$/
        const validate_email = /^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$/;
        const validate_phone =/^[6-9]\d{9}$/;
        const validate_password = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{7,}$/;
        if(name == "" || name ==null){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter your name");
        }else if(name.length <=2){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter your full name without space");
        }else if(!valid_name.test(name)){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter valid name");
        }else if(email == "" || email ==null){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter your email address");
        }else if(!validate_email.test(email)){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter valid email address");
        }else if(phone==""|| phone==null){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter your phone no");
        }else if(!validate_phone.test(phone)){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter valid phone no");
        }else if(password==""|| password==null){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter your password");
        }else if(!password.match(validate_password)){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter your strong password");
        }else if(confirm_password==""|| confirm_password==null){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Please enter your confirm password");
        }else if(password != confirm_password){
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Password not match");
        }else{
            $('.load').show();
            $('.gradient-custom').hide();
            $('.show_load').css({
            background:"black"
        });
            $.ajax({
                type:"POST",
                url:"user-signup",
                data:{
                    name:name,
                    email:email,
                    phone:phone,
                    password:password,
                    confirm_password:confirm_password
                },success:function(data){
                    if(data=="otp send"){
                        $('.load').hide();
                        $('.gradient-custom').show();
                        alertify.set('notifier', 'position', 'top-right');
                        alertify.success("OTP send successfully! please check your email");
                        setTimeout(function () {
                            window.location.href = "user-signup/email-verification"
                        }, 1000);
                    }else if (data == "not send email"){
                        $('.load').hide();
                        $('.gradient-custom').show();
                        alertify.set('notifier', 'position', 'top-right');
                        alertify.error("OTP send failed from email!");
                    }else if(data == "email exist"){
                        $('.load').hide();
                        $('.gradient-custom').show();
                        alertify.set('notifier', 'position', 'top-right');
                        alertify.error("Email already exist. Please login or use different email");
                    }else if(data == "phone exist"){
                        $('.load').hide();
                        $('.gradient-custom').show();
                        alertify.set('notifier', 'position', 'top-right');
                        alertify.error("Phone no already exist. Please use different phone no");
                    }else{
                        $('.load').hide();
                        $('.gradient-custom').show();
                        alertify.set('notifier', 'position', 'top-right');
                        alertify.error("Something went wrong. Please try again later");
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
    $(window).on('load',function(){
        $('.load').show();
        $('.gradient-custom').hide();
        $('.show_load').css({
            background:"black"
        });
        $('.load').hide();
        $('.gradient-custom').show();
    });

});

