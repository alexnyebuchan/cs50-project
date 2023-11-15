function updateLarder() {
  var selectedOption = document.getElementById('larderSuggestions').value;
  var list = document.getElementById('ingredientList');
  list.innerHTML = '';

  var ingredients = [];

  switch (selectedOption) {
    case 'oils':
      ingredients = [
        'Olive oil',
        'Coconut oil',
        'Vegetable Oil',
        'Balsamic vinegar',
        'Apple cider vinegar',
        'White wine vinegar',
      ];
      break;
    case 'herbs':
      ingredients = [
        'Basil',
        'Oregano',
        'Thyme',
        'Rosemary',
        'Cumin',
        'Parpika',
        'Chili Powder',
        'Garlic Powder',
        'Curry Powder',
        'Ground Cinnamon',
        'Bay Leaves',
      ];
      break;
    case 'cans':
      ingredients = [
        'Canned beans',
        'Chickpeas',
        'Canned tomatoes',
        'Tomato paste',
        'Canned tuna',
        'Canned salmon',
        'Canned corn',
        'Canned vegetables',
        'Canned fruit',
      ];
      break;
    case 'grains':
      ingredients = [
        'Rice',
        'Quinoa',
        'Lentils',
        'Pasta',
        'Couscous',
        'Barley',
        'Rolled oats',
      ];
      break;
    case 'flour':
      ingredients = [
        'All-purpose flour',
        'Whole wheat flour',
        'Baking powder',
        'Baking soda',
        'Cornstarch',
        'Yeast',
        'Cocoa powder',
        'Vanilla extract',
      ];
      break;
    case 'nuts':
      ingredients = [
        'Almonds',
        'Walnuts',
        'Pecans',
        'Cashews',
        'Peanuts',
        'Chia seeds',
        'Flaxseeds',
        'Sunflower seeds',
      ];
      break;
    case 'sauces':
      ingredients = [
        'Soy sauce',
        'Worcestershire sauce',
        'Hot sauce',
        'Ketchup',
        'Mustard',
        'Mayonnaise',
        'Honey',
        'Maple syrup',
      ];
      break;
    case 'jars':
      ingredients = [
        'Pickles',
        'Olives',
        'Capers',
        'Roasted red peppers',
        'Salsa',
        'Marinara sauce',
      ];
      break;
    case 'fruits':
      ingredients = ['Raisins', 'Cranberries', 'Apricots', 'Dates'];
      break;
    case 'misc':
      ingredients = [
        'Stock or bouillon',
        'Coconut',
        'Popcorn kernels',
        'Tea bags',
        'Sugar',
        'Salt',
      ];
      break;
    default:
      ingredients = ['No ingredients available'];
  }

  ingredients.forEach(function (ingredient) {
    var listItem = document.createElement('li');
    listItem.textContent = ingredient;
    listItem.classList.add('ingredientItem');
    list.appendChild(listItem);
  });

  var listItems = document.querySelectorAll('#ingredientList li');
  listItems.forEach(function (listItem) {
    listItem.addEventListener('click', function () {
      var textarea = document.getElementById('larder');
      var ingredientText = this.textContent;
      var currentText = textarea.value.trim();

      if (currentText !== '') {
        textarea.value = currentText + ', ' + ingredientText;
      } else {
        textarea.value = ingredientText;
      }
    });
  });
}

document
  .getElementById('larderSuggestions')
  .addEventListener('change', updateLarder);

updateLarder();
