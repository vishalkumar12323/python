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
    window = tk.Tk()
    window.title("Text to Morse Code")
    window.minsize(width=560, height=480)
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    content = tk.Frame(window, padx=24, pady=24)
    content.grid(row=0, column=0, sticky="nsew")
    content.columnconfigure(0, weight=1)
    content.rowconfigure(3, weight=1)
    content.rowconfigure(7, weight=1)

    tk.Label(
        content,
        text="Text to Morse Code",
        font=("TkDefaultFont", 18, "bold"),
    ).grid(row=0, column=0, sticky="w")
    tk.Label(
        content,
        text="Enter text below. Letters, numbers, and supported punctuation are converted; "
        "unsupported characters are ignored. A slash separates words.",
        justify="left",
        wraplength=500,
    ).grid(row=1, column=0, sticky="w", pady=(4, 18))

    tk.Label(content, text="Text").grid(row=2, column=0, sticky="w", pady=(0, 6))
    input_box = tk.Text(content, height=6, wrap="word", undo=True)
    input_box.grid(row=3, column=0, sticky="nsew")

    tk.Label(content, text="Morse code").grid(
        row=6, column=0, sticky="w", pady=(18, 6)
    )
    output_box = tk.Text(content, height=5, wrap="word", state="disabled")
    output_box.grid(row=7, column=0, sticky="nsew")

    status_label = tk.Label(content, text="", anchor="w")
    status_label.grid(row=9, column=0, sticky="ew", pady=(10, 0))

    def convert_text(event=None):
        source_text = input_box.get("1.0", "end-1c")
        if not source_text.strip():
            output = ""
            status = "Enter some text to convert."
        else:
            output = text_to_morse(source_text)
            status = (
                "No supported characters to convert."
                if not output
                else "Conversion complete."
            )

        output_box.configure(state="normal")
        output_box.delete("1.0", "end")
        output_box.insert("1.0", output)
        output_box.configure(state="disabled")
        status_label.configure(text=status)
        return "break"

    def clear_text():
        input_box.delete("1.0", "end")
        output_box.configure(state="normal")
        output_box.delete("1.0", "end")
        output_box.configure(state="disabled")
        status_label.configure(text="")
        input_box.focus_set()

    buttons = tk.Frame(content)
    buttons.grid(row=8, column=0, sticky="w", pady=(14, 0))
    tk.Button(buttons, text="Convert", command=convert_text).grid(
        row=0, column=0, padx=(0, 8)
    )
    tk.Button(buttons, text="Clear", command=clear_text).grid(row=0, column=1)

    window.bind("<Control-Return>", convert_text)
    input_box.focus_set()
    window.mainloop()

if __name__ == "__main__":
    main()