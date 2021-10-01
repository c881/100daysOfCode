from turtle import Screen, Turtle
#import csv
import pandas
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

screen = Screen()

screen.setup(width=726,height=492)
image = "blank_states_img.gif"
screen.bgpic(image)

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
answer = ""
while len(guessed_states) < len(all_states) and answer != None:
    answer = screen.textinput(title=f"{len(guessed_states)}/{len(data.state)} states correct",
                              prompt="Can you guess a state?")
    if answer != None:
        answer = answer.title()
        if answer in all_states and answer not in guessed_states:
            guessed_states.append(answer)
            state_data = data[data.state == answer]
            tim.goto(int(state_data.x), int(state_data.y))
            tim.write(answer)

# all_states = set(all_states)
# guessed_states = set(guessed_states)
#
# states_to_learn = pandas.DataFrame(list(all_states ^ guessed_states))

states_to_learn = pandas.DataFrame([state for state in all_states if state not in guessed_states])
states_to_learn.to_csv("states_to_learn.csv")

# if answer in states:
#     tim.goto(x=states[answer][0], y=states[answer][1])
#     tim.write(arg=f"{answer}", align=ALIGNMENT, font=FONT)

# screen.mainloop()

