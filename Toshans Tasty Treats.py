# Name: Aryan Aggarwal, id: 898707
calories = 0
print("Welcome to Toshan's Tasty Treats!")
print("\n")
print("Burgers:\t\t\tSide Orders:")
print("********\t\t\t********")
print("1 - Cheeseburger\t\t1 - Fries")
print("2 - Fish Burger\t\t\t2 - Baked Potato")
print("3 - Veggie Burger\t\t3 - Chef Salad")
print("4 - no burger\t\t\t4 - no side order")
print("\n")
print("Drinks:\t\t\tDesserts:")
print("********\t\t********")
print("1 - Soft Drink\t\t1 - Apple Pie")
print("2 - Orange Juice\t2 - Cake")
print("3 - Milk\t\t3 - Fruit Cup")
print("4 - no drink\t\t4 - no dessert")
input("\nPlease take a moment to read our menu. Press enter to continue...")
print("\nPlease enter your menu selections below.")
print("Enter \"4\" if you do not want a particular item.")
print("\n")
burger = int(input("Burger choice: "))
sideorder = int(input("Side Order choice: "))
drink = int(input("Drink choice: "))
dessert = int(input("Dessert choice: "))

if burger == 1:
    burger = "Cheeseburger"
    calories += 721
elif burger == 2:
    burger = "Fish Burger"
    calories += 313
elif burger == 3:
    burger = "Veggie Burger"
    calories += 521
elif burger == 4:
    burger = "No Burger"
    calories += 0

if sideorder == 1:
    sideorder = "Fries"
    calories += 150
elif sideorder == 2:
    sideorder = "Baked Potato"
    calories += 60
elif sideorder == 3:
    sideorder = "Chef Salad"
    calories += 190
elif sideorder == 4:
    sideorder = "No Side Order"
    calories += 0

if drink == 1:
    drink = "Soft Drink"
    calories += 203
elif drink == 2:
    drink = "Orange Juice"
    calories += 101
elif drink == 3:
    drink = "Milk"
    calories += 102
elif drink == 4:
    drink = "No drink"
    calories += 0

if dessert == 1:
    dessert = "Apple Pie"
    calories += 367
elif dessert == 2:
    dessert = "Cake"
    calories += 466
elif dessert == 3:
    dessert = "Fruit Cup"
    calories += 75
elif dessert == 4:
    dessert = "No dessert"
    calories += 0
    
print("You ordered: ",burger,", ",sideorder,", ",drink,", ",dessert,".",sep = "")
print("Total calorie count is:",calories)