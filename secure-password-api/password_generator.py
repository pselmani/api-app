import random
import string

def generate_password(length, special_count, digit_count):
    if length < special_count + digit_count:
        raise ValueError("Password length must be greater than the sum of special and digit counts")

    specials = "!@#$%^&*()_-+=<>?/|{}[]~"
    digits = string.digits
    letters = string.ascii_letters

    password_chars = random.choices(specials, k=special_count) + \
                     random.choices(digits, k=digit_count) + \
                     random.choices(letters, k=length - special_count - digit_count)

    random.shuffle(password_chars)
    return ''.join(password_chars)
