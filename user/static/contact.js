$(document).ready(function () {
    const contact = {
        init: function () {
            this.bindEvents();
        },
        bindEvents: function () {
            console.log("ready to bind events");
            // this.handlePostContact();
            this.handlePostContactWithOnClick();
        },

        /* Hanle POST request with form
            Things to remember is:
                + You have to handle submit event for this form, if you want browser check validation input fields before the form is process by django view.
                + type of button is submit not button
        */
        handlePostContact: function () {
            $('#contact-form').on('submit', function (event) {
                event.preventDefault();
                $.ajax({
                    url: '/users/contact/',
                    type: 'POST',
                    data: $(this).serialize(),
                    dataType: 'json',
                    success: function (response) {
                        if (response.success) {
                            $('#contact-form').hide();
                            $('#alert').html('<div class="alert alert-success">Thank you for your message!</div>').show();
                        } else {
                            $('#alert').html('<div class="alert alert-danger">' + response.errors + '</div>').show();
                        }
                    }
                });
            });
        },

        /* Incorrect way to handle submit form */
        handlePostContactWithOnClick: function () {
            $("#saveContactBtn").on("click", function (e) {
                e.preventDefault();
                console.log("handle click event");

                $.ajax({
                    url: '/users/contact/',
                    type: 'POST',
                    data: $('#contact-form').serialize(),
                    dataType: 'json',
                    success: function (response) {
                        if (response.success) {
                            $('#contact-form').hide();
                            $('#alert').html('<div class="alert alert-success">Thank you for your message!</div>').show();
                        } else {
                            $('#alert').html('<div class="alert alert-danger">' + response.errors + '</div>').show();
                        }
                    }
                });
            })
        }
    };
    contact.init();
}(jQuery));