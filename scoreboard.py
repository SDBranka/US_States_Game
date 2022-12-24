import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self, states_names_list):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("black")
        self.score = 0
        self.missed_states = states_names_list


    def correct_guess(self, x, y, state_name):
        self.score += 1
        self.missed_states.remove(state_name)
        self.goto(x, y)
        self.write(state_name, align = "center",
                    font = ("Courier", 9, "normal")
        )
