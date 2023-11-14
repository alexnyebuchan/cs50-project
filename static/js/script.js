function updateList() {
  var selectedOption = document.getElementById('larderSuggestions').value;
  var list = document.getElementById('ingredientList');
  list.innerHTML = '';

  var ingredients = [];

  switch (selectedOption) {
    case 'oils':
      ingredients = [
        'Olive oil',
        'Coconut oil',
        'Balsamic vinegar',
        'Apple cider vinegar',
      ];
      break;
    case 'herbs':
      ingredients = ['Basil', 'Oregano', 'Thyme', 'Rosemary'];
      break;
    default:
      ingredients = ['No ingredients available'];
  }

  ingredients.forEach(function (ingredient) {
    var listItem = document.createElement('li');
    listItem.textContent = ingredient;
    list.appendChild(listItem);
  });
}

document
  .getElementById('larderSuggestions')
  .addEventListener('change', updateList);

updateList();
