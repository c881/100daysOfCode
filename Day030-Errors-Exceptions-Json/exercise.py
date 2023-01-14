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

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:

    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass


print(total_likes)