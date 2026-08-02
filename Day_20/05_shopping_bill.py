product = input("Enter Product Name: ")
quantity = int(input("Enter the no. of quantity of product you buy: "))
price = int(input("Enter the price of that single product: "))

print(f"\n--Shopping Bill--\nProduct : {product}\nQuantity: {quantity}\nPrice   : ₹{price}\nTotal   : ₹{quantity * price}\n")