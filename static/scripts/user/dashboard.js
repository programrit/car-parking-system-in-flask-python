// about page read more button
function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
  }
}

$(document).ready(function(){
  new DataTable('#example', {
    responsive: true
  });
});

// card expiryDate select
$(document).ready(function () {
  $("#expiryDate").datepicker({
    dateFormat: "mm/yy",
    changeMonth: true,
    changeYear: true,
    startView: "months",
    showButtonPanel: true,
    minViewMode: "months",
    minDate: 0,
    autoSize: true,
    onClose: function (dateText, inst) {
      $(this).datepicker(
        "setDate",
        new Date(inst.selectedYear, inst.selectedMonth, 1)
      );
    },
  });
});

// captcha from contact page
$(document).ready(function () {
  $(".load").hide();
  $(".captcha").prop("disabled", true);
  $(".refresh").click(function (e) {
    e.preventDefault();
    $.ajax({
      type: "POST",
      url: "/",
      data: {
        refresh: true,
      },
      success: function (data) {
        if (data == "something went wrong") {
          alertify.set("notifier", "position", "top-right");
          alertify.error(data);
        } else {
          $(".captcha").attr("placeholder", data);
        }
      },
    });
  });
});

// contact data upload database
$(document).ready(function () {
  $(".submit_contact").click(function (e) {
    e.preventDefault();
    const contact_name = $(".contact_name").val();
    const contact_email = $(".contact_email").val();
    const contact_phone = $(".contact_phone").val();
    const contact_message = $("textarea#contact_message").val();
    const valid_name = /^[a-zA-Z]+$/;
    const validate_email = /^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$/;
    const validate_phone = /^[6-9]\d{9}$/;
    const placeholder = document.getElementById("floatingCaptcha").placeholder;
    const captcha_value = $(".captcha_value").val();
    const max_length = 250;
    if (contact_name == "" || contact_name == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your name");
    } else if (contact_name.length <= 2) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your full name without space");
    } else if (!valid_name.test(contact_name)) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter valid name");
    } else if (contact_email == "" || contact_email == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your email address");
    } else if (!validate_email.test(contact_email)) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter valid email address");
    } else if (contact_phone == "" || contact_phone == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your phone no");
    } else if (!validate_phone.test(contact_phone)) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter valid phone no");
    } else if (contact_message == "" || contact_message == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your message");
    } else if (contact_message.length < 20) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your message. Atleast 20 characters");
    } else if (contact_message.length > max_length) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Only allowed 250 characters");
    } else if (captcha_value == null || captcha_value == "") {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter captcha");
    } else if (captcha_value != placeholder) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Invalid Captcha");
    } else {
      $(".load").show();
      $(".gradient-custom").hide();
      $(".submit_contact").prop("disabled", true);
      $(".reset_contact").prop("disabled", true);
      $.ajax({
        type: "POST",
        url: "/",
        data: {
          contact_name: contact_name,
          contact_email: contact_email,
          contact_phone: contact_phone,
          contact_message: contact_message,
        },
        success: function (data) {
          if (data == "success") {
            $(":input").val("");
            $(".submit_contact").prop("disabled", false);
            $(".reset_contact").prop("disabled", false);
            $(".load").hide();
            $(".gradient-custom").show();
            alertify.set("notifier", "position", "top-right");
            alertify.success("Thank you for getting in touch with me");
          } else {
            $(":input").val("");
            $(".submit_contact").prop("disabled", false);
            $(".reset_contact").prop("disabled", false);
            $(".load").hide();
            $(".gradient-custom").show();
            alertify.set("notifier", "position", "top-right");
            alertify.error(data);
          }
        },
        error: function (error) {
          $(":input").val("");
          $(".submit_contact").prop("disabled", false);
          $(".reset_contact").prop("disabled", false);
          $(".load").hide();
          $(".gradient-custom").show();
          alertify.set("notifier", "position", "top-right");
          alertify.error("Something went wrong. Please try again later");
        },
      });
    }
  });
});


