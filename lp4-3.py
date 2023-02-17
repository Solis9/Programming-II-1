eggs = int(input("Enter the number of eggs puchased: "))

dozen = eggs / 12
price = 0.0
if dozen > 0 and dozen < 4:
  price = 0.50
elif dozen >= 4 and dozen < 6:
  price = 0.45
elif dozen >= 6 and dozen < 11:
  price = 0.40
elif dozen >= 11:
  price = 0.35

else:
  print("The number of eggs is invalid")
print("Price per egg is: $" + str(price))
print("Total cost is: $" + str(price*dozen))