x = 5
y = 1

# arithmetic operators
result = x + y + 2
print("Let's show x + y + 2 =", result)
print(type(result))
result = x - y - 2
print("Let's show x - y - 2 =", result)
print(type(result))
result = x * y * 2
print("Let's show x * y * 2 =", result)
print(type(result))
result = x / y / 2
print("Let's show x / y / 2 =", result)
print(type(result))
result = x % y
print("Let's show x % y =", result)
print(type(result))

# comparison operators
result = x > y  # should be True
print("Let's show x > y =", result)
print(type(result))
result = x < y  # should be False
print("Let's show x < y =", result)
print(type(result))
result = x == y # should be False
print("Let's show x == y =", result)
print(type(result))
result = x != y # should be True
print("Let's show x != y =", result)
print(type(result))
result = x >= y  # should be True
print("Let's show x >= y =", result)
print(type(result))
result = x <= y  # should be False
print("Let's show x <= y =", result)
print(type(result))


Hw = "Hello world!"
print(Hw)
print(len(Hw))
print(Hw[1])

print(Hw[7:])
print(Hw[-3:])
print(Hw[:5])
print(Hw[1:4])

x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

print(str(x) + str(y) + z)

print(6 > 5 and 10 > 20)
print(6 > 5 or 10 > 20)

print("casting numbers to bool...")
x = 0
print(bool(x))
x = -1
print(bool(x))
x = 1
print(bool(x))
x = 100
print(bool(x))
x = -100
print(bool(x))
x = 0.3
print(bool(x))
x = -0.3
print(bool(x))

print('Checking None...')
x = None
print(type(x))
print(x == False)  # yields False
print(x == True)  # yields False
print(True is True)
print(False is False)
print(x == None)  # yields True
print(x is None)  # preferred way to check for None

print('Convert str to bool')
print(bool(""))
print(bool("a"))
print(bool("ZEBRA"))