// page redirect like about, contact,home detail
$(document).ready(function () {
  $(".about_us").click(function (e) {
    e.preventDefault();
    $(".about").show();
    $(".home").hide();
    $(".parking").hide();
    $(".contact").hide();
    $("#nav1").removeClass("text-white");
    $("#nav2").removeClass("text-white");
    $("#nav3").removeClass("text-white");
    $("#nav4").removeClass("text-white");
    $("#nav5").removeClass("text-white");
    $("#nav6").removeClass("text-white");
    $(".fixed-top").removeClass("bg-transparent");
  });
  $(".booking_slot").click(function (e) {
    e.preventDefault();
    $(".parking").show();
    $(".home").hide();
    $(".about").hide();
    $(".contact").hide();
    $("#nav1").removeClass("text-white");
    $("#nav2").removeClass("text-white");
    $("#nav3").removeClass("text-white");
    $("#nav4").removeClass("text-white");
    $("#nav5").removeClass("text-white");
    $("#nav6").removeClass("text-white");
    $(".fixed-top").removeClass("bg-transparent");
  });
  $(".contact_us").click(function (e) {
    e.preventDefault();
    $(".parking").hide();
    $(".contact").show();
    $(".home").hide();
    $(".about").hide();
    $("#nav1").removeClass("text-white");
    $("#nav2").removeClass("text-white");
    $("#nav3").removeClass("text-white");
    $("#nav4").removeClass("text-white");
    $("#nav5").removeClass("text-white");
    $("#nav6").removeClass("text-white");
    $(".fixed-top").removeClass("bg-transparent");
  });
});


// slot booking select date for form and to and booking also
$(document).ready(function () {
  $("#from").attr("readonly", true);
  $("#to").attr("readonly", true);
  $(".day").attr("readonly", true);
  $(".amount").attr("readonly", true);
  $("#from").datepicker({
    dateFormat: "yy-mm-dd",
    changeMonth: true,
    changeYear: true,
    minDate: 0,
    autoSize: true,
  });
  $("#to").datepicker({
    dateFormat: "yy-mm-dd",
    changeMonth: true,
    changeYear: true,
    minDate: 0,
    autoSize: true,
  });
  var total;
  $(".confirm").click(function (e) {
    e.preventDefault();
    const from = $(".from").val();
    const to = $(".to").val();
    if (from == null || from == "") {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please select from date");
    } else if (to == null || to == "") {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please select to date");
    } else {
      const from_date = new Date(from);
      const to_date = new Date(to);
      const time = to_date - from_date;
      const days = Math.ceil(time / (1000 * 60 * 60 * 24));
      if (days < 0) {
        alertify.set("notifier", "position", "top-right");
        alertify.error("From date is greater than to date");
      } else if (days > 5) {
        alertify.set("notifier", "position", "top-right");
        alertify.error(
          "Your slot booking for only 5 days. You are booking in " +
            days +
            " days"
        );
      } else if (days == 0) {
        alertify.set("notifier", "position", "top-right");
        alertify.error("Booking slot atleast one day");
      } else {
        $(".day").attr("placeholder", days);
        total = parseInt(days);
        $(".amount").attr("placeholder", "₹ " + days * 50);
      }
    }
  });
  $(".booking").click(function (e) {
    e.preventDefault();
    const from = $(".from").val();
    const to = $(".to").val();
    if (total === undefined) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please book a slot and click confirm button");
    } else if (from == "" || from == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please select from date");
    } else if (to == "" || to == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please select to date");
    } else {
      $(".stripe").modal("show");
      $(".pay").click(function (e) {
        e.preventDefault();
        const cardNumber = $("#cardNumber").val();
        const expiryDate = $("#expiryDate").val();
        const cvv = $("#cvv").val();
        $("#expiryDate").prop("readonly",true);
        if (cardNumber == "" || cardNumber == null) {
          alertify.set("notifier", "position", "top-right");
          alertify.error("Please enter your card number");
        } else if(cardNumber.length > 13){
          alertify.set("notifier", "position", "top-right");
          alertify.error("Please enter valid card number");
        }else if(expiryDate == '' || expiryDate ==null){
          alertify.set("notifier", "position", "top-right");
          alertify.error("Please enter select expired date");
        }else if(cvv == '' || cvv ==null){
          alertify.set("notifier", "position", "top-right");
          alertify.error("Please enter your cvv number");
        }else if(cvv.length > 3){
          alertify.set("notifier", "position", "top-right");
          alertify.error("Please enter valid cvv number");
        }else {
          $(".load").show();
          $(".gradient-custom").hide();
          $(".booking").prop("disabled", true);
          $(".cancel_booking").prop("disabled", true);
          $(".pay").prop("disabled", true);
          $(".cancel_pay").prop("disabled", true);
          const total_days = total;
          const amount = total_days * 50;
          $.ajax({
            type: "POST",
            url: "/",
            data: {
              from: from,
              to: to,
              total_days: total_days,
              amount: amount,
            },
            success: function (data) {
              if (data == "booking") {
                $(".booking").prop("disabled", false);
                $(".cancel_booking").prop("disabled", false);
                $(".pay").prop("disabled", false);
                $(".cancel_pay").prop("disabled", false);
                $(".load").hide();
                $(".gradient-custom").show();
                alertify.set("notifier", "position", "top-right");
                alertify.success("Slot booking successfully");
                setTimeout(function () {
                  window.location.href = "/";
                }, 1000);
              } else {
                $(".booking").prop("disabled", false);
                $(".cancel_booking").prop("disabled", false);
                $(".pay").prop("disabled", false);
                $(".cancel_pay").prop("disabled", false);
                $(".load").hide();
                $(".gradient-custom").show();
                $(":input").val("");
                alertify.set("notifier", "position", "top-right");
                alertify.error(data);
                setTimeout(function () {
                  window.location.href = "/";
                }, 1000);
              }
            },
            error: function (error) {
              $(".booking").prop("disabled", false);
              $(".cancel_booking").prop("disabled", false);
              $(".pay").prop("disabled", false);
              $(".cancel_pay").prop("disabled", false);
              $(".load").hide();
              $(".gradient-custom").show();
              $(":input").val("");
              alertify.set("notifier", "position", "top-right");
              alertify.error("Something went wrong. Please try again later");
              setTimeout(function () {
                window.location.href = "/";
              }, 1000);
            },
          });
        }
      });
    }
  });
});



