document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll("a[href]");
    links.forEach(link => {
      // Skip links that are explicitly set to open in the same tab or are anchors
      if (!link.href.startsWith(window.location.origin) && !link.target) {
        link.setAttribute("target", "_blank");
        link.setAttribute("rel", "noopener noreferrer");
      }
    });
  });
  