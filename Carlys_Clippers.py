hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

#Prices and Cuts

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for cost in prices:
  total_price += cost 

# print(total_price) check 1 

average_price = total_price / len(prices)
print("Average Haircut Price: ", average_price)

new_prices = [cost - 5 for cost in prices]
print(new_prices)

#Revenue

total_revenue = 0 
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total Revenue:", total_revenue)

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(0, len(hairstyles)) if new_prices[i] < 30]

print(cuts_under_30)
