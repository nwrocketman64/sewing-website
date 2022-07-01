// The default current index.
let slideIndex = 1;

// Start the slide function.
showSlides(slideIndex);

// An interface function for the button controls on the slides.
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// The function controls which slide should appear.
function showSlides(n) {
    // Get all the slides by their class name.
    let slides = document.getElementsByClassName("slides");

    // Check to see if there are images to show.
    if (slides.length > 0){
        // If the index is greater than the slide length, loop it back.
        if (n > slides.length) {
            slideIndex = 1;
        }

        // If the index is less than one, loop it to the last slide.
        if (n < 1) {
            slideIndex = slides.length;
        }

        // Set all the slides to not appearing.
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }

        // Make the slide that the index is one to appear.
        slides[slideIndex - 1].style.display = "block";
    }
}
