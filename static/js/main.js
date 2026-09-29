document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll(".navbar .nav-link");
    const navCollapse = document.querySelector(".navbar-collapse");

    navLinks.forEach(link => {
        link.addEventListener("click", () => {
            if (navCollapse.classList.contains("show")) {
                bootstrap.Collapse.getOrCreateInstance(navCollapse).hide();
            }
        });
    });

    const alerts = document.querySelectorAll(".alert");
    alerts.forEach(alert => {
        setTimeout(() => {
            bootstrap.Alert.getOrCreateInstance(alert).close();
        }, 5000);
    });
});
