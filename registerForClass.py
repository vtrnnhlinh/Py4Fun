experience = input("What is your Spanish level? ")
if experience == "none":
    print("You should take Spanish 101")
elif experience == "101":
    print("You should take Spanish 102")
elif experience == "102":
    print("You should take Spanish 201")
elif experience == "201":
    print("You should take Spanish 202")
elif experience == "202":
    print("You should take advanced classes!")
else:
    print("Sorry we can't recognize what you entered.")
    print("Please enter 'none', '101', '102', '201', or '202'")