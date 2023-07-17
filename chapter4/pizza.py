pizza_list = ['pepperoni', 'cheese', 'sausage']
for pizza in pizza_list:
    print(f"I like {pizza} pizza.")
print("I really love pizza!")

frined_pizza = pizza_list[:]
pizza_list.append('mushroom')
frined_pizza.append('pineapple')
print(pizza_list)
print(frined_pizza)