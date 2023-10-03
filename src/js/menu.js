const restaurantMenus = {
    restaurant1: [
        { name: 'Pasta Carbonara', price: 12.99 },
        { name: 'Margherita Pizza', price: 10.99 },
        { name: 'Grilled Salmon', price: 16.99 },
        { name: 'Caesar Salad', price: 8.99 },
    ],
    restaurant2: [
        { name: 'Sushi Platter', price: 22.99 },
        { name: 'Teriyaki Chicken', price: 15.99 },
        { name: 'Vegetable Tempura', price: 10.99 },
        { name: 'Miso Soup', price: 3.99 },
    ],
    // Add more restaurants and their menus as needed
};

// Function to generate the menu items based on the selected restaurant
function generateMenu() {
    const menuContainer = document.getElementById('menu');
    menuContainer.innerHTML = ''; // Clear existing content

    const selectedRestaurant = document.getElementById('restaurantSelect').value;
    const menuItems = restaurantMenus[selectedRestaurant];

    menuItems.forEach(item => {
        const menuItem = document.createElement('div');
        menuItem.classList.add('col-md-6', 'menu-item');

        menuItem.innerHTML = `
            <h3>${item.name}</h3>
            <p>${item.price.toFixed(2)} USD</p>
        `;

        menuContainer.appendChild(menuItem);
    });
}

// Load the menu when the page loads
window.addEventListener('load', generateMenu);

// Update the menu when the user selects a different restaurant
document.getElementById('restaurantSelect').addEventListener('change', generateMenu);
