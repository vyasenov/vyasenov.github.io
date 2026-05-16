// Reading-progress bar for blog posts: fills as the reader scrolls down the page.
document.addEventListener("DOMContentLoaded", function () {
    const bar = document.createElement("div");
    bar.id = "reading-progress";
    document.body.appendChild(bar);

    function update() {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        bar.style.width = pct + "%";
    }

    document.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();
});
