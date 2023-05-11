import sys
import time
import os
import json
import getpass


print('''                                                                                             \n                                                                         ▄                          \n      ╒█▄    ,¬▄█AA ▄▄▄ ¬█▄█▄ ██`▀▀█▀¬██▀▀     ▄▄  ▄    ▄      a▄N█▀▀▀█  █ █▀▀▀▀▀                   \n      █"█▄█═ █▌ █  ╒█ -█µ█▀▀█µ███  █. █&       ███▄▐▌   █         █   █▀╘█ ▐▌-                      \n      █▄███▌ █▌ ▀█ ▐█▄▄█"█  ▐▌█-▀ⁿ ▐⌐▐█▄;      ▀ ▀┐▐███,███▀"     █   ▀    ▐█A⌐                     \n      █⌐ └█▀██   ▀ⁿ  ¬¬     `▀└        `     ▀▀▀▀▀▀└`└└└└└`▀▀▀                                      \n                 ▄▄▄▄∩▌ j▌ ╓█  ╒▄,  ▄ ╒█    ▄Æ▄  ╒r                                 ,╓              \n              '▀▀█    █44█ ]█╖ ▐▌▀█ █ ▐▌ ▄▄ ▀▀R▄ █                    ▀█        ╓@╢▒╜               \n                 █    █  ▀  █▒▒▒▌  ▀█ ╘█,█▀▄▄▄▄▀ ▀   ╖               , ▌    ╓╥╢▒▒▒╢`                \n                 '           ╢▒▒▒▒@╖    ¬¬ ▀╢░   e  ╢▒           ╓╢╢╜` ▌,╥╢▒▒▒▒▒▒╜                  \n                             ╙▒▒▒▒▒▒╢╗╖    ║▒▒╖    ║▒▒▒       ╓╢╢▒▒╜,╓▐▒▒▒▒▒▒▒▒╢                    \n                              ║▒▒▒▒▒▒▒▒╢@╖ ║▒▒▒╢╖ j▒▒▒╢    ╓@╢▒▒▒▒▒╢▒▒█▒▒▒▒▒▒▒╜                     \n                               ╢▒▒▒▒▒▒▒▒▒▒╢╢▒▒▒▒▒▒▒▒▒▒▒░╓╢╢▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒╣                       \n                  .╓           ╙▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀⌠!░░░░▀█▒▒▒▒▒█▀'╙Ñ▒▒▒▒▌▒▒▒▒╜                        \n                    ╙╢╢╗╖       ╙▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒W▄W╧²"╙▀'¬¬▐▌  ` ▒▒▒▒▒▒▒▒╜                         \n                     ▄▄▓@▒▒p╖    ╙▒▒▒▒▒▒▒▒▒▒▒▒▒╩█,     ▄∞M══▄▀▀∞²└▀▒▒▐▒▒▒░                          \n                  ,█╢╣▓▓▓╢█▒▒█▒@╖╖║▒▒▒▒▒▒▒▒▒▒▌⌐  ▐,≈M▀▄▄██████     ╙▒█▒▒░                           \n                 ╒╣▓▓▓▓▀▀█▒╢╢╢▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒╗▄∞█▀▄███████████     █▌▒▒                 ,,╓╥╢╜     \n           ▄▄▄▄▄,██▀██     █▒╢╢█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█ "▀████████████     █▒▒╓╖╥@╢╢╢╜     ,╓@╢╢▒║╜`       \n        ▄█▒╢╣╣█▀▒▒▒▒▒█▄, ╙▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄   ▀██████████▌    ▓▒▒▒▒▒▒╢`  ,╓╥╢╢▒▒▒╢╜`          \n       ▐▒╣╣╢▓╩▓▀▄▒▒▒▒▒█▀▒▒▒╢╢▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█    ████████▀L   █╢█▒▒▒╢▒╓╥╢╢▒▒▒▒▒╢╜              \n       ██▄██    ▐▒▒▄▒▄█▒╢╢╢▒█▀╙╢▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█   ██▀███▀▄▀   █╢╢╢▌▒▒▒▒▒▒▒▒▒▒╢╜                 \n       ▌▒▒╢█    ▐▒▒▒██▓▓█░▒╖╥@@╢▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▄   "▀▀└`    █▒║╢╢▓▒▒▒▒▒▒▒▒╨`                   \n       ▀▒╢╢╢▒█▓▒▒▒▒▒█╙▀▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█╦▄▄▄▄▄▄▄@▓▒╢╢╢╢╢╢█▒▒▒▒▒╜`                     \n        └▀╣▒▄█▒▒▒▒█▀╖╖╓,▀▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢╢║╢║║╢╢╢╢╢╢╢╢╢╢╫▒▒▒▒╢╢╢╢╢╢╢╢╢╢╢@@@╗╥╖╓,     \n            -└▀▀╙▒▒▒▒▒▒▒▒▒▀▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢╢╢╢╢╢╢╢╢╢╢╢╢╢╢╢█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢Ñ    \n                 └╢▒▒▒▒▒▒▒▒▒█▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█╣╢╢╢╢╢╢╢╢╢╢╢╢╢╢╢╫▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢╜╜`      \n''')


# Get the absolute path of the script
script_path = os.path.abspath(__file__)
root_dir_path = os.path.dirname(os.path.dirname(script_path))

