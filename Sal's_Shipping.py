weight =  41.6 #Change this variable.
cost = 0
drone_cost = 0
cost_of_premium_ground_shipping = 125

#ground-shipping
if weight <= 2:
  cost =  (weight * 1.50) + 20
elif weight > 2 and weight <= 6:
  cost = (weight * 3.00) + 20
elif weight > 6 and weight <= 10: 
  cost = (weight * 4.00) + 20
elif weight > 10:
  cost = (weight * 4.75) + 20

#drone shipping
if weight <= 2:
  drone_cost =  weight * 4.50
elif weight > 2 and weight <= 6:
  drone_cost = weight * 9.00
elif weight > 6 and weight <= 10: 
  drone_cost = weight * 12.00
elif weight > 10:
  drone_cost = weight * 14.25

print("Ground Shipping: $", cost)
print("Ground Premium Shopping: $",cost_of_premium_ground_shipping)
print("Drone shipping: $", drone_cost)

