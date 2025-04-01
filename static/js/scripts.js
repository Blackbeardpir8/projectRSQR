document.addEventListener("DOMContentLoaded", function () {
    // Base
  
// End Base
    
//Register


// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm_password');
    const allInputs = document.querySelectorAll('.form-input');
    
    // Add animation class to form elements sequentially
    function addSequentialAnimation() {
        const formGroups = document.querySelectorAll('.form-group');
        formGroups.forEach((group, index) => {
            setTimeout(() => {
                group.classList.add('fade-in');
            }, 100 * index);
        });
    }
    
    // Call the animation function after a short delay
    setTimeout(addSequentialAnimation, 300);
    
    // Form validation
    function validateForm(e) {
        let isValid = true;
        
        // Clear previous error messages
        document.querySelectorAll('.error-message').forEach(el => el.remove());
        document.querySelectorAll('.form-input.error').forEach(el => el.classList.remove('error'));
        
        // Validate email format
        const email = document.getElementById('email');
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email.value)) {
            showError(email, 'Please enter a valid email address');
            isValid = false;
        }
        
        // Validate phone number (simple validation)
        const phone = document.getElementById('phone');
        const phoneRegex = /^[0-9+\-\s]{10,15}$/;
        if (!phoneRegex.test(phone.value)) {
            showError(phone, 'Please enter a valid phone number');
            isValid = false;
        }
        
        // Validate password length
        if (password.value.length < 8) {
            showError(password, 'Password must be at least 8 characters');
            isValid = false;
        }
        
        // Validate password match
        if (password.value !== confirmPassword.value) {
            showError(confirmPassword, 'Passwords do not match');
            isValid = false;
        }
        
        if (!isValid) {
            e.preventDefault();
        } else {
            // Add loading effect to button when form is valid
            const button = document.querySelector('.register-btn');
            button.innerHTML = '<span class="loader"></span> Creating Account...';
            button.disabled = true;
        }
    }
    
    // Show error message
    function showError(input, message) {
        input.classList.add('error');
        const errorMessage = document.createElement('span');
        errorMessage.className = 'error-message';
        errorMessage.textContent = message;
        input.parentNode.appendChild(errorMessage);
    }
    
    // Add focus and blur event listeners to inputs for animation
    allInputs.forEach(input => {
        // Show/hide placeholder on focus/blur
        input.addEventListener('focus', function() {
            this.setAttribute('data-placeholder', this.getAttribute('placeholder'));
            this.setAttribute('placeholder', '');
        });
        
        input.addEventListener('blur', function() {
            this.setAttribute('placeholder', this.getAttribute('data-placeholder'));
        });
    });
    
    // Password strength indicator
    if (password) {
        password.addEventListener('input', function() {
            const strength = calculatePasswordStrength(this.value);
            updatePasswordStrengthIndicator(strength);
        });
    }
    
    function calculatePasswordStrength(password) {
        let strength = 0;
        
        // Length check
        if (password.length >= 8) strength += 1;
        if (password.length >= 12) strength += 1;
        
        // Complexity checks
        if (/[A-Z]/.test(password)) strength += 1;
        if (/[a-z]/.test(password)) strength += 1;
        if (/[0-9]/.test(password)) strength += 1;
        if (/[^A-Za-z0-9]/.test(password)) strength += 1;
        
        return Math.min(strength, 5);
    }
    
    function updatePasswordStrengthIndicator(strength) {
        // Remove any existing indicator
        const existingIndicator = document.querySelector('.password-strength');
        if (existingIndicator) existingIndicator.remove();
        
        // Create new indicator
        const indicator = document.createElement('div');
        indicator.className = 'password-strength';
        
        // Create strength bars
        const strengthBar = document.createElement('div');
        strengthBar.className = 'strength-bar';
        
        for (let i = 0; i < 5; i++) {
            const bar = document.createElement('span');
            bar.className = i < strength ? `strength-level strength-level-${strength}` : 'strength-level';
            strengthBar.appendChild(bar);
        }
        
        // Add label
        const label = document.createElement('span');
        label.className = 'strength-label';
        
        switch(strength) {
            case 0:
            case 1:
                label.textContent = 'Weak';
                label.style.color = '#ff3860';
                break;
            case 2:
            case 3:
                label.textContent = 'Medium';
                label.style.color = '#ffdd57';
                break;
            case 4:
            case 5:
                label.textContent = 'Strong';
                label.style.color = '#23d160';
                break;
        }
        
        indicator.appendChild(strengthBar);
        indicator.appendChild(label);
        
        // Add to DOM after password field
        password.parentNode.appendChild(indicator);
    }
    
    // Form submission
    if (registerForm) {
        registerForm.addEventListener('submit', validateForm);
    }
    
    // Add some CSS for the password strength indicator
    const style = document.createElement('style');
    style.textContent = `
        .password-strength {
            margin-top: 8px;
        }
        
        .strength-bar {
            display: flex;
            gap: 4px;
            margin-bottom: 4px;
        }
        
        .strength-level {
            height: 4px;
            flex: 1;
            background-color: #e0e0e0;
            border-radius: 2px;
        }
        
        .strength-level-1 {
            background-color: #ff3860;
        }
        
        .strength-level-2, .strength-level-3 {
            background-color: #ffdd57;
        }
        
        .strength-level-4, .strength-level-5 {
            background-color: #23d160;
        }
        
        .strength-label {
            font-size: 0.8rem;
        }
        
        .loader {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 2px solid rgba(255,255,255,0.3);
            border-radius: 50%;
            border-top-color: white;
            animation: spin 0.8s linear infinite;
            vertical-align: middle;
            margin-right: 8px;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    `;
    document.head.appendChild(style);
});


