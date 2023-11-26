# Define function

def add(arg1, arg2):
    total = arg1 + arg2
    return total


out = add(2, 3)
print(out)
print(add(10, 30))
print("#############")


def adder(arg1, arg2):
    print(arg1 + arg2)


adder(10, 50)
print(adder(1, 4))
print("#############")


def sum(arg):
    x = 0
    for i in arg:
        x += i
    return x


out = sum([10, 2, 30, 40])
print(out)

print("#############")


def greetings(MSG = 'Morning'):
    print(f"Good {MSG}")
    print("Welcome to functions.")


greetings('Evening')

print("#############")

def vac_feedback(vac, efficiency):
    print(f"{vac} Vaccine is having {efficiency} % efficiency")
    if (efficiency > 50) and (efficiency <= 75):
        print("Seems not so effective, needs more trial!")
    elif (efficiency > 75) and (efficiency < 90):
        print("Can consider this vaccine")
    elif efficiency >= 90:
        print("Sure, will take the shot!")
    else:
        print("Needs many more trials")


vac_feedback("Pfizer", 95)
vac_feedback("Unkown", 45)
vac_feedback(efficiency=91, vac='Modera')
