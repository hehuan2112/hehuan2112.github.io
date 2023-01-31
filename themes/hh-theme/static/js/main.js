/*! 
 * scripts for my site
 * Author: hehuan2112.github.io 
 */

/* force to hide expanded navbar when scroll down */
$(window).scroll(function(e) {
    var scroll = $(window).scrollTop();
    if (scroll >= 150) {
        $('#navbarMenu').collapse('hide');
    }

});

/* add classes into tables */
$("table:not(.highlighttable)").addClass("table table-hover table-sm table-bordered");
$("thead").addClass("thead-light");
