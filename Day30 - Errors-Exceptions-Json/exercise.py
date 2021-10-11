fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    ## My version
    # try:
    #     fruit = fruits[index]
    #     print(fruit + " pie")
    # except IndexError:
    #     print(f"Wrong Index.\nYou should try again with number between 0 and {len(fruits)}")

    # Video version
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")



make_pie(4)
