# password_generator.py
import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special):
    # Base characters (lowercase)
    characters = string.ascii_lowercase
    
    # Include uppercase letters if specified
    if include_uppercase:
        characters += string.ascii_uppercase
    
    # Include numbers if specified
    if include_numbers:
        characters += string.digits
    
    # Include special characters if specified
    if include_special:
        characters += string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def read_input_params():
    # Read input parameters from a file (shared volume)
    input_file_path = "/data/params.txt"
    with open(input_file_path, "r") as file:
        params = file.read().splitlines()
    
    # Parse the parameters
    length = int(params[0])
    include_uppercase = params[1] == "True"
    include_numbers = params[2] == "True"
    include_special = params[3] == "True"
    
    return length, include_uppercase, include_numbers, include_special

def write_generated_password(password):
    # Write the generated password to a file (shared volume)
    output_file_path = "/data/password.txt"
    with open(output_file_path, "w") as file:
        file.write(f"Generated Password: {password} \n")

if __name__ == "__main__":
    # Read input parameters from the shared file
    length, include_uppercase, include_numbers, include_special = read_input_params()
    
    # Generate the password
    password = generate_password(length, include_uppercase, include_numbers, include_special)
    
    # Write the password to the output file
    write_generated_password(password)
