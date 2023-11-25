# List / Collection of multi datatypes, enclosed in square brackets / mutable
str1 = "Alpha"
num1 = 123
first_list = [str1, "DevOps", 47, num1, 1.5]
print(first_list)

# Tuple / Collection of multi datatype, enclosed in round bracket / immutable

first_tuple = (str1, 'DevOps', 47, num1, 1.5)
print(first_tuple)

# Dictionary / Key-Value pair in curly brackets
first_dictionary = {"Name": "Imran", "Weight": 75, "Exercises": ["Boxing", "Dancing", "Jogging"]}
print(first_dictionary)

print("Variable first_list is a: ", type(first_list))
print("Variable first_tuple is a: ", type(first_tuple))
print("Variable first_dictionary is a: ", type(first_dictionary))

# Boolean
x = True
y = False
print(x)
print(y)
print("x is a ", type(x))
print("y is a ", type(y))
