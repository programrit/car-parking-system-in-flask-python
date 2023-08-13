$(document).ready(function () {
  $(".load").hide();
});

$(document).ready(function () {
  new DataTable("#example", {
    responsive: true,
  });
});

$(".sidebar ul li").on("click", function () {
  $(".sidebar ul li.active").removeClass("active");
  $(this).addClass("active");
});

$(".open-btn").on("click", function () {
  $(".sidebar").addClass("active");
});

$(".close-btn").on("click", function () {
  $(".sidebar").removeClass("active");
});

$(".show ul li").on("click", function () {
  $(".show ul li.active").removeClass("active");
  $(this).addClass("active");
});

window.addEventListener("DOMContentLoaded", (event) => {
  // Toggle the side navigation
  const sidebarToggle = document.body.querySelector("#sidebarToggle");
  if (sidebarToggle) {
    // Uncomment Below to persist sidebar toggle between refreshes
    // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
    //     document.body.classList.toggle('sb-sidenav-toggled');
    // }
    sidebarToggle.addEventListener("click", (event) => {
      event.preventDefault();
      document.body.classList.toggle("sb-sidenav-toggled");
      localStorage.setItem(
        "sb|sidebar-toggle",
        document.body.classList.contains("sb-sidenav-toggled")
      );
    });
  }
});

$(document).ready(function () {
  $("#dataTable").DataTable();
});

window.addEventListener("DOMContentLoaded", (event) => {
  // Simple-DataTables
  // https://github.com/fiduswriter/Simple-DataTables/wiki

  const datatablesSimple = document.getElementById("datatablesSimple");
  if (datatablesSimple) {
    new simpleDatatables.DataTable(datatablesSimple);
  }
});

// user_table start

// add new user
$(document).ready(function () {
  $(".add").click(function (e) {
    e.preventDefault();
    var name = $(".name").val();
    var email = $(".email").val();
    var phone = $(".phone").val();
    var password = $(".password").val();
    var confirm_password = $(".confirm_password").val();
    const valid_name = /^[a-zA-Z]+$/;
    const validate_email = /^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$/;
    const validate_phone = /^[6-9]\d{9}$/;
    const validate_password =
      /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{7,}$/;
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
    } else if (password == "" || password == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your password");
    } else if (!password.match(validate_password)) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your strong password");
    } else if (confirm_password == "" || confirm_password == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your confirm password");
    } else if (password != confirm_password) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Password not match");
    } else {
      $(".load").show();
      $(".add").prop("disabled", true);
      $(".cancel").prop("disabled", true);
      $.ajax({
        type: "POST",
        url: "user-table",
        data: {
          name: name,
          email: email,
          phone: phone,
          password: password,
          confirm_password: confirm_password,
        },
        success: function (data) {
          if (data == "add") {
            $(".load").hide();
            $(".add").prop("disabled", false);
            $(".cancel").prop("disabled", false);
            alertify.set("notifier", "position", "top-right");
            alertify.success("Add Successfully");
            setTimeout(function () {
              window.location.href = "user-table";
            }, 1000);
          } else {
            $(".load").hide();
            $(".add").prop("disabled", false);
            $(".cancel").prop("disabled", false);
            alertify.set("notifier", "position", "top-right");
            alertify.error(data);
          }
        },
        error: function (error) {
          $(".load").hide();
          $(".add").prop("disabled", false);
          $(".cancel").prop("disabled", false);
          alertify.set("notifier", "position", "top-right");
          alertify.error("Something went wrong. Please try again later");
        },
      });
    }
  });
});

