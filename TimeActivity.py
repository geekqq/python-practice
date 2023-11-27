import random


def time_activity(*args, **kvargs):
    print(args)
    print(kvargs)
    minutes = sum(args) + random.randint(0, 60)
    print(minutes)
    choice = random.choice(list(kvargs.keys()))
    print(choice)
    print(f"You will have to spend {minutes} minutes for {kvargs[choice]}")

time_activity(10, 20, 10, hobby='Dance', sport='Boxing', fun='Driving', work='DevOps')
