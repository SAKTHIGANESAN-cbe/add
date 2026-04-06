/*
   Plastic Waste Management System - JavaScript
   Client-side functionality and interactivity
*/

// ============================================
// DOM READY
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    console.log('Plastic Waste Management System loaded');
    initializeEventListeners();
});

// ============================================
// EVENT LISTENERS INITIALIZATION
// ============================================

function initializeEventListeners() {
    // Add smooth scrolling to CTA buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Add ripple effect on click
            addRippleEffect(e, this);
        });
    });

    // Add form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            validateForm(e, this);
        });
    });
}

// ============================================
// RIPPLE EFFECT
// ============================================

function addRippleEffect(e, element) {
    // Only apply to buttons
    if (!element.classList.contains('btn')) return;

    const rect = element.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const ripple = document.createElement('span');
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    ripple.classList.add('ripple');

    // Add ripple style if not exists
    if (!document.querySelector('style[data-ripple]')) {
        const style = document.createElement('style');
        style.setAttribute('data-ripple', 'true');
        style.innerHTML = `
            .btn {
                position: relative;
                overflow: hidden;
            }
            .ripple {
                position: absolute;
                width: 20px;
                height: 20px;
                background: rgba(255, 255, 255, 0.5);
                border-radius: 50%;
                transform: scale(0);
                animation: rippleAnimation 0.6s ease-out;
                pointer-events: none;
            }
            @keyframes rippleAnimation {
                to {
                    transform: scale(4);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }

    element.appendChild(ripple);

    // Remove ripple after animation
    setTimeout(() => ripple.remove(), 600);
}

// ============================================
// FORM VALIDATION
// ============================================

function validateForm(e, form) {
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    let isValid = true;

    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            showFieldError(input, 'This field is required');
        } else {
            clearFieldError(input);
        }
    });

    // Additional validation for specific fields
    const emailInput = form.querySelector('input[type="email"]');
    if (emailInput && emailInput.value) {
        if (!isValidEmail(emailInput.value)) {
            isValid = false;
            showFieldError(emailInput, 'Please enter a valid email');
        }
    }

    const passwordInputs = form.querySelectorAll('input[name="password"], input[name="confirm_password"]');
    if (passwordInputs.length === 2) {
        if (passwordInputs[0].value !== passwordInputs[1].value) {
            isValid = false;
            showFieldError(passwordInputs[1], 'Passwords do not match');
        }
    }

    if (!isValid) {
        e.preventDefault();
    }
}

function showFieldError(field, message) {
    // Remove existing error if any
    clearFieldError(field);

    // Add error styling
    field.style.borderColor = '#E74C3C';
    field.style.backgroundColor = '#FADBD8';

    // Create error message
    const errorMsg = document.createElement('small');
    errorMsg.className = 'field-error';
    errorMsg.style.color = '#E74C3C';
    errorMsg.style.display = 'block';
    errorMsg.style.marginTop = '5px';
    errorMsg.textContent = '❌ ' + message;

    field.parentNode.insertBefore(errorMsg, field.nextSibling);
}

function clearFieldError(field) {
    field.style.borderColor = '';
    field.style.backgroundColor = '';

    const errorMsg = field.parentNode.querySelector('.field-error');
    if (errorMsg) {
        errorMsg.remove();
    }
}

// ============================================
// EMAIL VALIDATION
// ============================================

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// ============================================
// TABLE FUNCTIONALITY
// ============================================

// Search functionality in view page
const searchInput = document.getElementById('searchInput');
if (searchInput) {
    searchInput.addEventListener('keyup', debounce(filterTable, 300));
}

// Type filter functionality
const typeFilter = document.getElementById('typeFilter');
if (typeFilter) {
    typeFilter.addEventListener('change', filterTable);
}

function filterTable() {
    const searchTerm = document.getElementById('searchInput')?.value.toLowerCase() || '';
    const typeFilter = document.getElementById('typeFilter')?.value || '';
    const tableBody = document.getElementById('tableBody');

    if (!tableBody) return;

    const rows = tableBody.getElementsByTagName('tr');

    for (let row of rows) {
        let showRow = true;
        const type = row.dataset.type;

        if (typeFilter && type !== typeFilter) {
            showRow = false;
        }

        if (searchTerm) {
            const rowText = row.textContent.toLowerCase();
            if (!rowText.includes(searchTerm)) {
                showRow = false;
            }
        }

        row.style.display = showRow ? '' : 'none';
    }

    // Add animation to visible rows
    const visibleRows = Array.from(rows).filter(row => row.style.display !== 'none');
    visibleRows.forEach((row, index) => {
        row.style.animation = `slideIn 0.3s ease ${index * 0.05}s`;
    });
}

// ============================================
// TABLE SORTING
// ============================================

function sortTable(columnIndex) {
    const table = document.getElementById('recordsTable');
    if (!table) return;

    const tbody = table.getElementsByTagName('tbody')[0];
    const rows = Array.from(tbody.getElementsByTagName('tr'));

    // Sort rows
    rows.sort((a, b) => {
        const aValue = a.getElementsByTagName('td')[columnIndex].textContent.trim();
        const bValue = b.getElementsByTagName('td')[columnIndex].textContent.trim();

        // Check if values are numbers
        if (!isNaN(aValue) && !isNaN(bValue)) {
            return parseFloat(aValue) - parseFloat(bValue);
        }

        // Sort alphabetically
        return aValue.localeCompare(bValue);
    });

    // Re-append rows in sorted order
    rows.forEach(row => {
        tbody.appendChild(row);
        // Add animation
        row.style.animation = 'slideIn 0.3s ease';
    });
}

// ============================================
// UTILITY FUNCTIONS
// ============================================

// Debounce function to limit function calls
function debounce(func, delay) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func.apply(this, args), delay);
    };
}

// Show notification
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;

    // Add styles if not exists
    if (!document.querySelector('style[data-notification]')) {
        const style = document.createElement('style');
        style.setAttribute('data-notification', 'true');
        style.innerHTML = `
            .notification {
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 15px 20px;
                border-radius: 8px;
                background: white;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                z-index: 1000;
                animation: slideIn 0.3s ease;
                font-weight: 500;
            }
            .notification-success {
                border-left: 4px solid #2ECC71;
                color: #2ECC71;
            }
            .notification-error {
                border-left: 4px solid #E74C3C;
                color: #E74C3C;
            }
            .notification-warning {
                border-left: 4px solid #F39C12;
                color: #F39C12;
            }
        `;
        document.head.appendChild(style);
    }

    document.body.appendChild(notification);

    // Remove notification after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Set date input to today
function setTodayDate(inputId) {
    const dateInput = document.getElementById(inputId);
    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.value = today;
    }
}

// ============================================
// CONFIRM DELETE
// ============================================

function confirmDelete(message = 'Are you sure you want to delete this record?') {
    return confirm(message);
}

// ============================================
// LOCAL STORAGE FUNCTIONS
// ============================================

// Save form data to localStorage for recovery
function saveFormData(formId) {
    const form = document.getElementById(formId);
    if (form) {
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });
        localStorage.setItem(`form_${formId}`, JSON.stringify(data));
    }
}

// Restore form data from localStorage
function restoreFormData(formId) {
    const savedData = localStorage.getItem(`form_${formId}`);
    if (savedData) {
        const data = JSON.parse(savedData);
        const form = document.getElementById(formId);
        if (form) {
            Object.keys(data).forEach(key => {
                const input = form.querySelector(`[name="${key}"]`);
                if (input) {
                    input.value = data[key];
                }
            });
        }
    }
}

// Clear saved form data
function clearFormData(formId) {
    localStorage.removeItem(`form_${formId}`);
}

// Save form data before submit (for accidental page reload)
document.addEventListener('keydown', function(e) {
    // Auto-save on Ctrl+S
    if (e.ctrlKey && e.key === 's') {
        e.preventDefault();
        const form = document.querySelector('form.form-container');
        if (form) {
            saveFormData(form.id || 'main_form');
            showNotification('Form saved locally', 'success');
        }
    }
});

// ============================================
// DATE AND TIME UTILITIES
// ============================================

function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(date).toLocaleDateString('en-US', options);
}

function getRelativeTime(date) {
    const now = new Date();
    const diff = now - new Date(date);
    const seconds = Math.floor(diff / 1000);

    if (seconds < 60) return 'Just now';
    const minutes = Math.floor(seconds / 60);
    if (minutes < 60) return `${minutes}m ago`;
    const hours = Math.floor(minutes / 60);
    if (hours < 24) return `${hours}h ago`;
    const days = Math.floor(hours / 24);
    if (days < 30) return `${days}d ago`;
    const months = Math.floor(days / 30);
    return `${months}mo ago`;
}

// ============================================
// EXPORT DATA
// ============================================

function exportTableToCSV(tableId, filename = 'export.csv') {
    const table = document.getElementById(tableId);
    if (!table) return;

    let csv = [];
    const rows = table.querySelectorAll('tr');

    rows.forEach(row => {
        const cols = row.querySelectorAll('td, th');
        let csvRow = [];
        cols.forEach(col => {
            csvRow.push('"' + col.textContent.trim() + '"');
        });
        csv.push(csvRow.join(','));
    });

    downloadCSV(csv.join('\n'), filename);
}

function downloadCSV(data, filename) {
    const blob = new Blob([data], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    window.URL.revokeObjectURL(url);
}

// ============================================
// PRINT FUNCTIONALITY
// ============================================

function printTable(tableId) {
    const table = document.getElementById(tableId);
    if (!table) return;

    const printWindow = window.open('', '', 'height=400,width=800');
    printWindow.document.write('<html><head><title>Plastic Waste Records</title>');
    printWindow.document.write('<style>');
    printWindow.document.write('table { width: 100%; border-collapse: collapse; }');
    printWindow.document.write('th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }');
    printWindow.document.write('th { background-color: #4ECDC4; color: white; }');
    printWindow.document.write('</style></head><body>');
    printWindow.document.write('<h2>Plastic Waste Management Records</h2>');
    printWindow.document.write(table.outerHTML);
    printWindow.document.write('</body></html>');
    printWindow.document.close();
    printWindow.print();
}

// ============================================
// ACCESSIBILITY
// ============================================

// Keyboard navigation for tables
document.addEventListener('keydown', function(e) {
    const table = document.getElementById('recordsTable');
    if (!table) return;

    const rows = Array.from(table.querySelectorAll('tbody tr:not([style*="display: none"])'));
    const currentRow = document.activeElement?.closest('tr');
    const currentIndex = rows.indexOf(currentRow);

    if (e.key === 'ArrowDown' && currentIndex < rows.length - 1) {
        rows[currentIndex + 1].focus();
        e.preventDefault();
    } else if (e.key === 'ArrowUp' && currentIndex > 0) {
        rows[currentIndex - 1].focus();
        e.preventDefault();
    }
});

// ============================================
// ANALYTICS TRACKING
// ============================================

function trackEvent(eventName, eventData = {}) {
    console.log(`Event: ${eventName}`, eventData);
    // You can integrate Google Analytics or other tracking here
    // Example: ga('send', 'event', eventName, eventData);
}

// Track page views
window.addEventListener('load', function() {
    const pageName = document.body.className || 'unknown';
    trackEvent('page_view', { page: pageName });
});

// ============================================
// POLISH & NICE TOUCHES
// ============================================

// Add fade-in animation to page load
window.addEventListener('load', function() {
    document.body.style.opacity = '1';
});

// Add loading state to forms
document.addEventListener('submit', function(e) {
    const form = e.target;
    const submitBtn = form.querySelector('button[type="submit"]');
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = '⏳ Loading...';
    }
});

// Prevent double submission
let isSubmitting = false;

document.addEventListener('submit', function(e) {
    if (isSubmitting) {
        e.preventDefault();
        return false;
    }
    isSubmitting = true;
    setTimeout(() => {
        isSubmitting = false;
    }, 3000);
});

console.log('✅ JavaScript module loaded successfully!');
