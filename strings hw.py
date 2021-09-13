#AlexLadin
#9/13/21
print("Hello")
print('Hello')
a="Hello"
print(a)

b="Hello, World!"
print(b[2:5])
b="Hello, World!"
print(b[:5])
b="Hello, World!"
print(b[2:])
b="Hello, World!"
print(b[-5:-2])

a="Hello, World!"
print(a.upper())
a="Hello, World!"
print(a.lower())
a="Hello, World!"
print(a.strip()) #returns "Hello, World!"
a="Hello, World!"
print(a.replace("H", "J"))
a="Hello, World!"
print(a.split(",")) #returns ['Hello', 'World!']

a="Hello"
b="World"
c=a+b
print(c)
a="Hello"
b="World"
c=a + " "+ b
print(c)

age=36
txt="My name is John, and i am {}"
print(txt.format(age))
quantity=3
itemno= 567
price=49.95
my order= "I want {} peices of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

txt="We are the so-called \"Vikings\" from the north."
