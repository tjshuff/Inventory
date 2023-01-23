# Defining shoe class.
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return(f"Country: {self.country} | Product Code: {self.code} | Shoe: {self.product} | Cost: R{self.cost} | Stock: {self.quantity}")
    def return_string(self):
        return(f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}")

# Blank list.
inventory_list = []

# Initializes data into list. Runs at the start of program.
def read_shoes_data():
    with open("inventory.txt", "r") as file:
        next(file)
        shoe_data_list = file.read().splitlines()
        for lines in shoe_data_list:
            lines_list = lines.split(",")
            shoe_data = Shoe(lines_list[0], lines_list[1], lines_list[2], lines_list[3], lines_list[4])
            inventory_list.append(shoe_data)

# Add new shoe data. Writes to inventory.txt file.
def capture_shoes():
    country_input = input("Enter the country: ")
    product_code_input = input("Enter the prodcut code: ")
    product_input = input("Enter the shoe model: ")
    cost_input = int(input("Enter the shoe cost: "))
    stock_input = int(input("Enter the current stock level: "))

    with open("inventory.txt", "a") as file:
        file.write(f"\n{country_input},{product_code_input},{product_input},{cost_input},{stock_input}")
    read_shoes_data()
    menu()

# Show all inventory.
def view_all():
    for data in inventory_list:
        print(Shoe.__str__(data))
    menu()

# Function to allow users to display the lowest stock in the inventory, and update stock with whatever number they choose
# Writes data to inventory.txt and re-reads eveything into inventory_list
def re_stock():
    list_of_quantities = []
    for shoe in inventory_list:
        quantities = shoe.get_quantity()
        list_of_quantities.append(int(quantities))
    minimum_quantities = min(list_of_quantities)

    for shoe in inventory_list:
        if shoe.quantity == str(minimum_quantities):
            print(f"""The shoe with the lowest stock is:
{shoe}""")

            while True:
                try:
                    user_input = int(input("Please enter the amount you would like to restock this shoe by: "))
                except:
                    ValueError
                    print("Please enter a number!")
                break
            shoe_qnty_int = int(shoe.quantity)
            shoe_qnty_int += user_input
            shoe_qnty_int = str(shoe_qnty_int)
            shoe.quantity = shoe_qnty_int
            print(f"""Stock updated for : 
{shoe}""")
    with open("inventory.txt", "w") as file:
        for shoe in inventory_list:
            file.write(shoe.return_string()+"\n")
    menu()

# Function to allow users to search for a show using an SKU code.
def search_shoe():
    user_selection = input("Enter the product code you would like to search: ")
    search_result = [shoe for shoe in inventory_list if shoe.code == user_selection]
    for data in search_result:
        print(Shoe.__str__(data))
    menu()


# Function to display inventory data with total costs calculated.
def value_per_item():
    for shoe in inventory_list:
        shoe_inventory_int = int(shoe.quantity)
        shoe_cost_int = int(shoe.cost)
        shoe_total_cost = shoe_cost_int * shoe_inventory_int
        print(f"{shoe.product} | Quantity: {shoe.quantity} | Cost per item: {shoe.cost} | Total Inventory cost = {shoe_total_cost}")
    menu()

# Highest quantity function. Reads all data from inventory list and prints highest stock level.
def highest_qty():
    list_of_quantities = []
    for shoe in inventory_list:
        quantities = shoe.get_quantity()
        list_of_quantities.append(int(quantities))
    minimum_quantities = max(list_of_quantities)

    for shoe in inventory_list:
        if shoe.quantity == str(minimum_quantities):
            print(f"""The shoe with the highest stock is:
{shoe}""")
            print(f"{shoe.product} should be put on sale!")

    menu()


# Defining menu function.
def menu():
    print("""
    """)
    print("""--- Welcome to Nike International Warehouse Inventory Management System ---

                Please select from the following menu options""")

    print("""
1 - Add new stock to manifest
2 - View all current stock globally
3 - View the lowest stock levels, and re-stock
4 - View the highest stock levels
5 - See stock cost per item
6 - Search for an Item
0 - Exit program""")

    while True:
        try:
            user_selection = int(input("Selection: "))
        except:
            ValueError
            print("Please enter a valid number.")
        if user_selection == 1:
            capture_shoes()
        elif user_selection == 2:
            view_all()
        elif user_selection == 3:
            re_stock()
        elif user_selection == 4:
            highest_qty()
        elif user_selection == 5:
            value_per_item()
        elif user_selection == 6:
            search_shoe()
        elif user_selection == 0:
            print("Goodbye!")
            exit()
        else:
            print("Please enter a valid selection.")


# Initializing Data!
read_shoes_data()

# Call menu function.
menu()
