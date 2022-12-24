import turtle as t
import pandas as pd
from scoreboard import Scoreboard


# read the csv file and store the data in states
states = pd.read_csv("50_states.csv")
# print(states)
# print(states["state"])
# print(states["state"].to_list())


# build screen
screen = t.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)
# turtle only works with .gif files
image = "blank_states_img.gif"
# add image
screen.addshape(image)
t.shape(image)

# create scoreboard
scoreboard = Scoreboard(states["state"].to_list())


# # to get the coordinates of the state for development purposes
# def get_mouse_click_coor(x, y):
#     print(f"You clicked at ({x}, {y})")

# # prints coordinates of mouse click
# screen.onscreenclick(get_mouse_click_coor)


# TODO: 5 Record the correct guesses in a list
# TODO: 6 Keep track of score
# completed 5 and 6 by use of scoreboard OOP

# TODO: 4 use a loop to allow the user to keep guessing
while scoreboard.score < 51:
    # TODO: 1 prompt the user with a question and store the answer
    #  in a variable as titlecase
    answer_state = (screen.textinput(title = f"{scoreboard.score}/50   Guess the State",
                                    prompt = "Name a US state?"
    )).title()
    print(f"answer_state: {answer_state}")

    # If exit is entered, write the unguessed states
    # to a csv file named states_to_learn and 
    # break out of the game loop
    if answer_state == "Exit":
        new_data = pd.DataFrame(scoreboard.missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # TODO: 2 check if the guess is among the 50 states
    # check for correct answer
    # if answer_state in the values of the series states["state"]
    if answer_state in states["state"].values:
        print("You guessed correctly!")
        # TODO: 3 display guessed states name on the map
        scoreboard.correct_guess(x = states[states["state"] == answer_state]["x"].values[0],
                                    y = states[states["state"] == answer_state]["y"].values[0], 
                                    state_name = answer_state
        )

# use instead of screen.exitonclick() so that screen doesn't
# close when you click on the image
screen.mainloop()