// update user data fetch and show
$(document).ready(function () {
  $('.id').hide();    
  $(".show_data").click(function (e) {
    e.preventDefault();
    const value = $(this).val();
    if (value == "" || value == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Invaild data");
    } else {
      $.ajax({
        type: "POST",
        url: "user-table",
        data: {
          id: value,
        },
        success: function (data) {
          if (data == "no user") {
            $("#staticModalUpdate").modal("hide");
            alertify.set("notifier", "position", "top-right");
            alertify.error("User not Found :(");
          } else {
            $(".update_name").val(data.name);
            $(".update_email").val(data.email);
            $(".update_phone").val(data.phone_no);
            $('.id').val(value);
            $("#staticModalUpdate").modal("show");
          }
        },
        error: function (error) {
          alertify.set("notifier", "position", "top-right");
          alertify.error("Something went wrong. Please try again later");
        },
      });
    }
  });
});

// update user data
$(document).ready(function () {
  $('.id').hide();  
  $(".update").click(function (e) {
    e.preventDefault();
    var name = $(".update_name").val();
    const user_id = $('.id').val();
    const valid_name = /^[a-zA-Z]+$/;
    if (name == "" || name == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your name");
    } else if (name.length <= 2) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your full name without space");
    } else if (!valid_name.test(name)) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter valid name");
    } else {
      $(".load").show();
      $(".update").prop("disabled", true);
      $(".reset").prop("disabled", true);
      $.ajax({
        type: "POST",
        url: "user-table",
        data: {
          user_id:user_id,
          name: name,
        },
        success: function (data) {
          if (data == "update") {
            $(".load").hide();
            $(".update").prop("disabled", false);
            $(".reset").prop("disabled", false);
            alertify.set("notifier", "position", "top-right");
            alertify.success("Update Successfully");
            setTimeout(function () {
              window.location.href = "user-table";
            }, 1000);
          } else {
            $(".load").hide();
            $(".update").prop("disabled", false);
            $(".reset").prop("disabled", false);
            alertify.set("notifier", "position", "top-right");
            alertify.error(data);
          }
        },
        error: function (error) {
          $(".load").hide();
          $(".update").prop("disabled", false);
          $(".reset").prop("disabled", false);
          alertify.set("notifier", "position", "top-right");
          alertify.error("Something went wrong. Please try again later");
        },
      });
    }
  });
});

// delete user data

$(document).ready(function(){
  $('.delete_data').click(function(e){
    e.preventDefault();
    const user_id  = $(this).val();
    if (user_id == null || user_id==""){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Invalid data");
    }else{
      Swal.fire({
        title: 'Are you sure You want to delete the user data?',
        text: 'Once deleted you cannot recover the user data!',
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
            url:'user-table',
            data: {
              delete_id:user_id,
            },success:function(response){
              if (response == "delete"){
                swal.fire({
                  allowOutsideClick: false,
                  title: "Deleted",
                  text: "Your data has been deleted.",
                  icon: "success"
                });
                $("#datatablesSimple").load(location.href + " #datatablesSimple");
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
            text: "Your data is safe.",
            icon: "error"
          });
        }
      });
    }
  });
});

// user_table end

// admin_table start

// add new admin
$(document).ready(function () {
  $(".add_admin").click(function (e) {
    e.preventDefault();
    var name = $(".admin_name").val();
    var email = $(".admin_email").val();
    var password = $(".admin_password").val();
    const valid_name = /^[a-zA-Z]+$/;
    const validate_email = /^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$/;
    const validate_password =
      /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{7,}$/;
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
    } else if (password == "" || password == null) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your password");
    } else if (!password.match(validate_password)) {
      alertify.set("notifier", "position", "top-right");
      alertify.error("Please enter your strong password");
    } else {
      $(".load").show();
      $(".add_admin").prop("disabled", true);
      $(".cancel_admin").prop("disabled", true);
      $.ajax({
        type: "POST",
        url: "admin-table",
        data: {
          name: name,
          email: email,
          password: password,
        },
        success: function (data) {
          if (data == "add") {
            $(".load").hide();
            $(".add_admin").prop("disabled", false);
            $(".cancel_admin").prop("disabled", false);
            alertify.set("notifier", "position", "top-right");
            alertify.success("Add Successfully. Password send your email");
            setTimeout(function () {
              window.location.href = "admin-table";
            }, 1000);
          } else {
            $(".load").hide();
            $(".add_admin").prop("disabled", false);
            $(".cancel_admin").prop("disabled", false);
            alertify.set("notifier", "position", "top-right");
            alertify.error(data);
          }
        },
        error: function (error) {
          $(".load").hide();
          $(".add_admin").prop("disabled", false);
          $(".cancel_admin").prop("disabled", false);
          alertify.set("notifier", "position", "top-right");
          alertify.error("Something went wrong. Please try again later");
        },
      });
    }
  });
});

