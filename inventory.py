
"""
A programe to display a menu of which the user will make selections and then
the user can perform differnt operations
"""


class Shoe:

    '''
   initialising the following attributes:
    ● country,
    ● code,
    ● product,
            ● cost, and
    ● quantity.
    '''

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
      
    def get_cost(self):  
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
       This code is to return the quantity of the shoes.
        '''
        return self.quantity
                        
    # Add a code to returns a string representation of a class.
    def __str__(self):
        return (f"Country: {self.country}, "
                f"Code: {self.code}, "
                f"Product: {self.product}, "
                f"Cost: {self.cost}, "
                f"Quantity: {self.quantity}, ")
       
# =============Shoe list===========


shoe_list = []


def read_shoes_data():
    '''
    The list will be used to store a list of objects of shoes.
    '''
    try:
        with open("inventory.txt", "r") as file:
            next(file)
         
            for line in file:
                line = line.strip()

                if not line:  # Skip blank lines
                    continue

                parts = line.split(",")

                country, code, product, cost, quantity = parts

                shoe = Shoe(
                        country,
                        code,
                        product,
                        float(cost),    # floating cost
                        int(quantity)   # turnig quantity to interger
                    )

                shoe_list.append(shoe)

                print(shoe)

    except FileNotFoundError:
        print("inventory.txt not found.")


# ==========Functions outside the class==============


def capture_shoes():

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = float(input("Cost: "))
    quantity = int(input("Quantity: "))
 
    shoe = Shoe(country, code, product, cost, quantity)

    shoe_list.append(shoe)

    with open("inventory.txt", "a") as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")
   

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. 
    '''
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. The user should enter 
    R to re-stock.Then the quantity would be updated on the file for the 
    selected shoe.
    '''
   
    lowest = min(shoe_list, key=lambda shoe: shoe.quantity)

    print("Lowest stock:")
    print(lowest)
    print()
    restock = input("Please enter (r or R) to re-stock: ").capitalize()
    if restock == "R":
        num = int(input("input numbers of shoes: "))
        lowest.quantity += num
       
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")

            for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},"
                    f"{shoe.quantity}\n"
                )

        print(f"{num} shoes has been successfully added ")


def search_shoe():
    '''
        This function will search for a shoe from the list
        using the shoe code and return this object so that it will be printed.
    '''
    code = input("Enter shoe code: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)


def value_per_item():
    '''
        This function will calculate the total value for each item.
        and Print this information on the console for all the shoes.
    '''
    print("Tolal value per item:\n")
    for item_value in shoe_list:
        total_value = item_value.get_cost() * item_value.get_quantity()
        
        print(f"{item_value.product}: {total_value}")

    '''
    This code is to determine the product with the highest quantity.
    '''


def highest_qty():
    highest = max(shoe_list, key=lambda shoe: shoe.quantity)
    print("Highest stock item:")
    print(highest)

# ==========Main Menu=============
    '''
    A menu that executes each function above.
  
    '''


while True:

    print("\nMenu")
    print("1. Read shoes data")
    print("2. Capture shoes")
    print("3. View all")
    print("4. Re-stock")
    print("5. Search shoe")
    print("6. Value per item")
    print("7. Highest quantity")
    print("8. Exit")

    select = input("Choose an option: ")

    if select == "1":
        read_shoes_data()

    elif select == "2":
        capture_shoes()

    elif select == "3":
        view_all()

    elif select == "4":
        re_stock()

    elif select == "5":
        search_shoe()

    elif select == "6":
        value_per_item()

    elif select == "7":
        highest_qty()

    elif select == "8":
        print("Exiting")
        break

    else:
        print("Invalid option.")

