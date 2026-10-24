import tkinter as tk

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ',': '--..--', 
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.', ')': '-.--.-'
}


def text_to_morse(text: str):
    morse_code = []

    for char in text.upper():
        if char.isspace():
            if morse_code and morse_code[-1] != "/":
                morse_code.append("/")
        elif char in MORSE_CODE_DICT:
            # Append the morse code mapping
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            # Skip unknown chars
            continue

    return ' '.join(morse_code)

def morse_to_text(morse_code: str):
    text_by_morse = {code: char for char, code in MORSE_CODE_DICT.items()}
    words = morse_code.split("/")
    
    return " ".join(
        "".join(text_by_morse[code].lower() for code in word.split())
        for word in words
    ).strip()
    

def main():
    print("---- Text to Morse code converter And Vice versa -----")
    user_input = input("Enter the text you want to convert: ")

    if user_input.strip() == "":
        print("No text entered.")
        return
    morse_code = text_to_morse(user_input)
    # text = morse_to_text(morse_code)

    print(f"\nOriginal Text: {user_input}")
    print(f"Morse Code:   {morse_code}\n")

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Text To Morse Code Generator")
    window.minsize(width=720, height=500)
    # main()

    window.mainloop()