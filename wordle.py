import os
import sys
import enum
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import words
import ColorFormat as CF

class State(enum.Enum):
    BAD = CF.COLOR.NONE
    WRONG = CF.COLOR.YELLOW
    GOOD = CF.COLOR.GREEN


class Game:
    def __init__(self):
        self.rows = [[(" ", State.BAD) for _ in range(5)] for _ in range(6)]
        self.word = random.choice(words.words)
        self.guess = 0


    def start(self):
        print("Welcome to Wordle!")

        win = False
        while not win and self.guess < 6:
            print(self)
            self.make_guess()
            win = self.check_win()

            if win:
                print(self)
                print("Congratulations, you've won!")
            elif self.guess == 6:
                print(self)
                print(f"Sorry, you've run out of guesses. The word was: {self.word}")


    def check_win(self):
        for char, state in self.rows[self.guess - 1]:
            if state != State.GOOD:
                return False
        return True


    def make_guess(self):
        guess = ""
        while len(guess) != 5 or guess not in words.words:
            guess = input("Enter a five-letter word: ").lower()

        answer_count = {letter: self.word.count(letter) for letter in self.word}
        grade = [State.BAD for _ in range(5)]

        for idx, guess_char in enumerate(guess):
            if guess_char == self.word[idx]:
                grade[idx] = State.GOOD
                answer_count[guess_char] -= 1

        for idx, guess_char in enumerate(guess):
            if grade[idx] == State.BAD and guess_char in answer_count and answer_count[guess_char] > 0:
                grade[idx] = State.WRONG
                answer_count[guess_char] -= 1

        self.rows[self.guess] = list(zip(guess, grade))
        self.guess += 1


    def __str__(self):
        return_string = ""
        for row in self.rows:
            for char, state in row:
                color = state.value
                return_string += CF.ColorFormatBuilder.begin().setFormat(CF.STYLE.UNDERLINE, color).addText(char).build() + " "
            return_string += "\n"
        return return_string.strip()


if __name__ == "__main__":
    try:
        Game().start()
    except KeyboardInterrupt as ex:
        print("\nThanks for playing!")
        pass
    except Exception as ex:
        debug = os.getenv("DEBUG") != None
        if debug: print(ex)
        pass
