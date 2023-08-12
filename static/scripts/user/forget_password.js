// forget password to get email and send otp from user (user-login/forget-password)
$(document).ready(function () {
  $(".load").hide();
  $(".forget").click(function (e) {
    e.preventDefault();
    const email = $(".email").val();
    const validate_email = /^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$/;
    if (email == "" || email == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your email");
    } else if (!validate_email.test(email)) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter valid email");
    } else {
      $(".forget").prop("disabled", true);
      $(".load").show();
      $(".gradient-custom").hide();
      $(".show_load").css({
        background: "black",
      });
      $.ajax({
        type: "POST",
        url: "forget-password",
        data: {
          email: email,
        },
        success: function (data) {
          if (data == "send") {
            $(".load").hide();
            $(".gradient-custom").show();
            $(".forget").prop("disabled", false);
            alertify.set("notifier", "position", "top-right");
            alertify.success("OTP send successfully. Please check your email");
            setTimeout(function () {
              window.location.href = "/user-login/email-verification";
            }, 1000);
          } else {
            $(".load").hide();
            $(".gradient-custom").show();
            $(".forget").prop("disabled", false);
            alertify.set("notifier", "position", "top-right");
            alertify.error(data);
          }
        },
        error: function (error) {
          $(".load").hide();
          $(".gradient-custom").show();
          $(".forget").prop("disabled", false);
          alertify.set("notifier", "position", "top-right");
          alertify.error("Something went wrong. Please try again later");
        },
      });
    }
  });
});

// after send otp. otp verfication 
$(document).ready(function () {
  $(".load").hide();
  $(".enter").click(function (e) {
    e.preventDefault();
    const email_otp = $(".email_otp").val();
    if (email_otp == "" || email_otp == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your OTP");
    } else if (isNaN(email_otp)) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter valid OTP");
    } else {
      $(".load").show();
      $(".gradient-custom").hide();
      $(".show_load").css({
        background: "black",
      });
      $.ajax({
        type: "POST",
        url: "email-verification",
        data: { email_otp: email_otp },
        success: function (data) {
          if (data == "OTP verfication successfully") {
            $(".load").hide();
            $(".gradient-custom").show();
            alertify.set("notifier", "position", "top-right");
            alertify.success("OTP verification successfully");
            setTimeout(function () {
              window.location.href = "/user-login/change-password";
            }, 1000);
          } else if (data == "incorrect otp") {
            $(".load").hide();
            $(".gradient-custom").show();
            alertify.set("notifier", "position", "top-right");
            alertify.error("Incorrect OTP");
          } else if (data == "otp expired") {
            $(".load").hide();
            $(".gradient-custom").show();
            alertify.set("notifier", "position", "top-right");
            alertify.error("Your OTP is expired. Please click resend OTP");
          } else if (data == "otp verify failed") {
            $(".load").hide();
            $(".gradient-custom").show();
            alertify.set("notifier", "position", "top-right");
            alertify.error("OTP verification failed. Please click resend OTP");
          } else if (data == "alerady verify") {
            $(".load").hide();
            $(".gradient-custom").show();
            alertify.set("notifier", "position", "top-right");
            alertify.error("Your Account is already verified. Please login");
            setTimeout(function () {
              window.location.href = "/user-login";
            }, 1000);
          } else {
            $(".load").hide();
            $(".gradient-custom").show();
            alertify.set("notifier", "position", "top-right");
            alertify.error("Something went wrong.");
          }
        },
        error: function (error) {
          $(".load").hide();
          $(".gradient-custom").show();
          alertify.set("notifier", "position", "top-right");
          alertify.error("Something went wrong. Please try again later");
        },
      });
    }
  });

// resend otp for forget password 

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
      type: "POST",
      url: "email-verification",
      data: { resend_otp_email: true },
      success: function (data) {
        if (data == "otp send") {
          $(".load").hide();
          $(".gradient-custom").show();
          alertify.set("notifier", "position", "top-right");
          alertify.success("OTP send successfully! please check your email");
          setTimeout(function () {
            window.location.href = "email-verification";
          }, 1000);
        } else if (data == "otp not send") {
          $(".load").hide();
          $(".gradient-custom").show();
          alertify.set("notifier", "position", "top-right");
          alertify.error(
            "OTP send failed! Please check your internet connection"
          );
        } else {
          $(".load").hide();
          $(".gradient-custom").show();
          alertify.set("notifier", "position", "top-right");
          alertify.error("Something went wrong. Please try again later");
        }
      },
      error: function (error) {
        $(".load").hide();
        $(".gradient-custom").show();
        alertify.set("notifier", "position", "top-right");
        alertify.error("Something went wrong. Please try again later");
      },
    });
  });

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


// change password

$(document).ready(function(){
  $('.change_password').click(function(e){
    e.preventDefault();
    const new_password = $('.new_password').val();
    const confirm_password = $('.confirm_password').val();
    const validate_password = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{7,}$/;
    if (new_password == "" || new_password == null){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your new password");
    }else if (!validate_password.test(new_password)){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter strong password");
    }else if (confirm_password == "" || confirm_password == null){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your confirm password");
    }else if (new_password != confirm_password){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Password not match");
    }else{
      $(".load").show();
      $(".gradient-custom").hide();
      $(".show_load").css({
        background: "black",
      });
      $.ajax({
        type: 'POST',
        ur: 'change-password',
        data:{
          new_password : new_password,
          confirm_password: confirm_password,
        },success:function(data){
          if(data == "update"){
            $(".load").hide();
            $(".gradient-custom").show();
            alertify.set("notifier", "position", "top-right");
            alertify.success("Password update successfully");
            setTimeout(function () {
              window.location.href = "/user-login"
            }, 1000);
          }else{
            $(".load").hide();
            $(".gradient-custom").show();
            alertify.set("notifier", "position", "top-right");
            alertify.error(data);
          }
        },error:function(error){
          $(".load").hide();
          $(".gradient-custom").show();
          alertify.set("notifier", "position", "top-right");
          alertify.error("Something went wrong. Please try again later");
        }
      });
    }
  });
});


// resend otp timer from 60s
if (localStorage.getItem("count_timer")) {
  var count_timer = localStorage.getItem("count_timer");
} else {
  var count_timer = 60 * 1;
}
var minutes = parseInt(count_timer / 60);
var seconds = parseInt(count_timer % 60);
function countDownTimer() {
  if (seconds < 10) {
    seconds = "0" + seconds;
  }
  if (minutes < 10) {
    minutes = "0" + minutes;
  }

  document.getElementById("timer").innerHTML =
    "Resend OTP is " + minutes + ":" + seconds + " Seconds";
  if (count_timer <= 0) {
    localStorage.clear("count_timer");
    $("#timer").hide();
    $(".resend_otp_email").css("display", "block");
    $(".resend_otp_phone").css("display", "block");
  } else {
    count_timer = count_timer - 1;
    minutes = parseInt(count_timer / 60);
    seconds = parseInt(count_timer % 60);
    localStorage.setItem("count_timer", count_timer);
    setTimeout("countDownTimer()", 1000);
  }
}
setTimeout("countDownTimer()", 1000);
