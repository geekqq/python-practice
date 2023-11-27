import random


def time_activity(*args, **kwargs):
    print(args)
    print(kwargs)
    minutes = sum(args) + random.randint(0, 60)
    print(minutes)
    choice = random.choice(list(kwargs.keys()))
    print(choice)
    print(f"You will have to spend {minutes} minutes for {kwargs[choice]}")


def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 mins")
    print("Enjoy your meal")


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

