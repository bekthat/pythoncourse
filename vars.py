a = 'abc'  # string
b = 123  # integer
c = 12.34  # float
d = True  # boolean
e = None  # null
f = [1, 2, 3]  # list
g = (1, 2, 3)  # tuple
h = {'name': 'John', 'age': 30}  # dictionary
i = {1, 2, 3}  # set

print(id(a))  # memory address of a
print(type(a))  # type of a

my_number = 10
print(id(my_number))

other_number = my_number
print(id(other_number))
