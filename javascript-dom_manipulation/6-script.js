document.addEventListener('DOMContentLoaded', () => {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    // Transform the response in json
    .then(response => response.json())
    .then(data => {
      // Add name datas from json objects fetched
      const char = document.getElementById('character');
      char.textContent = data.name;
    })
    // Try error recuperation for the first time
    .catch(error => {
      console.error('Error while fetching datas :', error);
    });
});
