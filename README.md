Shopping Cart Application
A Python-based shopping cart system that allows users to add, remove, and manage items. This application simulates a simple retail environment where users can select items, view their cart, and see the total price of the selected items.

Features
Add Items to Cart: Select products to add to the cart.
Remove Items from Cart: Remove unwanted products from the cart.
View Cart: Display all items currently in the shopping cart.
Calculate Total Price: Automatically calculate the total price of items in the cart.
Clear Cart: Option to clear all items from the cart and start fresh.
Technologies Used
Python 3.x: Core programming language used for the application.
Setup Instructions
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/shopping-cart.git
Open the project folder:
bash
Copy code
cd shopping-cart
Run the Python script to start the application:
bash
Copy code
python ShoppingCart.py
How to Use
Add items: Users will be prompted to add items by entering the item name and price.
Remove items: Users can remove an item by entering its name.
View cart: Users can display all current items in the cart, along with their prices.
View total price: The total price of all items in the cart is displayed.
Clear cart: Users can reset the cart to remove all items at once.
Example Usage
python
Copy code
Enter command: Add
Enter item name: Apple
Enter item price: 1.99

Enter command: Add
Enter item name: Bread
Enter item price: 2.50

Enter command: View
Items in cart:
1. Apple - $1.99
2. Bread - $2.50
Total price: $4.49

Enter command: Remove
Enter item name: Bread
Item removed.

Enter command: View
Items in cart:
1. Apple - $1.99
Total price: $1.99

Enter command: Clear
Cart has been cleared.
Future Improvements
Add the ability to apply discount codes or promotions.
Implement a graphical user interface (GUI) for better user experience.
Enhance the system to handle product categories and quantities.
License
This project is licensed under the MIT License.