// update user data from modal
$(document).ready(function () {
  $(".close").click(function () {
    $("#form")[0].reset();
  });
  $(".update").click(function (e) {
    e.preventDefault();
    const name = $(".name").val();
    const email = $(".email").val();
    const phone = $(".phone").val();
    const valid_name = /^[a-zA-Z]+$/;
    const validate_email = /^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$/;
    const validate_phone = /^[6-9]\d{9}$/;
    const user_profile = document.getElementById("profile");
    const count_image = user_profile.files.length;
    if (name == "" || name == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your name");
    } else if (name.length <= 2) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your full name without space");
    } else if (!valid_name.test(name)) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter valid name");
    } else if (email == "" || email == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your email address");
    } else if (!validate_email.test(email)) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter valid email address");
    } else if (phone == "" || phone == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your phone no");
    } else if (!validate_phone.test(phone)) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter valid phone no");
    } else if (count_image > 1 && count_image < 0) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Image allowed only one!");
    } else {
      $(".update").prop("disabled", true);
      $(".reset").prop("disabled", true);
      $(".load").show();
      $(".gradient-custom").hide();
      if (count_image == 1) {
        const formData = new FormData();
        formData.append("name", name);
        formData.append("email", email);
        formData.append("phone", phone);
        formData.append("profile", user_profile.files[0]);
        $.ajax({
          type: "POST",
          url: "/",
          data: formData,
          contentType: false,
          processData: false,
          success: function (data) {
            if (data == "update successfully") {
              $(".update").prop("disabled", false);
              $(".reset").prop("disabled", false);
              $(".load").hide();
              $(".gradient-custom").show();
              alertify.set("notifier", "position", "top-right");
              alertify.success("Update Successfully");
              setTimeout(function () {
                window.location.href = "/";
              }, 1000);
            } else {
              $(".update").prop("disabled", false);
              $(".reset").prop("disabled", false);
              $(".load").hide();
              $(".gradient-custom").show();
              alertify.set("notifier", "position", "top-right");
              alertify.error(data);
            }
          },
          error: function (error) {
            $(".update").prop("disabled", false);
            $(".reset").prop("disabled", false);
            $(".load").hide();
            $(".gradient-custom").show();
            alertify.set("notifier", "position", "top-right");
            alertify.error("Something went wrong. Please try agin later");
          },
        });
      } else {
        const formData = new FormData();
        formData.append("name", name);
        formData.append("email", email);
        formData.append("phone", phone);
        $.ajax({
          type: "POST",
          url: "/",
          data: formData,
          contentType: false,
          processData: false,
          success: function (data) {
            if (data == "update successfully") {
              $(".update").prop("disabled", false);
              $(".reset").prop("disabled", false);
              $(".load").hide();
              $(".gradient-custom").show();
              alertify.set("notifier", "position", "top-right");
              alertify.success("Update Successfully");
              setTimeout(function () {
                window.location.href = "/";
              }, 1000);
            } else {
              $(".update").prop("disabled", false);
              $(".reset").prop("disabled", false);
              $(".load").hide();
              $(".gradient-custom").show();
              alertify.set("notifier", "position", "top-right");
              alertify.error(data);
            }
          },
          error: function (error) {
            $(".update").prop("disabled", false);
            $(".reset").prop("disabled", false);
            $(".load").hide();
            $(".gradient-custom").show();
            alertify.set("notifier", "position", "top-right");
            alertify.error("Something went wrong. Please try agin later");
          },
        });
      }
    }
  });
});