//end Register

//FAQ
document.addEventListener("DOMContentLoaded", function () {
    const faqItems = document.querySelectorAll(".faq-item");

    faqItems.forEach(item => {
        item.addEventListener("click", function () {
            this.classList.toggle("active");
        });
    });
});


// Medical
<script>
document.addEventListener("DOMContentLoaded", function () {
    fetch("/medical-details/", {
        method: "GET",
        headers: { "Authorization": "Bearer " + localStorage.getItem("token") }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("blood_type").value = data.blood_type || "";
        document.getElementById("medical_conditions").value = data.medical_conditions || "";
        document.getElementById("allergies").value = data.allergies || "";
        document.getElementById("past_surgeries").value = data.past_surgeries || "";
        document.getElementById("current_medications").value = data.current_medications || "";
        document.getElementById("primary_doctor_name").value = data.primary_doctor_name || "";
        document.getElementById("primary_doctor_contact").value = data.primary_doctor_contact || "";
    });

    document.getElementById("medical_document").addEventListener("change", function(event) {
        let file = event.target.files[0];
        if (file) document.getElementById("medicalPdfPreview").src = URL.createObjectURL(file);
    });

    document.getElementById("insurance_document").addEventListener("change", function(event) {
        let file = event.target.files[0];
        if (file) document.getElementById("insurancePdfPreview").src = URL.createObjectURL(file);
    });
});

function updateMedicalDetails() {
    let formData = new FormData();
    formData.append("blood_type", document.getElementById("blood_type").value);
    formData.append("medical_conditions", document.getElementById("medical_conditions").value);
    formData.append("allergies", document.getElementById("allergies").value);
    formData.append("past_surgeries", document.getElementById("past_surgeries").value);
    formData.append("current_medications", document.getElementById("current_medications").value);
    formData.append("primary_doctor_name", document.getElementById("primary_doctor_name").value);
    formData.append("primary_doctor_contact", document.getElementById("primary_doctor_contact").value);

    let medicalDoc = document.getElementById("medical_document").files[0];
    if (medicalDoc) formData.append("medical_document", medicalDoc);

    let insuranceDoc = document.getElementById("insurance_document").files[0];
    if (insuranceDoc) formData.append("insurance_document", insuranceDoc);

    fetch("/medical-details/", {
        method: "PUT",
        headers: { "Authorization": "Bearer " + localStorage.getItem("token") },
        body: formData
    })
    .then(response => response.json())
    .then(data => alert("Medical details updated successfully!"))
    .catch(error => alert("Error updating medical details."));
}
</script>


//Emergency//


const API_BASE_URL = "/api/emergency/contacts/";  
const token = localStorage.getItem("jwt_token");  // Fetch JWT token from local storage

// Fetch and display all emergency contacts
async function fetchContacts() {
    const response = await fetch(API_BASE_URL, {
        headers: { "Authorization": `Bearer ${token}` }
    });

    const contacts = await response.json();
    const contactsList = document.getElementById("contacts-list");
    contactsList.innerHTML = "";

    contacts.forEach(contact => {
        contactsList.innerHTML += `
            <div class="contact-card">
                <p><strong>${contact.name}</strong> (${contact.relation})</p>
                <p>Primary: ${contact.primary_phone}</p>
                <p>Alternate: ${contact.alternate_phone || "N/A"}</p>
                <button onclick="editContact(${contact.id}, '${contact.name}', '${contact.primary_phone}', '${contact.alternate_phone}', '${contact.relation}')">Edit</button>
                <button onclick="deleteContact(${contact.id})">Delete</button>
            </div>
        `;
    });
}

// Add a new contact
document.getElementById("contact-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const newContact = {
        name: document.getElementById("name").value,
        primary_phone: document.getElementById("primary_phone").value,
        alternate_phone: document.getElementById("alternate_phone").value || null,
        relation: document.getElementById("relation").value,
    };

    const response = await fetch(API_BASE_URL, {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify(newContact)
    });

    if (response.ok) {
        alert("Contact added successfully!");
        fetchContacts();  // Refresh the contact list
        document.getElementById("contact-form").reset();
    } else {
        alert("Failed to add contact.");
    }
});

// Delete a contact
async function deleteContact(contactId) {
    if (!confirm("Are you sure you want to delete this contact?")) return;

    const response = await fetch(`${API_BASE_URL}${contactId}/`, {
        method: "DELETE",
        headers: { "Authorization": `Bearer ${token}` }
    });

    if (response.ok) {
        alert("Contact deleted successfully!");
        fetchContacts();
    } else {
        alert("Failed to delete contact.");
    }
}

// Edit a contact
async function editContact(id, name, primary_phone, alternate_phone, relation) {
    const newName = prompt("Update Name:", name);
    const newPrimaryPhone = prompt("Update Primary Phone:", primary_phone);
    const newAlternatePhone = prompt("Update Alternate Phone:", alternate_phone);
    const newRelation = prompt("Update Relation:", relation);

    const updatedContact = {
        name: newName,
        primary_phone: newPrimaryPhone,
        alternate_phone: newAlternatePhone,
        relation: newRelation
    };

    const response = await fetch(`${API_BASE_URL}${id}/`, {
        method: "PATCH",
        headers: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify(updatedContact)
    });

    if (response.ok) {
        alert("Contact updated successfully!");
        fetchContacts();
    } else {
        alert("Failed to update contact.");
    }
}

// Load contacts when page loads
window.onload = fetchContacts;



//End Emergency//