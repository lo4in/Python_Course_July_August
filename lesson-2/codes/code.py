#String methods in Pyhton

#Caption sensative

a = 1
b = 5


print(a < b)



text = "   ---Hello, World---   "

print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.strip())
print(text.replace("World", "Python"))
print(len(text))

txt = '   -Hello python    '
print(txt.replace("-", "").split())



#Example 


sent = input("Gap kiriting: ")
count = len(sent.strip().replace("!", "").split())
print(count)


