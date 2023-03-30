items = int(input("Enter the number of items to be purchased: "))

price = 0.0
if items > 0 and items <= 99:
  price = 5.95
elif items > 100 and items <= 199:
  price = 5.75
elif items > 200 and items <= 299:
  price = 5.40
elif items >= 749:
  price = 5.15
else:
  print("The number of copies is invalid")
print("Price per item is: $" + str(price))
print("Total cost is: $" + str(price*items))