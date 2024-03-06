import random
import string

def generate_password(length, num_passwords, include_special_chars):
    """
    Generate a secure password with a mix of uppercase and lowercase letters, numbers, and special characters.

    :param length: The length of the password.
    :param num_passwords: The number of passwords to generate.
    :param include_special_chars: Whether to include special characters in the password.
    :return: A list of generated passwords.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    if num_passwords < 1:
        raise ValueError("Number of passwords must be at least 1.")

    generated_passwords = []

    for _ in range(num_passwords):
        password = []

        # Include at least one uppercase letter, one lowercase letter, and one number.
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))

        # Fill the rest of the password with random characters.
        for _ in range(length - 3):
            if include_special_chars and random.random() < 0.25:
                password.append(random.choice(string.punctuation))
            else:
                password.append(random.choice(string.ascii_letters + string.digits))

        # Shuffle the password to ensure randomness.
        random.shuffle(password)

        generated_passwords.append("".join(password))

    return generated_passwords

def main():
    """
    The main function of the password generation script.
    """
    try:
        length = int(input("Enter the desired password length (minimum 8): "))
        num_passwords = int(input("Enter the number of passwords to generate (minimum 1): "))
        include_special_chars = input("Include special characters? (y/n): ").lower() == "y"

        generated_passwords = generate_password(length, num_passwords, include_special_chars)

        for i, password in enumerate(generated_passwords):
            print(f"Password {i + 1}: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__== "__main__":
    main()