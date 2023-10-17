import time

class Dict_create(dict):
    def __init__(self) -> None:
        self = dict()
    def add(self, key, value):
        self[key] = value
    
    def checkout():
        i = True
        while i == True:
            card_num = input("Please enter debit or credit card number: \n")
            exp_date = input("Enter card expiration date in (ex: 01/25) format: \n")
            name = input("Please enter the name as shown on card: \n")
            code = input("Please enter 3-digit security code: \n")
            if len(card_num) != 16:
                print("Please enter a valide card number")
                i = True
                
        

def my_cart():
    """Creates a counter to keep track of
    how times a fruit was added to the basket
    """
    inventory = {"Fruit": ["Apple", "Orange", "Pineapple", "Pear", "Cherry", "Watermelon", 
                           "Mango", "Berry", "Blueberry", "Nectarine", "Blackberry", "Peach", 
                           "Grape", "Grapefruit", "Strawberry", "Kiwi", "Papaya"], 
                "Kitchen": ["Spoon", "Fork", "Knife", "Pot", "Plate", "Bowl", "Cup", "Refrigerator", 
                            "Microwave", "Oven", "Pantry"], 
                "Bathroom": ["Soap", "Toothbrush", "Comb", "Towel", "Toilet Paper", "Hairspray", 
                             "Shampoo", "Conditioner", "Hand Soap"], 
                "Bedroom": ["Mattress", "Lamp", "Sheets", "Curtains", "Pillow", "Dresser", "Hanger", 
                            "Hamper", "Closet"], 
                "Living room": ["Television", "Couch", "Rug", "Blanket", "Fan", "Lamp", "Chair", "Desk", "Ottoman", 
                                "Remote", "Bookshelf", "Book"], 
                "Food": ["Pasta", "Bread", "Cheese", "Cereal", "Milk", "Water", "Lettuce", "Tomato",
                         "Ice Cream", "Mushrooms", "Tofu", "Beans", "Rice", "Coffee", "Juice", "Chips",
                         "Crackers", "Nuts", "Hamburger", "Granola"]}
    
    print("Welcome! Let's pick out some items to add to your cart!")
    time.sleep(2)
    print("Here are the categories: ")
    time.sleep(1.5)
    for k, v in inventory.items():
        print(k)
    category = input("Choose a category: ").capitalize()
    if category == "Fruit":
        print("Here are the fruits we have in stock: ")
        fruit_vals = inventory["Fruit"]
        print(*fruit_vals, sep=', ')
    elif category == "Kitchen":
        print("Here are the kitchen items we have in stock: ")
        kitchen_vals = inventory["Kitchen"]
        print(*kitchen_vals, sep='\n')
    elif category == "Bathroom":
        print("Here are the bathroom items we have in stock: ")
        bathroom_vals = inventory["Bathroom"]
        print(*bathroom_vals, sep='\n')
    elif category == "Bedroom":
        print("Here are the bedroom items we have in stock: ")
        bedroom_vals = inventory["Bedroom"]
        print(*bedroom_vals, sep='\n')
    elif category == "Living room":
        print("Here are the living room items we have in stock: ")
        living_room_vals = inventory["Living room"]
        print(*living_room_vals, sep='\n')
    elif category == "Food":
        print("Here are the food items we have in stock: ")
        food_vals = inventory["Food"]
        print(*food_vals, sep='\n')
    else:
        time.sleep(1)
        print("Sorry, that is not in our category list.\nPlease check spelling and enter one of the category names.")
        return

    i = True
    basket = Dict_create()
    while i:
        product = input("Enter an item to add to the cart (or 'done' to finish): ").capitalize()
        default_num = 1
        if product in basket:
            for k, v in basket.items():
                if k == product:
                    basket[k] = v + 1
            i = True
        elif product != "done" and product in inventory[category] and product not in basket:
            basket.add(product, default_num)
            i = True
        elif product == "Done":
            print("Alright! Let's what we have in your cart!")
            time.sleep(2)
            for key, value in basket.items():
                print(f"item: {key} x {value}")
            time.sleep(1.5)
            print("Great! Now let's go checkout!")
            i = False
        else:
            print("Please enter a product in the given list.")
            i = True

my_cart()

