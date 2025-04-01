# shopping cart program
foods = []
prices = []
food = []
price = []
total = 0

while True:
    food = input("Enter the food (press q to quit): ")
    if food.lower() == "q":
         break
    else:
        price = float (input(f"Enter the price :$ {food}: "))
        foods.append(food)
        prices.append(price)

print("----YOUR ORDER-----")
for food in foods:
    print(food,end=" ")
for price in prices:
    total += price
print()
print(f"Your total $ {total}")










