/*
    Function to send Contact Form message
*/
function sendMail(contactForm) {
    emailjs.send("gmail", "contact_form", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "your_message": contactForm.textarea1.value
    })
        .then(
            function (response) {
                console.log("SUCCESS", response);
            },
            function (error) {
                console.log("FAILED", error);
            }
        );
    return false;
}

/*
    jQuery to resize textarea in Message line
*/
$('#textarea1').val('New Text');
  M.textareaAutoResize($('#textarea1'));