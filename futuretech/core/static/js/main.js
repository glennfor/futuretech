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

    console.log('maini')
    $('#export-form').click(
      function(){
        console.log('in>>>>>>')
        html2canvas(document.querySelector('#profile')).then(function(canvas) {
            console.log('starting...')
            // only jpeg is supported by jsPDF
            var imgData = canvas.toDataURL("image/jpeg", 1.0);
            var pdf = new jsPDF();
          
            pdf.addImage(imgData, 'JPEG', 0, 0);
            pdf.save("download.pdf");
          console.log('done...')
      });
      }
    )
})(jQuery);



// (function () {
//     'use strict'
//     const forms = document.querySelectorAll('.requires-validation')
//     Array.from(forms)
//       .forEach(function (form) {
//         form.addEventListener('submit', function (event) {
//           if (!form.checkValidity()) {
//             event.preventDefault()
//             event.stopPropagation()
//           }
//           form.classList.add('was-validated')
//         }, false)
//       })
//     })()
    