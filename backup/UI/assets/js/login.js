$(document).ready(function() {
    /*Login Page*/
    $(document).mousemove(function(event) {
        TweenLite.to($("body"),
            .5, {
                css: {
                    backgroundPosition: "" + parseInt(event.pageX / 8) + "px " + parseInt(event.pageY / '12') + "px, " + parseInt(event.pageX / '15') + "px " + parseInt(event.pageY / '15') + "px, " + parseInt(event.pageX / '30') + "px " + parseInt(event.pageY / '30') + "px",
                    "background-position": parseInt(event.pageX / 8) + "px " + parseInt(event.pageY / 12) + "px, " + parseInt(event.pageX / 15) + "px " + parseInt(event.pageY / 15) + "px, " + parseInt(event.pageX / 30) + "px " + parseInt(event.pageY / 30) + "px"
                }
            })
    });

    /* Vendor DashBoard*/
    $('#id_breakfast_selector').multiSelect({});
    $('#id_lunch_selector').multiSelect({});
    $('#id_snacks_selector').multiSelect({});
    $('#id_dinner_selector').multiSelect({});

    $(document).on('change', '.meal-selector', function() {

        $('.menu-create-wrap').addClass('hide');
        switch (this.id) {
            case "id_select_breakfast":
                $(".menu-create-wrap-breakfast").removeClass('hide');
                break;

            case "id_select_lunch":
                $(".menu-create-wrap-lunch").removeClass('hide');
                break;


            case "id_select_snacks":
                $(".menu-create-wrap-snacks").removeClass('hide');
                break;

            case "id_select_dinner":
                $(".menu-create-wrap-dinner").removeClass('hide');
                break;
        }
    });


})
