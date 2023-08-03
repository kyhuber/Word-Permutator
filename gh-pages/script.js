// Function to handle the form submission and send data to the backend
async function handleSubmit(event) {
    event.preventDefault();
  
    const centerLetter = document.getElementById('centerLetter').value.trim().toLowerCase();
    const additionalLetters = document.getElementById('additionalLetters').value.trim().toLowerCase();
  
    // Prepare the data to be sent in the request body as JSON
    const data = {
      centerLetter: centerLetter,
      additionalLetters: additionalLetters
    };
  
    try {
      // Make a POST request to the backend API endpoint
      const response = await fetch('/find-permutations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
  
      // Parse the response JSON
      const result = await response.json();
  
      if (result.success) {
        // Display the sorted permutations on the frontend
        const permutationsList = document.getElementById('permutationsList');
        permutationsList.innerHTML = result.permutations.join(', ');
      } else {
        alert('Error: Permutations not found.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Error: Unable to process the request.');
    }
  }
  
  // Add an event listener to the form submit button
  const form = document.getElementById('permutationForm');
  form.addEventListener('submit', handleSubmit);  