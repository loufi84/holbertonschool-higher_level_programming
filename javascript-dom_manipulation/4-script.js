const addItem = document.getElementById('add_item');
const list = document.querySelector('.my_list');

addItem.addEventListener('click', () => {
  const newListElem = document.createElement('li');
  newListElem.textContent = 'Item';
  list.appendChild(newListElem);
});
