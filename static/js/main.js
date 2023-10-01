(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();

    // Initiate the wowjs
    new WOW().init();

    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').css('top', '0px');
        } else {
            $('.sticky-top').css('top', '-100px');
        }
    });

    // NavBar active
    const navLinkEls = document.querySelectorAll('.nav-link');
    console.log(navLinkEls);
    const windowsPathname = window.location.pathname;

    navLinkEls.forEach(navLinkEl => {
        const navLinkPathname = new URL(navLinkEl.href).pathname;

        if (windowsPathname === navLinkPathname) {
            navLinkEl.classList.add('active');
        }
    });

    // Dropdown on mouse hover
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";

    $(window).on("load resize", function () {
        if (this.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(
                function () {
                    const $this = $(this);
                    $this.addClass(showClass);
                    $this.find($dropdownToggle).attr("aria-expanded", "true");
                    $this.find($dropdownMenu).addClass(showClass);
                },
                function () {
                    const $this = $(this);
                    $this.removeClass(showClass);
                    $this.find($dropdownToggle).attr("aria-expanded", "false");
                    $this.find($dropdownMenu).removeClass(showClass);
                }
            );
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });

    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });

    // Date and time picker
    $('.date').datetimepicker({
        format: 'L'
    });
    $('.time').datetimepicker({
        format: 'LT'
    });

    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 25,
        dots: true,
        loop: true,
        nav: false,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });

    document.addEventListener('DOMContentLoaded', function () {
        // Form validation
        var bookingForm = document.getElementById('booking-form');
        if (bookingForm) { // Check if the form element exists
            bookingForm.addEventListener('submit', function (event) {
                // Get the form fields
                var providerSelect = document.getElementById('provider');
                var serviceSelect = document.getElementById('service');
                var carSelect = document.getElementById('car');
                var dateInput = document.querySelector('input[name="date"]');
                var emailInput = document.getElementById('email'); // Get the email input field
    
                // Email validation regular expression
                var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    
                // Check if any of the required fields are empty
                if (!providerSelect.value || providerSelect.value === 'Select A Service Provider' ||
                    !serviceSelect.value || serviceSelect.value === 'Select A Service' ||
                    !carSelect.value || carSelect.value === 'Select Your Car' ||
                    !dateInput.value || !emailPattern.test(emailInput.value)) { // Check if email is valid using the pattern
                    // Prevent form submission
                    event.preventDefault();
    
                    // Show an error message
                    alert('Please fill out all required fields correctly before booking.');
            }
          });
        }
      });

})(jQuery);
