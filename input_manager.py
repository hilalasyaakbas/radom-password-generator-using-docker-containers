# input_manager.py

def get_user_input():
    # Collect password parameters from the user
    length = int(input("Enter password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
    include_special = input("Include special characters? (y/n): ").strip().lower() == "y"
    
    # Return the input as a tuple
    return length, include_uppercase, include_numbers, include_special

def write_params_to_file(params):
    # Write the parameters to a file (shared volume)
    file_path = "/data/params.txt"
    with open(file_path, "w") as file:
        for param in params:
            file.write(f"{param}\n")



if __name__ == "__main__":
    # Get user input
    params = get_user_input()
    
    # Write parameters to shared file
    write_params_to_file(params)
    
    # Notify the user that password is being generated
    print("Password is being generated...\n")
    




