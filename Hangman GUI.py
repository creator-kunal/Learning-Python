import tkinter as tk
from tkinter import messagebox
import random

# Hangman art dictionary
hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\ ", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

# Sample word list
words = ["apple", "banana", "orange", "strawberry", "grape", 
         "watermelon", "mango", "pineapple", "peach", "pear", 
         "kiwi", "coconut", "cherry", "blueberry", "raspberry", 
         "lemon", "lime", "papaya", "pomegranate", 
         "guava", "plum", "fig", "apricot", 
         "avocado", "cantaloupe", "blackberry", "tangerine", 
         "grapefruit", "starfruit", "pomelo", "mandarin", 
         "persimmon", "lychee", "jackfruit", "durian", 
         "guanabana", "gooseberry", "elderberry", "mulberry", 
         "quince", "feijoa"]

class HangmanGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hangman Game")
        self.geometry("400x400")

        self.answer = random.choice(words)
        self.hint = ["_"] * len(self.answer)
        self.wrong_guesses = 0
        self.guessed_letters = set()

        self.canvas = tk.Canvas(self, width=200, height=200)
        self.canvas.pack(pady=20)

        self.hint_label = tk.Label(self, text=" ".join(self.hint), font=("Arial", 16))
        self.hint_label.pack(pady=20)

        self.guess_entry = tk.Entry(self, width=5)
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(self, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.display_man()

    def display_man(self):
        self.canvas.delete("all")
        for i, line in enumerate(hangman_art[self.wrong_guesses]):
            self.canvas.create_text(100, 20 + i * 20, text=line, font=("Arial", 16))

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", f"{guess} is already guessed.")
            return

        self.guessed_letters.add(guess)

        if guess in self.answer:
            for i in range(len(self.answer)):
                if self.answer[i] == guess:
                    self.hint[i] = guess
            self.hint_label.config(text=" ".join(self.hint))
        else:
            self.wrong_guesses += 1

        self.display_man()

        if "_" not in self.hint:
            messagebox.showinfo("You Win! \n", f"The word was: {self.answer}")
            self.destroy()
        elif self.wrong_guesses >= len(hangman_art) - 1:
            messagebox.showinfo("You Lose!", f"The word was: {self.answer}")
            self.destroy()

if __name__ == "__main__":
    game = HangmanGame()
    game.mainloop()