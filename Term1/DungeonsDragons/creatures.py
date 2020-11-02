import random


class Creature:
    def __init__(self, type_, name, attack, defense, crit_mult, health):
        self.type = type_
        self.name = name
        self.attack = attack
        self.init_defense = defense
        self.defense = defense
        self.crit_chance = 0.05
        self.crit_mult = crit_mult
        self.health = health
        self.alive = True
    
    def attack_creature(self, creature):
        """
        Attack a creature 
        :param creature: Creature
        :return (Str, Bool): (attack msg, is alive?)
        """
        dmg_dealt, attack_report = creature.defend(self.attack, self.crit_chance_chance())
        # If the attack was successful
        if attack_report == "success":
            msg = f"While attacking {creature.name}, {self.name} dealt {dmg_dealt} damage"
        # If the failed attack was because of an evasion
        elif attack_report == "evaded":
            msg = f"When {self.name} attempted to attack {creature.name}, {creature.name} evaded the attack!"
        elif attack_report == "perished":
            msg = f"{creature.name} perished under {self.name}'s attack!'"
        return msg, creature.alive


    def crit_chance_chance(self):
        """
        Return the crit_multiplier for the attack
        :return Float: the crit multiplier
        """
        return self.crit_mult if random.random() < self.crit_chance else 1

    def defend(self, attack_dmg, crit=1):
        """
        Defend against incoming damage
        :param attack_dmg: Int: the amount of damage
        :param crit: Float: the crit multiplier
        :return (Int, Str): (Dmg dealt, attack_report)
        """
        dmg_dealt = 0
        # Subtract attack damage from defense
        self.defense -= self.attack * crit
        # If damage was greater than current defense
        if self.defense < 0:
            # Subtract excess dmg from health
            self.health += self.defense
            dmg_dealt = abs(self.defense)
        # If dead, die
        attack_report = "success"
        if self.health <= 0:
            self.perish()
            attack_report = "perished"
        return dmg_dealt, attack_report

    def reset_defense(self):
        """
        Resets the creatures defense
        :return None
        """
        self.defense = self.init_defense

    def perish(self):
        """
        Kills the creature
        :return None
        """
        self.alive = False

    def __repr__(self):
        return {
            "type": self.type,
            "name": self.name,
            "attack": self.attack,
            "init_defense": self.init_defense,
            "defense": self.defense,
            "crit_mult": self.crit_mult,
            "health": self.health
        }
    
    def __str__(self):
        return f"{self.name}: {self.type} | {self.health}"

class Elf(Creature):
    def __init__(self, name, evade_chance, attack=30, defense=15, health=80):
        type_ = "elf"
        crit_mult = 1.25
        super().__init__(type_, name, attack, defense, crit_mult, health)
        self.evade_chance = evade_chance

    def defend(self, attack_dmg, crit=1):
        """
        Defend against incoming damage. a self.evade_chance chance to dodge the attack
        :param attack_dmg: Int: incoming damage
        :param crit: Float: the crit multiplier
        :return (Int, Str): (dmg dealt, attack report)
        """
        dmg_dealt = 0
        if random.random() > self.evade_chance:
            # Subtract attack damage from defense
            self.defense -= self.attack * crit
            # If damage was greater than current defense
            if self.defense < 0:
                # Subtract excess dmg from health
                self.health += self.defense
                dmg_dealt = abs(self.defense)
            # If dead, die
            if self.health <= 0:
                self.perish()
                return dmg_dealt, "perished"
            return dmg_dealt, "success"
        return dmg_dealt, "evaded"

    def inc_evade_chance(self):
        self.evade_chance += 0.025

    def __repr__(self):
        output = super().__repr__()
        output["evade_chance"] = self.evade_chance
        return output


class Dwarf(Creature):
    def __init__(self, name, dmg_inc, miss_chance, attack=45, defense=20, health=100):
        type_ = "dwarf"
        crit_mult = 1.05
        super().__init__(type_, name, attack, defense, crit_mult, health)
        self.dmg_inc = dmg_inc
        self.dmg_inc_chance = 0.05
        self.miss_chance = miss_chance

    def attack_creature(self, creature):
        """
        Attack a creature
        :param creature: Creature
        :return (Str, Bool): (message, is alive?)
        """
        msg = ""
        # If dwarf doesn't miss attack
        if random.random() > self.miss_chance:
            dmg_dealt, attack_report = creature.defend(self.attack, self.crit_chance_chance())
            self.attempt_dmg_inc()
            if attack_report == "success":
                msg = f"While attacking {creature.name}, {self.name} dealt {dmg_dealt} damage!"
            elif attack_report == "evaded":
                msg = f"When {self.name} attempted to attack {creature.name}, {creature.name} evaded the attack!"
            elif attack_report == "perished":
                msg = f"{creature.name} perished under {self.name}'s attack!'"
        # If dwarf misses attack
        else:
            msg = f"When {self.name} attempted to attack {creature.name}, {self.name} missed!"
        return msg, creature.alive

    def attempt_dmg_inc(self):
        """
        Has a self.dmg_inc_chance chance to increase self.damage by self.dmg_inc. It also increases self.miss_chance by 5%
        :return None
        """
        if random.random() < self.dmg_inc_chance:
            self.attack += self.dmg_inc
            self.miss_chance += 0.05

    def __repr__(self):
        output = super().__repr__()
        output["dmg_inc"] = self.dmg_inc
        output["miss_chance"] = self.miss_chance
        return output


class Wizard(Creature):
    def __init__(self, name, health_steal_inc_chance, attack=30, defense=0, health=100, health_steal=1.25):
        type_ = "wizard"
        crit_mult = 1
        super().__init__(type_, name, attack, defense, crit_mult, health)
        self.health_steal_inc_chance = health_steal_inc_chance
    
    def attack_creature(self, creature):
        """
        Attacks a creature; the wizards health incerases by self.health_steal percent of the damage dealth, then attempts to increase health steal
        :param creature: Creature
        :return Str: message
        """
        dmg_dealt, attack_report = creature.defend(self.attack, self.crit_mult)
        msg = ""

        if attack_report == "success":
            msg = f"While attacking {creature.name}, {self.name} dealt {dmg_dealt}, stealing {dmg_dealt * self.health_steal} health!"
            self.health += dmg_dealt * self.health_steal
            self.attempt_inc_health_steal()
        elif attack_report == "evaded":
            msg = f"When {self.name} attempted to attack {creature.name}, {creature.name} evaded the attack!"
        elif attack_report == "perished":
            msg = f"{creature.name} perished under {self.name}'s attack!'"

        return msg, creature.alive
    
    def attempt_inc_health_steal(self):
        """
        Attempts to increase self.health_steal
        :return None
        """
        if random.random() > self.health_steal_inc_chance:
            self.health_steal += 0.05

    def __repr__(self):
        output = super().__repr__()
        output["health_steal_inc_chance"] = self.health_steal_inc_chance
