import turtle
import pandas

FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.tracer(0)
screen.addshape(image)
screen.setup(width=800, height=600)
turtle.shape(image)

# Read the csv file
states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()

correct_guesses = []

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

prompt_title = "Guess the State"

while len(correct_guesses) < 50:
    screen.update()
    answer_state = screen.textinput(title=prompt_title, prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in correct_guesses]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")

        break

    if answer_state in states_list:
        if answer_state not in correct_guesses:
            correct_guesses.append(answer_state)
            correct = len(correct_guesses)
            prompt_title = f"{correct}/50 States Correct"

            # Get dataframe row for correct state
            state_data = states_data[states_data.state == answer_state]

            state_turtle = turtle.Turtle()
            state_turtle.hideturtle()
            state_turtle.penup()
            state_turtle.goto(int(state_data.x), int(state_data.y))
            state_turtle.write(answer_state, align="left", font=FONT)

# screen.exitonclick()
