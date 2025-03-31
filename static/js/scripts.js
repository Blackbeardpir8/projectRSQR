document.addEventListener("DOMContentLoaded", function () {
    // Base
  
// End Base
    


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