from pathlib import Path
import argparse
from caesar import Caesar

# Parser configuration
parser = argparse.ArgumentParser(
    description="Caesar cipher | ROT13 - Letter substitution with rotation of letter values by an arbitrary integer.",
    epilog="Written by toshydev",
    prog="caesar",
)
parser.add_argument("text",
                    help="Text to be encoded/decoded by rotation")
parser.add_argument("-f", "--file", action="store_true",
                    help="File to be read and encode/decoded")
parser.add_argument("-r", "--rotation",
                    help="Value(Integer) to rotate text by")


def main():
    try:
        caesar = Caesar()
        args = parser.parse_args()
        if args.rotation:
            caesar.set_rotation(int(args.rotation))
        if args.file:
            target = Path(args.text)
            if not target.exists():
                print("The target file doesn't exist")
                raise SystemExit(1)
            caesar.parse(target)
        if not args.file:
            caesar.set_text(args.text)
        while True:
            print(f"\nRotation: {caesar.get_rotation()}")
            caesar.rotate()
            print(caesar.get_rotated_text())
            print("------------------------------\n")
            user = input(
                "--- Increase rotation [ENTER] | Set rotation [s] | Quit [q] ---\n")
            if user.lower() == "quit" or user.lower() == "q":
                break
            if user.lower() == "set" or user.lower() == "s":
                new_rotation = int(input("Set rotation: "))
                caesar.set_rotation(new_rotation)
            if user.lower() == "":
                new_rotation = (caesar.get_rotation() + 1) % 26
                caesar.set_rotation(new_rotation)

    except KeyboardInterrupt:
        print("--- Exit Caesar ---")
