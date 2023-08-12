
$(document).ready(function(){
    $('.load').hide();
    $(".user-content").hide();
    $(".home").click(function(){
        $(".dashboard-content").show();
        $(".user-content").hide();
    });
    $(".user").click(function(){
        $(".dashboard-content").hide();
        $(".user-content").show();
    });
});

$(document).ready(function(){
    new DataTable('#example', {
      responsive: true
    });
  });

$(".sidebar ul li").on("click",function(){
    $(".sidebar ul li.active").removeClass("active");
    $(this).addClass("active");
});

$('.open-btn').on('click',function(){
    $('.sidebar').addClass("active");
});

$('.close-btn').on('click',function(){
    $('.sidebar').removeClass("active");
});


$(".show ul li").on("click",function(){
    $(".show ul li.active").removeClass("active");
    $(this).addClass("active");
});


window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

$(document).ready(function() {
    $('#dataTable').DataTable();
});

window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }
});
  