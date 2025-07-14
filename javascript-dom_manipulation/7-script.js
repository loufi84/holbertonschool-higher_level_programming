document.addEventListener('DOMContentLoaded', () => {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  // Transform the response in json
    .then(response => response.json())
    .then(data => {
      const listMovies = document.getElementById('list_movies');
      // Looping through the data to get all movies titles
      data.results.forEach(film => {
        const li = document.createElement('li');
        li.textContent = film.title;
        listMovies.appendChild(li);
      });
    })
    .catch(error => {
      console.error('Error while fetching datas :', error);
    });
});
