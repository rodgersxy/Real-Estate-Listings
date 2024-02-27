document.addEventListener('DOMContentLoaded', function () {
    const date = new Date();
    document.querySelector('.year').innerHTML = date.getFullYear();
  
    setTimeout(function () {
      $('#message').fadeOut('slow');
    }, 3000);
  
    // Activate the carousel
    $('#imageSlider').carousel();
  
    document.getElementById('btn-back-to-top').addEventListener('click', function () {
      // Smoothly scroll to the top of the page
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  });
  