# Function to print text gradually
def print_gradually(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04)  

def print_gradually_fast(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.005) 

# Prompt the user for their full name character by character
print_gradually("Please enter your full name: ")
full_name = input()

# Extract the first name from the full name
first_name = full_name.split()[0]


# Prompt the user for their favorite food, addressing them by their first name
# print_gradually("Thank you, " + first_name + "! Welcome to Automate All The Things! Are you exited?: ")
# favorite_food = input()


def prompt_with_options(message, options):
    # Print the message and options
    print_gradually(message + "\n")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Keep asking for input until a valid option is chosen
    while True:
        print_gradually("Enter your choice: ")
        choice = input()
        
        # Validate the input
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice)-1]
        
        print("Invalid input. Please enter the number corresponding to your choice.")

# Define the message and options
message = "Thank you, " + first_name + "! Welcome to Automate All The Things! Are you exited?"
options = ['Yes', 'YEEEAAAAHHHHHH!!!!!']

# Prompt the user and get their choice
user_choice = prompt_with_options(message, options)

# Process the user's choice
if user_choice == 'Yes':
    print_gradually("That's great!\n")
else:
    print_gradually("WOOOOHOOOOOOOO!!!! DAMN RIGHT!!\n")


print_gradually("Alright, let's get the necessary details. What will be the name of your app?: ")
app_name = input()


print_gradually("Great name! What's the name of your Azure DevOps Organization?: ")
az_devops_org = input()

print_gradually("Ok. What's your DockerHub username?: ")
dockerhub_username = input()

print_gradually("I'm gonna need you to get me your AWS Access Keys:\n")
aws_access_key = getpass.getpass("- Access Key: ")
aws_secret_access_key = getpass.getpass("- Secret Access Key: ")



# Create a dictionary with the variable names and their values
data = {
    "AATT_FULL_NAME": full_name,
    "AATT_APP_NAME": app_name,
    "AATT_AZ_DEVOPS_ORG": az_devops_org,
    "AATT_DOCKERHUB_USERNAME": dockerhub_username,
    "AATT_AWS_ACCESS_KEY": aws_access_key,
    "AATT_AWS_SECRET_ACCESS_KEY": aws_secret_access_key
}

# def replace_keys_in_file(file_path, replacements):
#     with open(file_path, 'r') as file:
#         content = file.read()
    
#     for key, value in replacements.items():
#         content = content.replace(key, value)
    
#     with open(file_path, 'w') as file:
#         file.write(content)


# def search_and_replace(directory, replacements):
#     for root, _, files in os.walk(directory):
#         for file_name in files:
#             if file_name == 'info.json':
#                 continue  # Skip processing info.json file
#             file_path = os.path.join(root, file_name)
#             replace_keys_in_file(file_path, replacements)

def main():
    # Create a dictionary with the variable names and their values
    data = {
        "AATT_FULL_NAME": full_name,
        "AATT_APP_NAME": app_name,
        "AATT_AZ_DEVOPS_ORG": az_devops_org,
        "AATT_DOCKERHUB_USERNAME": dockerhub_username,
        "AATT_AWS_ACCESS_KEY": aws_access_key,
        "AATT_AWS_SECRET_ACCESS_KEY": aws_secret_access_key
    }

    # Extract the replacements
    replacements = {key: str(value) for key, value in data.items()}

    # Specify the directory to search
    directory = root_dir_path  

    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name == 'info.json':
                continue  # Skip processing info.json file
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r') as file:
                content = file.read()
            
            for key, value in replacements.items():
                content = content.replace(key, value)
            
            with open(file_path, 'w') as file:
                file.write(content)
            # replace_keys_in_file(file_path, replacements)

    # Search and replace keys in files
    # search_and_replace(directory, replacements)

    # print('Replacement completed successfully!')

# Save the data dictionary to a JSON file
# output_file = root_dir_path + "/info.json"
# with open(output_file, "w") as file:
#     json.dump(data, file, indent=4)

print_gradually("That's it! All files have been customized with your info.\nDon't worry, this file is specified in the .gitignore so it won't be pushed if you decide to upload this.\n\n")

print_gradually_fast(" _   _    _    ____  ______   __     _   _   _ _____ ___  __  __    _  _____ ___ _   _  ____ _ _ _ \n| | | |  / \  |  _ \|  _ \ \ / /    / \ | | | |_   _/ _ \|  \/  |  / \|_   _|_ _| \ | |/ ___| | | |\n| |_| | / _ \ | |_) | |_) \ V /    / _ \| | | | | || | | | |\/| | / _ \ | |  | ||  \| | |  _| | | |\n|  _  |/ ___ \|  __/|  __/ | |    / ___ \ |_| | | || |_| | |  | |/ ___ \| |  | || |\  | |_| |_|_|_|\n|_| |_/_/   \_\_|   |_|    |_|   /_/   \_\___/  |_| \___/|_|  |_/_/   \_\_| |___|_| \_|\____(_|_|_)")


# Print the entered name and the script's absolute path
# print("\nYour full name is:", full_name)
# print("\nYour app name is:", app_name)
# print("Rootdir  path:", root_dir_path)
# print("Variables saved in:", output_file)
