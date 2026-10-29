
"""
PySecrets - A fun Python Easter egg library.

Created by Shaswat.
"""

import random
import time

__version__ = "1.0.0"
__author__ = "Shaswat"


def zen():
    """Display Python's famous Zen of Python."""
    import this
def manager():
    print("MANAGER RESULTS")
    print("Shaswat: GET OUT!")

def matrix(lines=10, width=45, delay=0.05):
    """Display a Matrix-inspired stream of random characters."""
    if lines < 1 or width < 1:
        raise ValueError("lines and width must be positive integers.")

    if delay < 0:
        raise ValueError("delay cannot be negative.")

    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*"

    try:
        for _ in range(lines):
            print(
                "".join(random.choice(characters) for _ in range(width))
            )
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nMatrix stopped!")


def hack():
    """Display a fictional hacker-style animation."""
    messages = [
        "Initializing fictional hacking simulator...",
        "Scanning imaginary network...",
        "Checking pretend security systems...",
        "Decrypting imaginary files...",
        "Loading secret Easter eggs...",
        "ACCESS GRANTED!",
    ]

    try:
        for message in messages:
            print(f"[PySecrets] {message}")
            time.sleep(0.6)

        print("Just kidding! This is only an animation.")
    except KeyboardInterrupt:
        print("\nSimulation stopped!")


def secret():
    """Reveal a secret message."""
    messages = [
        "You found the secret!",
        "Python is more fun when you experiment.",
        "Keep coding. Keep creating.",
        "Every expert was once a beginner.",
        "Easter egg unlocked!",
    ]

    print("\n" + random.choice(messages) + "\n")


def konami():
    """Display the Konami-code Easter egg."""
    code = "UP UP DOWN DOWN LEFT RIGHT LEFT RIGHT B A"

    print("The legendary Konami code!")
    print(code)
    print("Achievement unlocked: Retro Gamer!")


def pydunio():
    """Display a PyDunio Easter egg."""
    print("=" * 36)
    print("       PYDUNIO EASTER EGG")
    print("=" * 36)
    print("Python meets Arduino!")
    print("Write Python-style programs for Arduino.")
    print("Keep building cool projects!")
    print("=" * 36)


def help():
    """Display the available PySecrets functions."""
    print("PySecrets - Available Easter eggs")
    print("---------------------------------")
    print("zen()       - Display Python's Zen")
    print("matrix()    - Show Matrix-style text")
    print("hack()      - Run a fictional hacker animation")
    print("secret()    - Reveal a secret message")
    print("konami()    - Reveal the Konami code")
    print("pydunio()   - Show the PyDunio Easter egg")
    print("discover()  - Choose an Easter egg interactively")


def discover():
    """Let the user choose an Easter egg."""
    options = {
        "1": zen,
        "2": matrix,
        "3": hack,
        "4": secret,
        "5": konami,
        "6": pydunio,
        "7": help,
    }

    while True:
        print("\n===== PySecrets =====")
        print("1. Python's Zen")
        print("2. Matrix")
        print("3. Hacker animation")
        print("4. Secret message")
        print("5. Konami code")
        print("6. PyDunio")
        print("7. Help")
        print("0. Exit")

        choice = input("Choose an Easter egg: ").strip()

        if choice == "0":
            print("Thanks for exploring PySecrets!")
            break

        action = options.get(choice)

        if action:
            action()
        else:
            print("Invalid choice. Try again.")


def version():
    """Display the library version."""
    print(f"PySecrets version {__version__}")


if __name__ == "__main__":
    discover()
