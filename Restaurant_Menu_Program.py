def menu_template():
    # dictionary with prices of all products in hierarchy
    all_prices = {
        '1': {'1': {'1': 361, '2': 409}, '2': {'1': 361, '2': 409}, '3': {'1': 361, '2': 409}, '4': {'1': 396, '2': 461}, '5': {'1': 396, '2': 461}, '6': {'1': 396, '2': 461}, '7': {'1': 396, '2': 461}, '8': {'1': 399, '2': 509}, '9': {'1': 399, '2': 509}},
        '2': {'1': {'1': 360, '2': 374}, '2': {'1': 360, '2': 374}, '3': {'1': 360, '2': 374}, '4': {'1': 360, '2': 374}, '5': {'1': 250, '2': 291}, '6': {'1': 250, '2': 291}, '7': {'1': 250, '2': 291}, '8': {'1': 250, '2': 291}, '9': {'1': 335, '2': 348}, '10': {'1': 335, '2': 361}, '11': {'1': 239, '2': 291}},
        '3': {'1': {'1': 348, '2': 365}, '2': {'1': 348, '2': 365}, '3': {'1': 348, '2': 400}},
        '4': {'1': {'1': 335, '2': 365}, '2': {'1': 335, '2': 365}, '3': {'1': 348, '2': 400}, '4': {'1': 348, '2': 400}}
    }
    item_price = all_prices[category][item]
    print("------------------------------------------------------")
    print("Choose a size:")
    print(" 1. Small \t 2. Regular")
    print(f" Rs. {item_price['1']}/- \t Rs. {item_price['2']}/-")
    size = input("You have chosen: ")
    print("------------------------------------------------------")
    quantity = int(input("How many would you like to order: "))
    if size == '1':
        return item_price['1'] * quantity
    else:
        return item_price['2'] * quantity


# defining a variable to calculate total cost of the items
cost = 0
while True:                               # applying a loop to run until user enters 'no' or 'N'
    print("------------------------------------------------------")
    print("Choose a Category:")
    # asking user to select a category
    print(" 1. Espresso & Mocha Chillers \n 2. Over Ice \n 3. Chocolate Chillers \n 4. Fusion ")
    category = input("You have chosen: ")
    print("------------------------------------------------------")

    if category == '1':
        print("Choose an Item:")
        # asking user to select an item
        print(" 1. Very Vanilla Chiller \n 2. Cocoa Loco \n 3. Cookies N Cream \n 4. Hazlenut Mocha Chiller \n 5. Chocolate Macadamia Chiller \n 6. Italian Chiller \n 7. Caramel Nut Chiller \n 8. Tiramisu Chiller \n 9. Toffee Nut Chiller")
        item = input(" You have chosen: ")
        cost += menu_template()

    elif category == '2':
        print("Choose an Item:")
        print(" 1. Signature Iced Coffee \n 2. Iced Mocha \n 3. Iced Caramel Latte \n 4. Iced Americano \n 5. Blueberry Lemonade \n 6. Lychee Lemonade \n 7. Green Apple Lemonade \n 8. Peach Lemonade \n 9. Apple Soda \n 10. Lime Soda \n 11. Iced Teas(Peach / Lemon Lychee)")
        item = input(" You have chosen: ")
        cost += menu_template()

    elif category == '3':
        print("Choose an Item:")
        print(
            " 1. Original Iced Chocolate \n 2. White Iced Chocolate \n 3. Chocolate Delight")
        item = input(" You have chosen: ")
        cost += menu_template()

    elif category == '4':
        print("Choose an Item:")
        print(
            " 1. Iced Lime \n 2. Apple Chiller \n 3. Chai Chiller \n 4. Green Tea Chiller")
        item = input(" You have chosen: ")
        cost += menu_template()

    option = input("Do you want to order anything else (Y/N): ")
    if option == 'N'.casefold() or option == "No".casefold():
        break


# service charge is equal to 7% of the cost of the customer
service_charge = cost * 0.07
# total tax is equal to 15% of the cost of the customer
total_tax = cost * 0.15
# total bill is the sum of the cost and the total tax and the service charge
total_cost = cost + total_tax + service_charge

print("The total cost/total bill is Rs. " + str(round(total_cost, 2)) + "/-")

# writing / appending the total bill in a txt file with context manager
with open("bill.txt", 'w') as bill:
    bill.write(f"Service Charges: Rs.{str(round(service_charge, 2))}/- \n")
    bill.write(f"Tax Charges: Rs.{str(round(total_tax, 2))}/- \n")
    bill.write(f"Total Bill: Rs.{str(round(total_cost, 2))}/- \n")