// delete admin data
$(document).ready(function(e){
  $('.delete_admin').click(function(e){
    e.preventDefault();
    const admin_id = $(this).val();
    if (admin_id == "" || admin_id == null){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Invalid data");
    }else{
      Swal.fire({
        title: 'Are you sure You want to delete the admin data?',
        text: 'Once deleted you cannot recover the admin data!',
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
            url:'admin-table',
            data: {
              admin_id:admin_id,
            },success:function(response){
              if (response == "delete"){
                swal.fire({
                  allowOutsideClick: false,
                  title: "Deleted",
                  text: "Your data has been deleted.",
                  icon: "success"
                });
                $("#datatablesSimple").load(location.href + " #datatablesSimple");
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
            text: "Your data is safe.",
            icon: "error"
          });
        }
      });
    }
  });
});

// admin_table end


// user_other_device_table start

// delete user other device data

$(document).ready(function(e){
  $('.other_user_id').click(function(e){
    e.preventDefault();
    const other_user_id = $(this).val();
    if (other_user_id == "" || other_user_id == null){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Invalid data");
    }else{
      Swal.fire({
        title: 'Are you sure You want to delete the user data?',
        text: 'Once deleted you cannot recover the user data!',
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
            url:'user-login-other-device',
            data: {
              other_user_id:other_user_id,
            },success:function(response){
              if (response == "delete"){
                swal.fire({
                  allowOutsideClick: false,
                  title: "Deleted",
                  text: "Your data has been deleted.",
                  icon: "success"
                });
                $("#datatablesSimple").load(location.href + " #datatablesSimple");
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
            text: "Your data is safe.",
            icon: "error"
          });
        }
      });
    }
  });
});

// user_other_device_table end

// slot_booking_table start

// delete slot booking

$(document).ready(function(e){
  $('.slot_id').click(function(e){
    e.preventDefault();
    const slot_id = $(this).val();
    if (slot_id == "" || slot_id == null){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Invalid data");
    }else{
      Swal.fire({
        title: 'Are you sure You want to delete the slot data?',
        text: 'Once deleted you cannot recover the slot data!',
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
            url:'user-slot-table',
            data: {
              slot_id:slot_id,
            },success:function(response){
              if (response == "delete"){
                swal.fire({
                  allowOutsideClick: false,
                  title: "Deleted",
                  text: "Your data has been deleted.",
                  icon: "success"
                });
                $("#datatablesSimple").load(location.href + " #datatablesSimple");
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
            text: "Your data is safe.",
            icon: "error"
          });
        }
      });
    }
  });
});

// slot_booking_table end

// admin_other_device_table start

// delete admin other device
$(document).ready(function(e){
  $('.other_admin_id').click(function(e){
    e.preventDefault();
    const other_admin_id = $(this).val();
    if (other_admin_id == "" || other_admin_id == null){
      alertify.set("notifier", "position", "top-right");
      alertify.error("Invalid data");
    }else{
      Swal.fire({
        title: 'Are you sure You want to delete the admin data?',
        text: 'Once deleted you cannot recover the admin data!',
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
            url:'admin-login-other-device',
            data: {
              other_admin_id:other_admin_id,
            },success:function(response){
              if (response == "delete"){
                swal.fire({
                  allowOutsideClick: false,
                  title: "Deleted",
                  text: "Your data has been deleted.",
                  icon: "success"
                });
                $("#datatablesSimple").load(location.href + " #datatablesSimple");
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
            text: "Your data is safe.",
            icon: "error"
          });
        }
      });
    }
  });
});

// admin_other_device_table start