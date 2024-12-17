const imageInput = document.getElementById('imageInput');
const originalImage = document.getElementById('originalImage');
const responseImage = document.getElementById('responseImage');
const sendButton = document.getElementById('sendButton');
const dataTable = document.getElementById('dataTable').getElementsByTagName('tbody')[0];

imageInput.addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            originalImage.src = e.target.result;
            originalImage.style.display = 'block';
            sendButton.style.display = 'block';
        }
        reader.readAsDataURL(file);
    }
});

sendButton.addEventListener('click', function() {
    const file = imageInput.files[0];
    const formData = new FormData();
    formData.append('image', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Show the processed image
        responseImage.src = data.image_proc;
        responseImage.style.display = 'block';

        // Update the table with IP and DateTime
        const newRow = dataTable.insertRow();
        newRow.innerHTML = `
            <td>${data.ip}</td>
            <td>${data.datetime}</td>
            <td><img src="${data.image}" alt="Original Image" style="width: 100px; height: auto;"></td>
            <td><img src="${data.image_proc}" alt="Processed Image" style="width: 100px; height: auto;"></td>
            <td><button class="delete-btn" onclick="deleteRow(this)">🗑️</button></td>
        `;
    })
    .catch(error => console.error('Error:', error));
});

function deleteRow(button) {
    const row = button.parentNode.parentNode;
    dataTable.deleteRow(row.rowIndex - 1);
}
