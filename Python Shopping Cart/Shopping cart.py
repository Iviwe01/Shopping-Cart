import csv

count_order = 1   # my order id will start at 1

products = {         # This is a dictionary that will hold all my products and their prices
    'monster': 22,
    'score': 12,
    'redbull': 17,
    'prime': 55,
    'switch': 10
}


def write_transaction_to_csv(order_id, cart, total_cost_before_tax, total_cost_after_tax, discount_code):  # Function to link python and csv file
    filename = "shopping cart orders.csv"  # This is the name of the file where the orders will be recorded
    with open(filename, 'a', newline='') as csvfile:  # 'a' is append which allows for new orders to be added without overriding the existing ones
        fieldnames = ['Order ID', 'Product', 'Price', 'Tax', 'Discount Code']  # Field names for the CSV file
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:  # This will check if there is any existing orders in the file, if not it will write the header row
            writer.writeheader()
            writer.writerow({})


        writer.writerow({'Order ID': order_id})  # Write the unique order id for each order
        for item in cart:  # This will write each item in the cart in the csv file
            writer.writerow({'Product': item.capitalize(), 'Price': products[item]})
        writer.writerow({'Product': 'Total Cost Before Tax', 'Price': f"R{total_cost_before_tax:.2f}"})
        writer.writerow({'Product': 'Tax (15%)', 'Price': f"R{total_cost_after_tax - total_cost_before_tax:.2f}"})
        writer.writerow({'Product': 'Total Cost After Tax', 'Price': f"R{total_cost_after_tax:.2f}"})
        writer.writerow({'Product': 'Discount Code', 'Price': discount_code})


cart = []     # This is a list that will contain the choices of the consumer
total_cost = 0

while True: # Loop so that customer can choose again.
    print("\nThese are the products in store:")   # This will let the user know the items in store and their prices
    for product, price in products.items():
        print(f"{product.capitalize()}: R{price}") # Capitalize the first letter of my products to make it look more appealing


    choice = input("\nPlease select an item you want to buy (or type 'q' to exit transaction): ").lower()

    if choice == 'q': # the 'q' will give the user the option to exit the transaction when done
        break
    elif choice in products:
        cart.append(choice)
        total_cost += products[choice]
        print(f"{choice.capitalize()} added to your shopping cart.") # after choosing an item, this will show the user which product was selected
    else:
        print("Invalid item, Please choose a product in the store.")


    discount_code = input("\nPlease enter a discount code (if none enter 'none'): ").lower()  # This code will allow the user to insert the discount promo
    discount_rate = 0



    if discount_code == 'ifs354': # This if statement will check if the promo is valid or not, if it is it will add the discount and if its not it wont.
        discount_rate = 0.25
        total_cost *= (1 - discount_rate)
        print("Congrats, You have been awarded a 25% off with your promo code.")
    elif discount_code != 'none':
        print('Invalid promo, No discount has been added to total cost.')


    total_cost_after_tax = total_cost + total_cost * 0.15 # 15% S.A tax
    print("\nOrder details have been written to CSV file.") # This will print the details of the order(s)
    write_transaction_to_csv(count_order, cart, total_cost, total_cost_after_tax, discount_code) # This will write the attributes of the order(s)


    print("\nItems Purchased: ") # This will show the items in the cart.
    for item in cart:
        print(item.capitalize())

    print(f"\nTotal cost before tax: R{total_cost:.2f}") # This will show total cost before tax is deducted

    print(f"\nTotal cost after tax: R{total_cost_after_tax:.2f}") # This will show total cost after the tax deduction

    count_order += 1  # This will create a new unique id for every order
