
### INTRODUCCION ###

# list comprehension
l = [i for i in range(10)]
print(l)

# list comprehension with if condition
l = [i for i in range(10) if i % 2 == 0]
print(l)

# list comprehension with if else condition
l = [i if i % 2 == 0 else i * i for i in range(10)]
print(l)
