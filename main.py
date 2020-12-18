
from turtle import *
import random

screen = Screen()
screen.setup(width=500, height=400)

game_on = True

def play_game():
    clearscreen()
    is_race_on = False
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color from the list {colors}: ").lower

    y_positions = [-70, -40, -10, 20, 50, 80]
    all_turtles = []

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)


    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    play_again = screen.textinput(title=f"You've won! ", prompt=f"The {winning_color} turtle got there first. You want to play again?(y/n): ").lower()
                    if play_again == "y":
                        play_game()
                    if play_again == "n":
                        print(Error)
                        #return game_on == False
                    else:
                        print(Error)
                        #return game_on == False
                else:
                    play_again = screen.textinput(title=f"You lose! ", prompt=f"The {winning_color} turtle got there first. You want to play again?(y/n): ").lower()
                    if play_again == "y":
                        play_game()
                    if play_again == "n":
                        print(Error)
                        #return game_on = False
                        clearscreen()
                    else:
                        print(Error)
                        #return game_on = False
                        clearscreen()

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

while game_on:
    play_game()




screen.exitonclick()