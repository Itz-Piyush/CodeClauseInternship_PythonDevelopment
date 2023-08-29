import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Hello, world! This is a typing test.",
    "Python programming language is fun to learn.",
    "Practice makes perfect when it comes to typing.",
]


def highlight_errors(correct, typed):
    highlighted = ""
    for c1, c2 in zip(correct, typed):
        if c1 == c2:
            highlighted += c1
        else:
            highlighted += f"\033[91m{c2}\033[0m"  # red highlighter
    return highlighted


def typing_test():
    while True:
        sentence = random.choice(sentences)
        print("Type the following sentence:")
        print(sentence)

        input("Press Enter when you are ready to start...")

        start_time = time.time()
        user_input = input("Start typing: ")
        end_time = time.time()

        elapsed_time = end_time - start_time
        words_typed = len(user_input.split())
        words_per_minute = (words_typed / elapsed_time) * 60

        highlighted = highlight_errors(sentence, user_input)
        accuracy = (user_input.count(" ") / len(sentence.split())) * 100

        print("\nHighlighted:", highlighted)
        print("Typing speed:", words_per_minute, "words per minute")
        print("Accuracy:", accuracy, "%")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing! Goodbye.")
            break


typing_test()
