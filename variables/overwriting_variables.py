x = 5
print("Before reassignment:")
print("Value of x:", x)
print("ID of x:", id(x))

x = 10
print("\nAfter reassignment:")
print("Value of x:", x)
print("ID of x:", id(x))

x = 10
y = x
print("Value of x:", x)
print("ID of x:", id(x))
print("Value of y:", y)
print("ID of y:", id(y))
x = 20
print("Value of x:", x)
print("ID of x:", id(x))
print("Value of y:", y)
print("ID of y:", id(y))


a = [1, 2, 3]  # a points to the list object [1, 2, 3]
print("Value of a:", a)
print("ID of a:", id(a))
b = a  # b also points to the same list object as a
print("Value of b:", b)
print("ID of b:", id(b))
a = [4, 5, 6]  # a now points to a new list object [4, 5, 6], but b still points to [1, 2, 3]
print("Value of a:", a)
print("ID of a:", id(a))
print("Value of b:", b)
print("ID of b:", id(b))