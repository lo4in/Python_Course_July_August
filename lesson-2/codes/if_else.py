#IF/ELIF/ELSE Statements

# x = float(input("Enter number: "))

# if x > 0:
#     print(f"{x} is positive")
# elif x < 0:
#     print(f"{x} is negative")
# else:
#     print("is zero", x)


#   == , >, < , <=, >=, != 
#   and, or     
#   in, not 
#



# a = int(input("Enter a: "))
# b = int(input("Enter b:"))


# if a == 1 and b != 1:
#     print(f"A is 1 and B is 1 ")
# elif a == 0 or b == -1:
#     print("A is zero b is -1")
# else:
#     print("erro")

text = "Mening ismim Lochinbek, Men 19 yoshdaman va men Toshkentdanman"
city = "Toshkent"

if city in text and "19" in text:
    print(f"User is from {city}")
    print("User is 19 year")
else:
    print("User is not from TSH and not 19 y. o.")