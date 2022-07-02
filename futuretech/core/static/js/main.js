(function ($) {
    // "use strict";

    

    $(window).scroll(function () {
        if ($(this).scrollTop() > 108) {
            $('.sticky-top').css( {
                'position': 'fixed',
                'top' : '0px'
            })
        } else {
            $('.sticky-top').css(   {'position': 'sticky',
            'top' : '1000px'}
        );
        }
        
    });
})(jQuery);

/*

-----General----
->Implement context reduces [title, app name]
->alerts 
->emailjs


---JS----
->Back to top
->Carousel
->Covert nav
->Rework the landing page

----includes----
animate.css
AOS
JQuery
Bootstrap

-----routes-------
/
/home    (home page)
/register (register an account)
/accounts/login (login)
/accounts/logout (logout)
/user/profile (You can view all your info here and also print)
/admin

login page, logout page, 404 page

*/

(function () {
    'use strict'
    const forms = document.querySelectorAll('.requires-validation')
    Array.from(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
          form.classList.add('was-validated')
        }, false)
      })
    })()
    