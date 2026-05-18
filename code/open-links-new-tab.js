document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll("a[href]");
    links.forEach(link => {
      // Only externalize links that actually point to a different host.
      if (link.host && link.host !== window.location.host && !link.target) {
        link.setAttribute("target", "_blank");
        link.setAttribute("rel", "noopener noreferrer");
      }
    });
  });
  