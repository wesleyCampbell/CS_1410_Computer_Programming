import json
import os
from creatures import *
data_file_path = "Term1/DungeonsDragons/data"

clearTerminal = lambda: os.system('cls' if os.name == 'nt' else 'clear')


class Program:
    def __init__(self):
        self.creatures = []
        self.creature_types = [
            'elf',
            'dwarf',
            'wizard'
        ]
        self.setup_success = False

    def saveCreatures(self):
        """
        Saves a creature to a json file in the data folder
        :creature: creature
        return: None
        """
        for c in self.creatures:
            file_name = c.name + '.json'
            with open(os.path.join(data_file_path, file_name), 'w+') as f:
                json.dump(c.__repr__(), f)
 
    def loadCreature(self, file_name):
        """
        Given a file name, return a creature with inputed data
        :param filename: a filename FROM the data folder
        :return Creature
        """
        with open(os.path.join(data_file_path, file_name), 'r') as f:
            data = json.load(f)

        if data["type"] == "elf":
            """params:
            name | evade_chance | attack | defense | health
            """
            name = data["name"]
            evade_chance = data["evade_chance"]
            attack = data["attack"]
            defense = data["defense"]
            health = data["health"]

            return Elf(name, evade_chance, attack, defense, health)

        elif data.type == "dwarf":
            """
            params:
            name | dmg_inc | miss_chance | attack | defense | health
            """
            name = data["name"]
            dmg_inc = data["dmg_inc"]
            miss_chance = data["miss_chance"]
            attack = data["attack"]
            defense = data["defense"]
            health = data["health"]

            return Dwarf(name, dmg_inc, miss_chance, attack, defense, health)

        elif data.type == "wizard":
            """
            params:
            name | health_steal_inc_chance | attack | defense | health | health_steal
            """
            name = data["name"]
            health_steal_inc_chance = data["health_steal_inc_chance"]
            attack = data["attack"]
            defense = data["defense"]
            health = data["health"]
            health_steal = data["health_steal"]
            return Wizard(name, health_steal_inc_chance, attack, defense, health, health_steal)

    def printCreatures(self):
            """
            This function prints all the current creatures
            :return None
            """
            clearTerminal()
            for i, c in enumerate(self.creatures):
                print(f"{i}: {str(c)}")
            input("Press enter to continue...")

    def verifyInput(self, type_, max_value, msg, clear_terminal=True):
        """
        This function verifies that user input is the correct type. This function only works on verifing number values
        :param type_: Type, the type of the input
        :param max_value: Num, the maximum value the input can be
        :param msg: String, the input message
        """
        user_input = ''
        # This while loop verifies that the user inputs valid data
        while user_input != 'q':
            # Only clear the terminal if asked for it
            if clear_terminal:
                clearTerminal()
            print("Enter 'q' to quit: ")

            # If user input is valid
            try:
                user_input = type_(input(msg))
                # If the user inputed a value greater than the max
                if user_input > max_value:
                    user_input = max_value
                return user_input

            # If user input is invalid
            except:
                print(f"That was an invalid option. Please enter a {type_}")
                input("Press enter to continue...")
                continue

            # If user input was invalid
            else:
                print("That is an invalid option.")
                input("Press enter to try again....")
                continue

    def addCreature(self):
        """
        This function returns a new creature defined by user
        :return Creature
        """
        creature_input = ''

        # While loop verifies that user selects a valid creature type
        while creature_input != 'q':
            clearTerminal()
            print("Enter 'q' to quit.")
            # Print creature options
            for i in self.creature_types:
                print(i)

            creature_input = input("What kind of creature do you want to have: ").lower()

            added_creature = None

            # If the creature was a valid type
            if creature_input in self.creature_types:

                name = ''
                name_list = [c.name for c in self.creatures]
                # Make sure that user selects a new name,
                # Primarily for file issues
                while name not in name_list:
                    if name in name_list:
                        print("That name is already taken")
                        input("Press enter to try again...")
                        continue
                    name = input(f"Enter {creature_input}'s name: '")
                    break

                # If user selected an Elf
                if creature_input == "elf":
                    clearTerminal()

                    evade_chance = self.verifyInput(float, 0.5, "What is your evade chance? A float 0-0.5: ")

                    print(f"Added elf {name}")
                    input("Press enter to continue...")

                    added_creature = Elf(name, evade_chance)
                
                # If user selected a Dwarf
                elif creature_input == "dwarf":
                    clearTerminal()

                    dmg_inc = self.verifyInput(int, 10, "What is your damige increment? An int 0-10: ")

                    miss_chance = self.verifyInput(float, 0.5, "What is your miss chance? A float 0-0.5: ")

                    print(f"Added dwarf {name}")
                    input("Press enter to continue...")

                    added_creature = Dwarf(name, dmg_inc, miss_chance)

                elif creature_input == "wizard":
                    clearTerminal()

                    health_steal_inc_chance = self.verifyInput(float, 0.5, "What is your health steal increment chance? A float 0-0.5: ")

                    print(f"Added wizard {name}")
                    input("Press enter to continue...")

                    added_creature = Wizard(name, health_steal_inc_chance)
                self.creatures.append(added_creature)
                break

    def removeCreature(self):
        """
        This function will have the user select a creature to remove
        :return None
        """
        clearTerminal()
        
        # If there are creatures to remove
        if len(self.creatures):
            # Print out all creatures and their corresponding index value
            self.printCreatures()
            print('\n')
            
            user_input = self.verifyInput(int, len(self.creatures)-1, "Which creature do you want to remove? Index #: ", clear_terminal=False)
            selected_creature = self.creatures[user_input]

            # Confirm that user wants to delete creature
            if input(f"Delete {selected_creature.name}? y/n: ").lower() == 'y':
                # Delete creature from self.creatures
                self.creatures.remove(selected_creature)

                # If creature has save file, delete it
                try:
                    os.remove(os.path.join(data_file_path, selected_creature.name + ".json"))
                except FileNotFoundError:
                    pass

                print(f"Deleted {selected_creature.name}.")
            else:
                print("Deletion aborted.")
            input("Press enter to continue...")

    def selectLoadCreature(self):
        clearTerminal()
        
        # Collect all data files in data folder
        files = [f for f in os.listdir(data_file_path) if os.path.isfile(os.path.join(data_file_path, f))]
        
        for i, f in enumerate(files):
            print(f"{i}: {f}")

        # Verify that user selects a valid creature to load
        selected_index = self.verifyInput(int, len(files) - 1, "Which creature do you wish to load? Index #: ", clear_terminal=False)

        # Add creature to self.creatures
        c = self.loadCreature(files[selected_index])
        self.creatures.append(c)
        print(f"Added {c.type} {c.name}!")
        input("Press enter to continue...")

    def setupCreatures(self):
        """
        A function where the user makes a bunch of creatures
        :return None
        """

        switch = {
            "1": self.addCreature,
            "2": self.selectLoadCreature,
            "3": self.removeCreature,
            "4": self.printCreatures,
            "5": self.saveCreatures,
            "6": lambda: '',
            "q": lambda: "",
        }
        msg = """
            1: Add a creature
            2: Load a saved creature
            3: Remove a creature
            4: List current creatures
            5: Save current creatures
            6: Play game
            "q": Quit
        """

        user_input = ''
        while user_input != "q" and user_input != "6":
            os.system("clear")
            print("Select an option:")
            print(msg)

            user_input = input()

            # If we're going to play game
            if user_input == "6":
                self.setup_success = True

            try:
                switch[user_input]()

            except KeyError as e:
                print("That was an invalid option.")
                print(e)
                input("Press enter to continue...")
                continue

    def playGame(self):
        """
        This function is the main game loop
        :return None
        """
        for c in self.creatures:
            print(str(c))
        print('')

        for c in self.creatures:
            print(f"It is {c.name}'s turn!'")
            print('')

            opponents = self.creatures.copy()
            opponents.remove(c)

            for opponent in opponents:
                print(str(c))
            
            to_attack = ''
            name_list = [o.name for o in opponents]
            while to_attack not in name_list:
                to_attack = input("Who do you wish to attack? ")

                # If the user inputed an invalid name
                if to_attack not in opponents:
                    print("That is an invalid option. Please review inputed name")
                    input("Press enter to try again...")
                    continue
                
                selected_creature = opponents[name_list.index(to_attack)]

            c.attack_creature(selected_creature)
            if selected_creature.health < 0:
                self.removeCreature(selected_creature)

if __name__ == "__main__":
    program = Program()
    program.setupCreatures()
    # If setup was a success and there are creatures, play game
    if program.setup_success and len(program.creatures):
        program.playGame()
    else:
        print("Unable to play game. Try reloading game or adding creatures")