
# Defining the variables and algorithms for adding stock 
def global  adding_stock():
    new_kits= int(input("Please enter the amount units received:"))
    starting_stock= 25
    current_stock= int( new_kits += starting_stock)
    print("The current stock we have is ",current_stock"units")

# Creating the function for evaluating and printing low stock orders 
def global low_stock():
    if current_stock < 10:
        print("THE STOCK IS LOW, PLEASE RE-ORDER!")

# Creating the function for letting the customers put in the quantities they want. 
def global customer_orders():
    place_order= int(input( in range(11)("Please enter the amount of quantities you want:")))

    if place_order > 10:
        print("You can only order maximun 10 units!!")  # Condition to print when customer order's over 10 products 

    stock_level= (current_stock -= place_order)   # Condition to check the level of the stock level 
    
    if stock_level < place_order:
        print("There is not enough stock available!!")


