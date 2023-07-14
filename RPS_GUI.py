#Tkinter is a standard GUI library that creates GUI apps easily.
#The random module is used to generate random numbers.
#RPS by Shireesha
import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
choices = ["Rock", "Paper", "Scissors"]

def play_game(player_choice):
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    messagebox.showinfo("Result", f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\n\n{result}")

def play_again():
    play_game_window = tk.Toplevel(window)
    play_game_window.title("Play Rock Paper Scissors")

    # Create radio buttons for player choice
    player_choice_var = tk.StringVar(play_game_window)
    player_choice_var.set(choices[0])

    for choice in choices:
        tk.Radiobutton(play_game_window, text=choice, variable=player_choice_var, value=choice).pack()

    # Create a button to play the game
    play_button = tk.Button(
        play_game_window,
        text="Play",
        command=lambda: play_game(player_choice_var.get())
    )
    play_button.pack()

    # Focus the play button for better usability
    play_button.focus()

def start_game():
    # Create a button to play the game
    play_button = tk.Button(
        window,
        text="Play Rock Paper Scissors",
        command=play_again
    )
    play_button.pack()
# Call the start_game function to display the "Play Rock Paper Scissors" button
start_game()

# Start the GUI event loop
window.mainloop()

