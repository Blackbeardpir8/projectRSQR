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