document.addEventListener('DOMContentLoaded', () => {
  const button = document.getElementById('btn_translate');
  const select = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');

  button.addEventListener('click', () => {
    const lang = select.value;
    if (!lang) return;

    fetch(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
      .then((response) => response.json())
      .then((data) => {
        helloDiv.textContent = data.hello;
      })
      .catch((error) => {
        console.error('Error fetching translation:', error);
        helloDiv.textContent = 'Error fetching translation.';
      });
  });
});
