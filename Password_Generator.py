import random
import string

def generate_password(length):
    if length < 6:
        print("Password length should be at least 6 characters!")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("----- Password Generator -----")
    try:
        length = int(input("Enter the length of the password (minimum 6): "))
    except ValueError:
        print("Please enter a valid number!")
        return

    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
