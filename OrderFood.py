def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    #print(min_order, args)
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 mins")
    print("Enjoy your meal")


order_food("Salad", "Pizza", '红烧肉', 'Soup', "fries")