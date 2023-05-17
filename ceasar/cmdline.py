import sys
import fileinput
from ceasar import rotate


def main():
    try:
        # If no first argument is provided, start Interactive Mode
        text = "-"
        # If no second argument is provided, set rotation at 13
        rot = 13
        if len(sys.argv) == 2:
            text = sys.argv[1]
        if len(sys.argv) > 2:
            text = sys.argv[1]
            rot = int(sys.argv[2])
        if text == "-":
            print("--- Interactive Mode --- (Press 'Ctrl + c' to exit)")
        try:
            while True:
                print(f"Rotation: {rot}")
                with fileinput.input(text) as file:
                    for line in file:
                        print(rotate(line, rot))
                user = input(
                    "Increase or set rotation and run again? (yes/no/set)\n")
                if user.lower() == "yes" or user.lower() == "y":
                    rot = (rot + 1) % 26
                if user.lower() == "no" or user.lower() == "n":
                    break
                if user.lower() == "set" or user.lower() == "s":
                    rot = int(input("Set rotation: "))
        except FileNotFoundError:
            print(text)
            print(rotate(text, rot))
    except IndexError:
        print(
            "--- Error! No arguments given. (Usage: python3 ceasar.py [text or '-' (Interactive Mode)] [rotation (default=13)]) ---")
    except KeyboardInterrupt:
        print("--- Exit Interactive Mode ---")
    except FileNotFoundError:
        print(f"--- Error: Could not find file '{sys.argv[1]}' ---")
    except PermissionError:
        print("Error! Invalid argument given.")
    except EOFError:
        print("Error: Invalid usage")


main()
