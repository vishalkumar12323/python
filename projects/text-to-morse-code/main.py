
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', 
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.', ')': '-.--.-'
}


def text_to_morse(text: str):
    morse_code = []

    for char in text.upper():
        if char == '':
            # seprate words with a forward slash
            morse_code.append("/")
        elif char in MORSE_CODE_DICT:
            # Append the morse code mapping
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            # Skip unknown chars
            continue

    return ''.join(morse_code);
    

def main():
    print("---- Text to Morse code converter -----")
    user_input = input("Enter the text you want to convert: ")

    if user_input.strip() == "":
        print("No text entered.")
        return
    result = text_to_morse(user_input)
    print(f"\nOriginal Text: {user_input}")
    print(f"Morse Code:   {result}")

if __name__ == "__main__":
    main()