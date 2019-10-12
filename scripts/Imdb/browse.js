$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
      $(this).toggleClass('active');
    });

    
    $('#orgSubMenu').on('click', function (event) {
      alert();
    });


  });