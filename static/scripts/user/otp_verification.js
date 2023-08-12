
// otp verification from new user
$(document).ready(function () {
  $(".load").hide();
  $(".enter").click(function (e) {
    e.preventDefault();
    const email_otp =$('.email_otp').val();
    if(email_otp == "" || email_otp == null){
      alertify.set('notifier', 'position', 'top-right');
      alertify.error("Please enter your OTP");
    }else if(isNaN(email_otp)){
      alertify.set('notifier', 'position', 'top-right');
      alertify.error("Please enter valid OTP");
    }else{
      $(".load").show();
      $(".gradient-custom").hide();
      $(".show_load").css({
        background: "black",
      });
      $.ajax({
        type:"POST",
        url:"email-verification",
        data: {email_otp : email_otp},
        success:function(data){
          if(data == "signup successfully"){
            $('.load').hide();
            $('.gradient-custom').show();
            alertify.set('notifier', 'position', 'top-right');
            alertify.success("Signup Successfully. Please login :)");
            setTimeout(function () {
                window.location.href = "/user-login"
            }, 1000);
          }else if (data == "incorrect otp"){
            $('.load').hide();
            $('.gradient-custom').show();
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Incorrect OTP");
          }else if (data == "otp expired"){
            $('.load').hide();
            $('.gradient-custom').show();
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Your OTP is expired. Please click resend OTP");
          }else if (data == "otp verify failed"){
            $('.load').hide();
            $('.gradient-custom').show();
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("OTP verification failed. Please click resend OTP");
          }else if (data == "alerady verify"){
            $('.load').hide();
            $('.gradient-custom').show();
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Your Account is already verified. Please login");
            setTimeout(function () {
              window.location.href = "/user-login"
            }, 1000);
          }else{
            $('.load').hide();
            $('.gradient-custom').show();
            alertify.set('notifier', 'position', 'top-right');
            alertify.error("Something went wrong.");
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

// resend otp from new user
  $(".resend_otp_email").click(function (e) {
    e.preventDefault();
    $(".load").show();
    $(".gradient-custom").hide();
    $(".show_load").css({
      background: "black",
    });
    // $(".load").hide();
    // $(".gradient-custom").show();
    $.ajax({
        type:"POST",
        url:"email-phone-verification",
        data: {resend_otp_email:true},
        success:function(data){
            if(data=="otp send"){
                $('.load').hide();
                $('.gradient-custom').show();
                alertify.set('notifier', 'position', 'top-right');
                alertify.success("OTP send successfully! please check your email");
                setTimeout(function () {
                    window.location.href = "email-phone-verification"
                }, 1000);
            }else if (data == "otp not send"){
                $('.load').hide();
                $('.gradient-custom').show();
                alertify.set('notifier', 'position', 'top-right');
                alertify.error("OTP send failed! Please check your internet connection");
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
  });
  // $(".resend_otp_phone").click(function (e) {
  //   e.preventDefault();
  //   $(".load").hide();
  //   e.preventDefault();
  //   $(".load").show();
  //   $(".gradient-custom").hide();
  //   $(".show_load").css({
  //     background: "black",
  //   });
  //   // $(".load").hide();
  //   // $(".gradient-custom").show();
  //   $.ajax({
  //       type:"POST",
  //       url:"email-phone-verification",
  //       data: {resend_otp_phone:true},
  //       success:function(data){
  //           if(data=="otp send"){
  //               $('.load').hide();
  //               $('.gradient-custom').show();
  //               alertify.set('notifier', 'position', 'top-right');
  //               alertify.success("OTP send successfully! please check your phone no");
  //               setTimeout(function () {
  //                   window.location.href = "user-signup/email-phone-verification"
  //               }, 1000);
  //           }else{
  //               $('.load').hide();
  //               $('.gradient-custom').show();
  //               alertify.set('notifier', 'position', 'top-right');
  //               alertify.error("OTP send failed! Please check your internet connection");
  //           }
  //       },error:function(error){
  //           $('.load').hide();
  //           $('.gradient-custom').show();
  //           alertify.set('notifier', 'position', 'top-right');
  //           alertify.error("Something went wrong. Please try again later");
  //       }
  //   });
  // });


  $(window).on("load", function (e) {
    e.preventDefault();
    $(".load").show();
    $(".gradient-custom").hide();
    $(".show_load").css({
      background: "black",
    });
    $(".load").hide();
    $(".gradient-custom").show();
  });

});

// resend timer from new user
if(localStorage.getItem("count_timer")){
    var count_timer = localStorage.getItem("count_timer");
} else {
    var count_timer = 60*1;
}
var minutes = parseInt(count_timer/60);
var seconds = parseInt(count_timer%60);
function countDownTimer(){
    if(seconds < 10){
        seconds= "0"+ seconds ;
    }if(minutes < 10){
        minutes= "0"+ minutes ;
    }
    
    document.getElementById("timer").innerHTML = "Resend OTP is "+minutes+":"+seconds+" Seconds";
    if(count_timer <= 0){
        localStorage.clear("count_timer");
        $('#timer').hide();
        $('.resend_otp_email').css('display','block');
        $('.resend_otp_phone').css('display','block');
    } else {
        count_timer = count_timer -1 ;
        minutes = parseInt(count_timer/60);
        seconds = parseInt(count_timer%60);
        localStorage.setItem("count_timer",count_timer);
        setTimeout("countDownTimer()",1000);
    }
}
setTimeout("countDownTimer()",1000);