// remove booking slot

$(document).ready(function(){
  $('.delete_slot').click(function(e){
    e.preventDefault();
    id = $(this).val();
    if(id == null || id == ""){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Invalid data");
    }else{
      Swal.fire({
        title: 'Are you sure You want to delete the slot?',
        text: 'Once deleted you cannot recover the slot!',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Yes',
        cancelButtonText: 'No',
        reverseButtons: true,
        allowOutsideClick: false,
      }).then((result) => {
        if (result.isConfirmed) {
          // User clicked "Yes, delete it!"
          // Perform the delete operation here
          $.ajax({
            type: 'POST',
            url:'/',
            data: {
              id:id,
            },success:function(response){
              if (response == "delete"){
                swal.fire({
                  allowOutsideClick: false,
                  title: "Deleted",
                  text: "Your slot has been deleted.",
                  icon: "success"
                });
                $("#example").load(location.href + " #example");
              }else{
                swal.fire({
                  allowOutsideClick: false,
                  title: "Deleted",
                  text: response,
                  icon: "error"
                });
              }
            },error:function(error){
              swal.fire({
                allowOutsideClick: false,
                title: "Deleted",
                text: "Something Went Wrong. Please try again later",
                icon: "error"
              });
            }
          });
        } else if (result.dismiss === Swal.DismissReason.cancel) {
          // User clicked "No, cancel!"
          swal.fire({
            allowOutsideClick: false,
            title: "Cancelled",
            text: "Your slot is safe.",
            icon: "error"
          });
        }
      });
    }
    
  });
});



// update password

$(document).ready(function(){
  $('.upadte_password').click(function(e){
    e.preventDefault();
    const validate_password = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{7,}$/;
    const old_password = $('.old_password').val();
    const new_password = $('.new_password').val();
    const confirm_password = $('.confirm_password').val();
    if(old_password == "" || old_password == null){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your old password");
    }else if(new_password == "" || new_password ==null){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your new password");
    }else if(!validate_password.test(new_password)){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter strong password");
    }else if(new_password == old_password){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Old password and new password is same. Please use different password");
    }else if(new_password != confirm_password){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Password not match");
    }else{
      $('.upadte_password').prop("disabled",true);
      $('.cancel_password').prop("disabled",true);
      $.ajax({
        type: 'POST',
        url: '/',
        data: {
          old_password:old_password,
          new_password:new_password,
          confirm_password:confirm_password,
        },success:function(data){
          if(data == "update"){
            $('.upadte_password').prop("disabled",false);
            $('.cancel_password').prop("disabled",false);
            alertify.set("notifier", "position", "top-right");
            alertify.success("Password update successfully");
            setTimeout(function () {
              window.location.href = "/"
            }, 1000);
          }else{
            $('.upadte_password').prop("disabled",false);
            $('.cancel_password').prop("disabled",false);
            alertify.set("notifier", "position", "top-right");
            alertify.error(data);
          }
        },error:function(error){
          $('.upadte_password').prop("disabled",false);
          $('.cancel_password').prop("disabled",false);
          alertify.set("notifier", "position", "top-right");
          alertify.error("Something went wrong. Please try agin later");
        } 
      });
    }
  });
});


// logout

$(document).ready(function(){
  $('.logout').click(function(){
    const logout = true;
    $.ajax({
      type: 'POST',
      url :'/',
      data:{
        logout:logout
      },success:function(data){
        if(data == "logout"){
          alertify.set("notifier", "position", "top-right");
          alertify.success("Logout Successfully :)");
          setTimeout(function () {
            window.location.href = "/user-login"
          }, 1000);
        }else{
          alertify.set("notifier", "position", "top-right");
          alertify.error("Something went wrong. Please try agin later");
        }
      },error:function(error){
        alertify.set("notifier", "position", "top-right");
        alertify.error("Something went wrong. Please try agin later");
      }
    });
  });
});



// print invoice

$(document).ready(function(){
  $('.pdf').click(function(e){
    e.preventDefault();
    const value = $(this).val();
    $.ajax({
      type:'POST',
      url: '/',
      data: {
        value:value
      },success:function(data){
        if(data == "print"){
          window.open("/print",'_blank');
        }else{
          alertify.set("notifier", "position", "top-right");
          alertify.error(data);
        }
      },error:function(error){
        alertify.set("notifier", "position", "top-right");
        alertify.error("Something went wrong. Please try again later");
      }
    });
  });
});

