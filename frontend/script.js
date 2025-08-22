// Client‑side logic for the property search and scheduling portal

// Fetch and display properties when the search form is submitted
const searchForm = document.getElementById('searchForm');
const propertiesList = document.getElementById('properties');
const scheduleSection = document.getElementById('schedule');
const scheduleForm = document.getElementById('scheduleForm');
const confirmation = document.getElementById('confirmation');

searchForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  // Fetch all properties from the backend
  const res = await fetch('http://localhost:5000/properties');
  const properties = await res.json();
  propertiesList.innerHTML = '';
  properties.forEach((prop) => {
    const li = document.createElement('li');
    li.textContent = `${prop.address}, ${prop.city} – $${prop.price.toLocaleString()}`;
    li.addEventListener('click', () => selectProperty(prop));
    propertiesList.appendChild(li);
  });
});

function selectProperty(property) {
  // Display the scheduling form for the selected property
  scheduleSection.hidden = false;
  document.getElementById('propertyId').value = property.id;
  document.getElementById('selectedProperty').textContent =
    `Scheduling viewing for ${property.address}, ${property.city}`;
}

scheduleForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  // Gather data from the form
  const payload = {
    property_id: parseInt(document.getElementById('propertyId').value, 10),
    client_name: document.getElementById('clientName').value,
    client_email: document.getElementById('clientEmail').value,
    preferred_time: document.getElementById('preferredTime').value,
  };
  // Send the scheduling request to the backend
  const res = await fetch('http://localhost:5000/schedule', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const data = await res.json();
  if (!res.ok) {
    confirmation.hidden = false;
    confirmation.textContent = data.error || 'An error occurred.';
    return;
  }
  confirmation.hidden = false;
  confirmation.textContent = data.message;
  // Hide form after successful booking
  scheduleForm.hidden = true;
});