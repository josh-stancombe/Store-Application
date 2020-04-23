# ---------------------------- Global Variables & Products --------------------------
#Global variables
run = True 
cart = []

# Products table = Code : Name : Price 
prod1 = ["fr1", "fruit tea", round(3.11,2)]
prod2 = ["sr1", "strawberries", round(5.00,2)]
prod3 = ["cf1", "coffee", round(11.23,2)]

# ------------------------------------- Functions ------------------------------------
# 1. Initialisation 
def init():
    while run:

        # User Input:
        print("")
        selection = str(input("> "))
        print("")

        # Match product codes to names (for easier sorting):
        if selection in (prod1[0], prod2[0], prod3[0]) :
            if selection == prod1[0]:
                selection = prod1[1]
            if selection == prod2[0]:
                selection = prod2[1]
            if selection == prod3[0]:
                selection = prod3[1]

        # Add product to cart array:
        if selection in (prod1[1], prod2[1], prod3[1]) :
            cart.append(selection)
            print("Thanks - You've added", selection)

        # Delete a product from the cart array 
        elif selection ==  "remove" :
            delItem = input("Please type the name of the item you want to remove: ") 
            
            # Ensure there is at least 1 of the item in the basket: 
            if cart.count(delItem) > 0 :
                cart.remove(delItem)
                print("\nOK,", delItem, "has been removed from your cart.")

            else :
                print("\nSorry, you don't have any", delItem, "in your cart!")

        # View the cart:
        elif selection == "cart" : 
            # Call the cartItems function:
            p1Count, p2Count, p3Count = cartItems()

            # Display the contents:    
            print("OK, your cart is currently: \n")
            print("|", "Product".ljust(12), "|", "Qty".ljust(3))
            print("- - - - - - - - - - -")
            print("|", prod1[1].ljust(12), "|", str(p1Count).ljust(3))
            print("|", prod2[1].ljust(12), "|", str(p2Count).ljust(3))
            print("|", prod3[1].ljust(12), "|", str(p3Count).ljust(3))

        # Checkout 
        elif selection == "checkout" :
            checkout()
        
        # View Products
        elif selection == "products" :
            products()

        # Exit Application:
        elif selection == "exit" :
            print("Thanks for visting, come again. \n")
            input("\nPress the return key to exit.")
            exit() 

        # Anything else:
        else :
            print("Sorry, I didn't recognise that... Try again")

# 2. Welcome Message:
def welcomeMSG():

    # Display inital Welcome Message:
    print("Welcome to the Supermarket! \n")

    # Display current products:
    products()

    # Display promotion message:
    print("""\n Current Promotions: \n- Fruit Tea: Buy-One-Get-One-Free  \n- Strawberries: When you buy 3 or more, then the price per box is £4.50. """)

    # Display instructions message:
    print("""\n Intructions:   \n\n- Please type the name of a product or product code to add it to your cart.    \n- Type 'cart' to see the curent contents of your cart.    \n- Type 'products' to see the list of our products.    \n- Type 'remove' to remove a product from your cart.   \n- Type 'exit' to leave the shop.    \n- Type 'checkout' to checkout.     """)

# 3. Products definition function (showing what products are available):
def products():
    print("We sell the following products: \n""")
    print("|","code".ljust(4), "|", "product".ljust(12), "|", "price".ljust(5))
    print("- - - - - - - - - - - - - - - - ")
    print("|", prod1[0].ljust(4), "|", prod1[1].ljust(12), "|", "£", prod1[2])
    print("|", prod2[0].ljust(4), "|", prod2[1].ljust(12), "|", "£", prod2[2])
    print("|", prod3[0].ljust(4), "|", prod3[1].ljust(12), "|", "£", prod3[2])

# 4. Cart Items:
def cartItems():

    # Calculate products in the cart.
    p1Count = cart.count(prod1[1]) 
    p2Count = cart.count(prod2[1]) 
    p3Count = cart.count(prod3[1])
    return p1Count,p2Count,p3Count

#5. Checkout:
def checkout() :    
    
    # Retrieve product counts from cartItems function.
    p1Count, p2Count, p3Count = cartItems()
    
    # Calculate the product totals.
    p1Total = (p1Count * prod1[2])
    p2Total = (p2Count * prod2[2])
    p3Total = (p3Count * prod3[2])
    total  = (p1Total + p2Total + p3Total)

    # Checkout message.
    print("--------------------- C H E C K O U T ---------------------\n")
    print("Your Cart: \n")

    print("  |", "Product".ljust(12), "|", "Qty".ljust(3), "|", "Price ".ljust(7), "|", "Total".ljust(4))
    print("  - - - - - - - - - - - - - - - - - - - - -")
    print("  |", prod1[1].ljust(12), "|", str(p1Count).ljust(3), "|", "£", str(prod1[2]).ljust(5), "|", "£", p1Total)
    print("  |", prod2[1].ljust(12), "|", str(p2Count).ljust(3), "|", "£", str(prod2[2]).ljust(5), "|", "£", p2Total)
    print("  |", prod3[1].ljust(12), "|", str(p3Count).ljust(3), "|", "£", str(prod3[2]).ljust(5), "|", "£", p3Total)
    
    # Promotions.
    print("\nPromotions applied:") 
    totDiscount = promotions(p1Count, p2Count, p3Count)

    # Final total calculation.
    finalTotal = total - totDiscount

    # Final total message.
    print("\nTotal:")
    print("  - Cart Total: £", total)
    print("  - Promo Total: - £", totDiscount,"\n")
    
    print("------------------------------")
    print("  Your Final Total: £", finalTotal)
    print("------------------------------")

    # Thank you message
    print("\n\nThank you for shopping at our store. Please come again!")
    input("\nPress the return key to exit.")
    exit()


#6. Promotions:
def promotions(p1Count, p2Count, p3Count):

    # Promo 1: Fruit Tea BOGOF Offer.
    if p1Count >= 2 :
        discount1  = int(p1Count / 2) * prod1[2]
        print("  - Fruit Tea BOGOF promotion: - £", discount1)
    else:
        discount1 = 0

    # Promo 2: Strawberries Bulk Purchase Offer (3+ then price = £4.50 each). 
    if p2Count >= 3 :
        discount2 = p2Count * 0.5  #(50p per pack of strawberries)
        print("  - Strawberries bulk purchase promotion: - £", discount2)
    else :
        discount2 = 0

    # Calculate final discount.
    totDiscount = round(discount1 + discount2, 2)

    # Display 'None' if no promotions are applied.
    if totDiscount == 0 : 
        print("  - None")

    return totDiscount

# ----------------------------------- Calling Functions ----------------------------------
welcomeMSG()
init()