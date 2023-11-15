function addPerishable() {
  const perishableItems = document.querySelectorAll('.perishable');

  perishableItems.forEach((item) => {
    item.addEventListener('click', function () {
      const ingredientsInput = document.getElementById('ingredients');
      ingredientsInput.value += `${item.textContent}, `;
    });
  });
}

document.addEventListener('change', addPerishable);

addPerishable();
