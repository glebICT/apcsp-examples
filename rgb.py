import random

def binary_to_decimal(binary_str):
    """Convert binary string to decimal"""
    return int(binary_str, 2)

def decimal_to_binary(decimal):
    """Convert decimal to 8-bit binary string"""
    return format(decimal, '08b')

# Dictionary of colors and their RGB values
color_table = {
    'indigo': (75, 0, 130),
    'ivory': (255, 255, 240),
    'light pink': (255, 182, 193),
    'light yellow': (255, 255, 224),
    'magenta': (255, 0, 255),
    'neutral gray': (127, 127, 112),
    'pale yellow': (255, 255, 160),
    'vivid yellow': (255, 255, 14)
}

def play_game():
    score = 0
    while True:
        # Pick a random color
        color_name = random.choice(list(color_table.keys()))
        rgb_values = color_table[color_name]
        
        # Convert to binary
        binary_rgb = tuple(decimal_to_binary(x) for x in rgb_values)
        
        print("\nBinary RGB values:", binary_rgb)
        print("\nAvailable colors:")
        print("-" * 40)
        print("{:<15} {:>8} {:>8} {:>8}".format("Color", "R", "G", "B"))
        print("-" * 40)
        for color, (r, g, b) in color_table.items():
            print("{:<15} {:>8} {:>8} {:>8}".format(color, r, g, b))
        print("-" * 40)
        guess = input("Can you guess which color this is? (or 'quit' to exit): ").lower()
       
        if guess == 'quit':
            break
        
        if guess == color_name:
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong! It was {color_name}. Score: {score}")

if __name__ == "__main__":
    print("Welcome to the RGB Binary Color Game!")
    print("Try to guess the color from its binary RGB values.")
    play_game()