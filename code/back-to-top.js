// Show the Back-to-Top button when scrolling down
document.addEventListener("scroll", function () {
    const button = document.getElementById("back-to-top");
    if (window.scrollY > 200) { // Show the button after scrolling 200px
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
});

// Scroll to the top when the button is clicked
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: "smooth" });
}