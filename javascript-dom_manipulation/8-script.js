document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const hello = document.getElementById('hello');
      hello.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error while fetching datas :', error);
    });
});
