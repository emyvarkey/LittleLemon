from restaurant.models import  Menu

# Create menu items for Soups
Menu.objects.create(title='Chicken Creamy Baby Corn Soup', price=6.99, inventory = 50)
Menu.objects.create(title='Chicken Manchow Soup', price=6.99, inventory = 50)
Menu.objects.create(title='Hot And Sour Veg Soup', price=5.99,inventory = 50)

# Create menu items for Veg Appetizers
Menu.objects.create(title='Baby corn 65', price=11.99, inventory = 50)
Menu.objects.create(title='Baby corn Manchuria', price=11.99,inventory = 50)
Menu.objects.create(title='Crispy Corn 65', price=10.99, inventory = 50)

# Create menu items for Non-Veg Appetizers
Menu.objects.create(title='Chicken Lollipops', price=15.99, inventory = 50)
Menu.objects.create(title='Vanjaram Fish Fry', price=18.99, inventory = 50)
Menu.objects.create(title='Chili Chicken', price=14.99, inventory = 50)

Menu.objects.create(title='Channa Masala', price=13.99, inventory = 50)
Menu.objects.create(title='Daal Makhani', price=14.99,inventory = 50)

# Create menu items for Chicken Curries
Menu.objects.create(title='Achari Chicken Masala', price=15.99,inventory = 50)
Menu.objects.create(title='Butter Chicken', price=15.99,inventory = 50)
Menu.objects.create(title='Chicken Korma', price=15.99, inventory = 50)

# Create menu items for Rice and Noodles
Menu.objects.create(title='Egg Fried Rice', price=15.99,inventory = 50)
Menu.objects.create(title='Chicken Fried Rice', price=16.99, inventory = 50)
Menu.objects.create(title='Hakka Paneer Veg Noodles', price=16.99,inventory = 50)

# Create menu items for Biryani
Menu.objects.create(title='Chicken Biryani', price=18.99, inventory = 50)
Menu.objects.create(title='Beef Biryani', price=19.99, inventory = 50)
Menu.objects.create(title='Fish Biryani', price=18.99,inventory = 50)

# Create menu items for Tandoori and Grill
Menu.objects.create(title='Masala Papad (2 Pieces)', price=7.99,inventory = 50)
Menu.objects.create(title='Tandoori Chicken', price=23.99, inventory = 50)
Menu.objects.create(title='Tandoori Goat Chops', price=23.99,inventory = 50)

# Create menu items for Naan and Roti
Menu.objects.create(title='Paneer Kulcha', price=5.99, inventory = 50)
Menu.objects.create(title='Butter Naan', price=5.99, inventory = 50)
Menu.objects.create(title='Tandoori Roti', price=4.99,inventory = 50)

# Create menu items for Desserts
Menu.objects.create(title='Carrot Halwa', price=4.99,inventory = 50)
Menu.objects.create(title='Kulfi Mango', price=5.99, inventory = 50)
Menu.objects.create(title='Pineapple Souffle', price=6.99, inventory = 50)

# Create menu items for Beverages
Menu.objects.create(title='Coke', price=2.49, inventory = 100)
Menu.objects.create(title='Sprite', price=2.49,inventory = 100)
Menu.objects.create(title='Sweet Tea', price=4.99, inventory = 100)




print("Database populated successfully!")

