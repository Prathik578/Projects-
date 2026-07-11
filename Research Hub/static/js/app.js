// Confirm Delete Action
document.addEventListener("DOMContentLoaded", function() {
    const deleteForms = document.querySelectorAll("form[data-confirm]");
    deleteForms.forEach(form => {
        form.addEventListener("submit", function(event) {
            if (!confirm(
                    "Are you sure you want to delete this paper? This cannot be undone."
                    )) {
                event.preventDefault();
            }
        });
    });
});

// Show Selected Filename
document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.querySelector("input[type='file']");
    const fileNameDisplay = document.getElementById(
    "file-name-display"); // You'll need to add this span in HTML

    if (fileInput) {
        fileInput.addEventListener("change", function() {
            if (fileInput.files.length > 0) {
                const fileName = fileInput.files[0].name;
                if (fileNameDisplay) {
                    fileNameDisplay.textContent = `Selected: ${fileName}`;
                    fileNameDisplay.className = "text-success mt-2 small";
                }
            }
        });
    }
});

// Auto-hide Alerts
document.addEventListener("DOMContentLoaded", function() {
    const alerts = document.querySelectorAll(".alert");
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 3000); // 3 seconds
    });
});
