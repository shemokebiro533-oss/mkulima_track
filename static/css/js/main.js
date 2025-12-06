// Mkulima Track - Main JavaScript File
console.log('Mkulima Track JS loaded');

// Form validation
document.addEventListener('DOMContentLoaded', function() {
    // Logout button handler
    const logoutLinks = document.querySelectorAll('a[href*="logout"]');
    logoutLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Create a hidden form and submit it
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = this.href;
            
            // Add CSRF token
            const csrfInput = document.createElement('input');
            csrfInput.type = 'hidden';
            csrfInput.name = 'csrfmiddlewaretoken';
            csrfInput.value = getCookie('csrftoken');
            form.appendChild(csrfInput);
            
            document.body.appendChild(form);
            form.submit();
        });
    });
    
    // Crop recommendation form enhancement
    const cropForm = document.querySelector('form[action*="crop"]');
    if (cropForm) {
        cropForm.addEventListener('submit', function(e) {
            const location = this.querySelector('[name="location"]');
            if (location && !location.value) {
                e.preventDefault();
                alert('Please select a location');
                location.focus();
            }
        });
    }
});

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}