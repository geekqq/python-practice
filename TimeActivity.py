import random


def time_activity(*args, **kvargs):
    print(args)
    print(kvargs)
    min = sum(args) + random.randint(0, 60)
    print(min)
    choice = random.choice(list(kvargs.keys()))
    print(choice)
    print(f"You will have to spend {min} minutes for {kvargs[choice]}")

time_activity(10, 20, 10, hobby='Dance', sport='Boxing', fun='Driving', work='DevOps')
