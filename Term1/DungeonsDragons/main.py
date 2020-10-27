import json
import os
from creatures import *
data_file_path = "Term1/DungeonsDragons/data"


def saveCreature(creature):
    """
    Saves a creature to a json file in the data folder
    :creature: creature
    return: None
    """
    file_name = creature.name + '.json'
    with open(os.path.join(data_file_path, file_name), 'w+') as f:
        json.dump(creature.__repr__(), f)


def loadCreature(file_name):
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


# Get the creatures


