# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)

print("We sell", num_pizzas, "different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

print(pizza_and_prices)

pizza_and_prices = sorted(pizza_and_prices)
#print(pizza_and_prices) #check 1 

cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza) check 2
priciest_pizza = pizza_and_prices[6]
#print(priciest_pizza) check 3

pizza_and_prices.insert(4,[2.5, "peppers"])
#print(pizza_and_prices) check 4

three_chepeast = pizza_and_prices[:3]
print(three_chepeast) 
