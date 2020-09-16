import os
import platform

names_file = "names.names"
story_file = "Term1/story.story"


# Pull names from names.names
def load_names(file):
    file = open(names_file, "r")
    output = []
    for line in file:
        output.append(line.strip()[:-1] if line.strip()
                      [-1] == "," else line.strip())
    file.close()
    return output


# Save the names into an external file
def save_file():
    print("Saving File...")
    file = open(names_file, "w")
    for i, name in enumerate(names):
        file.write(name + ',\n' if i != len(names) - 1 else name)
    file.close()
    print("Done!")


# Add name to names list
def add():
    choice = input("Enter participant you wish to add: ")
    if input(f'Add {choice} to names list? y/n: ') == 'y':
        names.append(choice)
    else:
        print("Action aborted")


# Remove name from names list
def remove_name():
    for i, name in enumerate(names):
        print(f'{i} - {name}')
    choice = input("Enter participant you want to remove: ")
    print('choice', choice)

    index = -1
    if choice in names:
        index = names.index(choice)
    else:
        try:
            if int(choice) in range(len(names)):
                index = int(choice)
        except:
            pass
    if index >= 0:
        if input(f'Remove participant {names[index]}? y / n: ').lower() == 'y':
            names.pop(index)
        else:
            print("Action aborted")
    else:
        print("Invalid Input")


# Edit name in names list
def edit():
    # Print all particpants and cooresponding numbers
    for i, name in enumerate(names):
        print(f'{i} - {name}')
    print('Enter "QUIT" to quit')
    # Loop until a valid name inputed
    while True:
        edit = input("Enter participant you wish to edit: ")
        output = ''
        index = 0
        # Validify inputs
        # Quit
        if edit == "QUIT":
            break
        # If input is str and in the names list
        if edit in names:
            output = input(f'Edit participant {edit}: ')
            index = names.index(edit)
        # If input is an int and is within range of names list
        else:
            try:
                if int(edit) in range(len(names)):
                    output = input(f'Edit particpant {names[int(edit)]}: ')
                    index = int(edit)
            except ValueError:
                pass

        if len(output):
            if input(f'Change "{edit}" to "{output}"? y / n: ').lower() == 'y':
                names[index] = output
                break
            else:
                output = ''

        # If input is invalid
        print('Invalid Input\nEnter "QUIT" to exit')


# Sort participants alphebetically
def sort():
    if input("Sort Names Alphebetically? y/n: ") == 'y':
        global names
        names = sorted(names)
    else:
        print("Action Aborted")


# Print out all of the participants
def print_participants():
    for i, name in enumerate(names):
        print(f'{i} - {name + "," if i != len(names) - 1 else name}')


# Write the story using names
def write_story():
    # Load story
    story = open(story_file, 'r+')
    names_copy = names.copy()
    # Insert names from list and print string
    print(' '.join(map(lambda word: word.replace('{}', names_copy.pop(0))
                       if len(names_copy) and word[:2] == "{}" else word, story.read().split(' '))))


# A routine for quiting the program
def quit():
    print("Thanks for playing!")


################################################################################################################################################

# The user GUI
menu = """
1 - Add Participant
2 - Remove Participant
3 - Edit Participant
4 - Print Participants
5 - Sort Participants
6 - Write Story (Needs 26 Names)
7 - Save Names File
Q - Quit
"""

# A switch statement for loop below
switch = {
    "1": add,
    '2': remove_name,
    '3': edit,
    '4': print_participants,
    '5': sort,
    '6': write_story,
    '7': save_file,
    'Q': quit
}


user_input = ''
# The names list
names = load_names(names_file)

while user_input != 'Q':
    user_input = input(menu).upper()
    try:
        switch[user_input]()
    except KeyError:
        print("Invalid Option")
    input('Press "Enter" to continue: ')
    os.system('cls')
    print(platform.system())
