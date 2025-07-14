document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.getElementById('add_item');
  const removeItem = document.getElementById('remove_item');
  const clearList = document.getElementById('clear_list');
  const list = document.querySelector('.my_list');

  addItem.addEventListener('click', () => {
    const newListElem = document.createElement('li');
    newListElem.textContent = 'Item';
    list.appendChild(newListElem);
  });

  removeItem.addEventListener('click', () => {
    if (list.lastElementChild) {
      list.removeChild(list.lastElementChild);
    }
  });

  clearList.addEventListener('click', () => {
    list.innerHTML = '';
  });
});
