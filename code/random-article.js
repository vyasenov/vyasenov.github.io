(function () {
  function init() {
    var btn = document.getElementById("random-article-btn");
    if (!btn) return;

    var wrapper = document.getElementById("random-article-sidebar-wrapper");
    if (wrapper) {
      var sidebar = document.getElementById("quarto-margin-sidebar");
      if (sidebar) {
        wrapper.style.display = "block";
        sidebar.appendChild(wrapper);
      }
    }

    btn.addEventListener("click", function () {
      var path = window.location.pathname || "";
      var listingUrl = path.indexOf("/blog/") !== -1 ? "../listings.json" : "listings.json";

      fetch(listingUrl)
        .then(function (res) { return res.json(); })
        .then(function (data) {
          var blogListing = data.find(function (entry) {
            return entry.listing === "/blog/index.html";
          });
          if (!blogListing || !blogListing.items || blogListing.items.length === 0) {
            return;
          }
          var items = blogListing.items.filter(function (href) {
            return typeof href === "string" &&
              href.indexOf("/blog/") === 0 &&
              href !== "/blog/index.html" &&
              href.endsWith(".html");
          });
          if (items.length === 0) return;
          var randomItem = items[Math.floor(Math.random() * items.length)];
          window.location.href = window.location.origin + (randomItem.charAt(0) === "/" ? randomItem : "/" + randomItem);
        })
        .catch(function () {});
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
