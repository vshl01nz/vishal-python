a = "Good afternoon, "
b = input("What is your name?")
a +=b
# c = a + b
print(a)
# print (c)

# f-string



website = "fun learning"
print(f"welcome to {website}")

words = ["We ", "are","learning","python"]
joined = "".join(words)
print(joined)

print(joined.upper())
print(joined.lower())

basket = ["banana", " strawberry", "kiwi"]
price = 3
text = "Welcome to the grocery, everything is {} dollars"
print(text.format(price))

quantity = 3
discountcode = 500

myorder = "I want {} pieces of item discount code of {} for {} dollars."
print(myorder.format(quantity, discountcode, price))
total = price * quantity
print(f"Total price: {total}")
print("Your item to delivery: {}".format(basket))