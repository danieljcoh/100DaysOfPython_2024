import turtle

import pandas

screen = turtle.Screen()
screen.title(f"Guess the States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

number_of_guesses = 0
number_of_states_correct = 0

states_data = pandas.read_csv("50_states.csv")
list_of_states = states_data.state.to_list()
list_of_state_x_coor = states_data.x.to_list()
list_of_state_y_coor = states_data.y.to_list()

states_confirmed = []


dict_of_states_and_locations = {
    "states": list_of_states,
    "x_coor": list_of_state_x_coor,
    "y_coor": list_of_state_y_coor
}


# print(dict_of_states_and_locations["states"].index("Texas"))
# print(dict_of_states_and_locations["states"][42])
# print(dict_of_states_and_locations["x_coor"][42])
# print(dict_of_states_and_locations["y_coor"][42])


while number_of_states_correct != 50:
    number_of_guesses += 1

    answer_state = screen.textinput(title=f"{number_of_states_correct}/50Guess the State", prompt="What's another state?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missed_states = [state for state in list_of_states if state not in states_confirmed]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_practice.csv")
        break

    if answer_state in list_of_states and answer_state not in states_confirmed:
        state_idx = dict_of_states_and_locations["states"].index(answer_state)
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x=dict_of_states_and_locations["x_coor"][state_idx], y=dict_of_states_and_locations["y_coor"][state_idx])
        new_state.write(dict_of_states_and_locations["states"][state_idx], align="center", font=('Arial', 14, 'normal'))

        states_confirmed.append(answer_state)
        number_of_states_correct += 1

        # print(state_idx)
        # print(dict_of_states_and_locations["states"][state_idx])
        # print(dict_of_states_and_locations["x_coor"][state_idx])
        # print(dict_of_states_and_locations["y_coor"][state_idx])

