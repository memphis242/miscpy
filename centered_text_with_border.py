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
    if width <= (len(text) + 2):
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


def print_c_comment(text, width=80, indent=0):
    """
    Prints a C comment with text centered in the form below:

                 text
                   |
                   V
    /********** Example **********/
    <------------width------------>

    Args:
        text (str): The text to include in the comment
        width (int): The total width of the output (default is 80)

    Raises:
        ValueError: If the text is too long.
    """
    if width <= (len(text) + 2 + 2 + indent):   # 2 for spaces, 2 for '/' characters
        raise ValueError(f"Error: Width is too short. Needs to at least be {len(text) + 2 + 2 + indent}.")

    text_length = len(text) + 2 + indent  # Account for spaces around the text
    star_border_length = math.floor((width - text_length) / 2) - 2 # Take 2 off for the two '/' characters
    star_border = '*' * star_border_length
    centered_text = (' ' * indent) + f"/{star_border} {text} {star_border}/"

    print(centered_text)
    pyperclip.copy(centered_text)  # Copy the centered text to the clipboard
    print("The centered text has been copied to your clipboard.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python centered_text_with_border.py <your_text> <border_char> [width]")
        sys.exit(1)
    
    flag = sys.argv[1]

    if flag == '-c':

        if len(sys.argv) >= 4:
            try:
                width = int(sys.argv[3])
            except ValueError:
                print("Error: Width must be an integer.")
                sys.exit(1)

        if len(sys.argv) >= 5:
            try:
                width = int(sys.argv[4])
            except ValueError:
                print("Error: Indentation must be an integer.")
                sys.exit(1)

        print_c_comment( sys.argv[2], width )

    else:
        user_input = sys.argv[1]
        border_char = sys.argv[2]
        indentation = 3 # Assume 3 space indentation
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