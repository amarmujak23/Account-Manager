import os
import getpass
import json
from datetime import datetime
import time

# Function to clear the terminal screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Function to add a profile with the current date
def add_profile(username, password):
    now = datetime.now()
    date_created = now.strftime("%Y-%m-%d %H:%M:%S")

    # Storing the profile data in a dictionary without asterisks
    profile = {"Username": username, "Password": password, "DateCreated": date_created}
    profile_list.append(profile)

# Function to mask the username and password with asterisks
def mask_profile(profile):
    masked_profile = profile.copy()
    masked_profile["Username"] = "*" * len(profile["Username"])
    masked_profile["Password"] = "*" * len(profile["Password"])
    return masked_profile

# Load existing profiles from a JSON file
def load_profiles():
    if os.path.isfile("profiles.json"):
        with open("profiles.json", "r") as file:
            return json.load(file)
    else:
        return []

profile_list = load_profiles()

while True:
    commands = input("Available commands: add, show, delete, clear, or exit: ").strip()

    if commands == "add":
        username = input("Type a username: ")
        password = getpass.getpass("Type a password: ")
        # Clear the screen after user input
        clear_screen()
        add_profile(username, password)
        print("Profile Created")

    elif commands == "show":
        if not profile_list:
            print("There are no profiles")
        else:
            for i, profile in enumerate(profile_list):
                print(f"PROFILE {i}")
                masked_profile = mask_profile(profile)
                print(f"Username: {masked_profile['Username']}")
                print(f"Password: {masked_profile['Password']}")
                print(f"Date Created: {profile['DateCreated']}")

    elif commands == "delete":
        if len(profile_list) == 0:
            print("There are no profiles to delete")
        else:
            print(f"Profiles:")
            for i, profile in enumerate(profile_list):
                print(f"PROFILE {i}")

            delete_input = input("Type a profile to delete, or 'all' to delete all profiles: ")

            if delete_input.lower() == "all":
                profile_list.clear()
                print("All profiles deleted")
            else:
                try:
                    delete_index = int(delete_input)

                    if 0 <= delete_index < len(profile_list):
                        deleted_profile = profile_list.pop(delete_index)
                        print(f"PROFILE {delete_index} has been deleted:")

                    else:
                        print("Invalid profile number. No profile deleted.")

                except ValueError:
                    print("Invalid input. Please enter a valid profile number.")

    elif commands == "clear":
        clear_screen()
        print("Terminal Cleared")

    elif commands == "exit":
        #Default location in the same directory as the script
        save_path = "profiles.json"


        with open(save_path, "w") as file:
            json.dump(profile_list, file, indent=4)

        print("...")
        time.sleep(2)
        print(f"Profiles have been saved to {save_path}")
        print("Bye")
        break

    else:
        print("Invalid command")
