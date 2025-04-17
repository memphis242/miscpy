import sys
import math
import pyperclip  # Import the pyperclip library

def print_centered_text_with_border(text, border_char, width=80):
    """
    Prints text centered within a border of the specified character and width.

    Args:
        text (str): The text to center.
        border_char (str): The character to use for the border.
        width (int): The total width of the output (default is 80).

    Raises:
        ValueError: If the border_char is invalid or the text is too long.
    """
    if len(border_char) == 0:
        raise ValueError("Error: <border_char> cannot be an empty string.")
    if len(border_char) > 1:
        raise ValueError("Error: <border_char> must be a single character.")
    if not border_char.isprintable():
        raise ValueError("Error: <border_char> must be a printable character.")
    if width <= len(text) + 2:
        raise ValueError("Error: Width must be greater than the length of the text plus borders.")

    text_length = len(text) + 2  # Account for spaces around the text
    border_length = math.floor((width - text_length) / 2)
    border = border_char * border_length
    centered_text = f"{border} {text} {border}"

    # Adjust for odd widths
    while len(centered_text) < width:
        centered_text += border_char

    print(centered_text)
    pyperclip.copy(centered_text)  # Copy the centered text to the clipboard
    print("The centered text has been copied to your clipboard.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python centered_text_with_border.py <your_text> <border_char> [width]")
        sys.exit(1)

    user_input = sys.argv[1]
    border_char = sys.argv[2]

    width = 80
    if len(sys.argv) == 4:
        try:
            width = int(sys.argv[3])
        except ValueError:
            print("Error: Width must be an integer.")
            sys.exit(1)

    try:
        print_centered_text_with_border(user_input, border_char, width)
    except ValueError as e:
        print(e)
        sys.exit(1)