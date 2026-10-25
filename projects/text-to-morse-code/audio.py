import time
import math
import array
import sys

# Try to import pygame for Linux audio handling
try:
    import pygame
    # Initialize the mixer with standard CD-quality settings (44.1 kHz, 16-bit, mono)
    pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=1024)
except ImportError:
    print("Error: The 'pygame' library is required to play audio on Linux.")
    print("Please install it by running: pip install pygame")
    sys.exit(1)

# Comprehensive dictionary mapping characters to Morse code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', '!': '-.-.--', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '_': '..--.-', '$': '...-..-',
    '@': '.--.-.'
}

# Morse Code Timing Settings
SAMPLE_RATE = 44100
FREQUENCY = 600       # Tone pitch in Hz
DOT_DURATION = 0.150   # 150 milliseconds (converted to seconds)
DASH_DURATION = DOT_DURATION * 3

# Pre-calculate audio buffers for a single Dot and single Dash
def generate_sine_wave(duration, frequency=FREQUENCY, sample_rate=SAMPLE_RATE):
    """Generates a raw sine wave buffer for a specific duration."""
    num_samples = int(duration * sample_rate)
    # Create an array of 16-bit signed integers
    buf = array.array('h', [0] * num_samples)
    for i in range(num_samples):
        # Calculate sine wave value scaled to 16-bit audio range max (32767)
        t = float(i) / sample_rate
        buf[i] = int(32767 * math.sin(2 * math.pi * frequency * t))
    return pygame.mixer.Sound(buffer=buf)

# Generate sound objects globally to save CPU cycles
DOT_SOUND = generate_sine_wave(DOT_DURATION)
DASH_SOUND = generate_sine_wave(DASH_DURATION)

def text_to_morse(text):
    """Translates text to a formatted Morse code string."""
    morse_translated = []
    words = text.upper().split(' ')
    for word in words:
        word_code = [MORSE_CODE_DICT[char] for char in word if char in MORSE_CODE_DICT]
        morse_translated.append(' '.join(word_code))
    return '   '.join(filter(None, morse_translated))

def play_morse_audio(morse_text):
    """Plays generated sine wave audio based on Morse code strings."""
    print("Playing audio...", end="", flush=True)
    
    words = morse_text.split('   ')
    for word_index, word in enumerate(words):
        letters = word.split(' ')
        
        for letter_index, letter in enumerate(letters):
            for symbol in letter:
                if symbol == '.':
                    DOT_SOUND.play()
                    time.sleep(DOT_DURATION)
                elif symbol == '-':
                    DASH_SOUND.play()
                    time.sleep(DASH_DURATION)
                
                # Intra-character gap (pause between elements inside a letter)
                time.sleep(DOT_DURATION)
            
            # Short gap between letters (3 units total, we already slept 1 unit above)
            if letter_index < len(letters) - 1:
                time.sleep(DOT_DURATION * 2)
                
        # Word gap (7 units total, we subtract gaps already taken care of)
        if word_index < len(words) - 1:
            time.sleep(DOT_DURATION * 4)
            
    print(" Done!")

def main():
    print("--- Linux Text to Morse Code Converter ---")
    user_input = input("Enter text to convert: ")
    
    if user_input.strip() == "":
        print("Empty input string.")
        return
        
    morse_result = text_to_morse(user_input)
    print("\nOriginal Text: ", user_input)
    print("Morse Code:    ", morse_result)
    print("-" * 40)
    
    play_morse_audio(morse_result)

if __name__ == "__main__":
    main()
