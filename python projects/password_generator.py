import random
import string

def generate_password(length=12, use_lower=True, use_upper=True, use_numbers=True, use_special=True):
    required_chars = []
    character_pool = []

    if use_lower:
        character_pool += list(string.ascii_lowercase)
        required_chars.append(random.choice(string.ascii_lowercase))

    if use_upper:
        character_pool += list(string.ascii_uppercase)
        required_chars.append(random.choice(string.ascii_uppercase))

    if use_numbers:
        character_pool += list(string.digits)
        required_chars.append(random.choice(string.digits))

    if use_special:
        character_pool += list(string.punctuation)
        required_chars.append(random.choice(string.punctuation))

    if not character_pool:
        return "❌ Error: At least one character type must be selected."

    if length < len(required_chars):
        return "❌ Error: Password length too short for selected options."

    remaining_length = length - len(required_chars)
    password = required_chars + random.choices(character_pool, k=remaining_length)
    random.shuffle(password)

    return ''.join(password)

try:
    length = int(input("Enter password length : "))
    lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    special = input("Include special characters? (y/n): ").lower() == 'y'
    password = generate_password(length, lower, upper, numbers, special)
    print("\n✅ Generated Password:", password)
except ValueError:
    print("❌ Please enter a valid number for length.")
