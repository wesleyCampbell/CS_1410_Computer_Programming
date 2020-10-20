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
        :return None
        """
        creature.defend(self.attack, self.crit_chance_chance())

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
        :return Bool: Attack success?
        """
        # Subtract attack damage from defense
        self.defense -= self.attack * crit
        # If damage was greater than current defense
        if self.defense < 0:
            # Subtract excess dmg from health
            self.health += self.defense
        # If dead, die
        if self.health <= 0:
            self.perish()
        return True

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


class Elf(Creature):
    def __init__(self, name, evade_chance):
        type_ = "elf"
        attack = 30
        defense = 15
        crit_mult = 1.25
        health = 80
        super().__init__(type_, name, attack, defense, crit_mult, health)
        self.evade_chance = evade_chance

    def defend(self, attack_dmg, crit=1):
        """
        Defend against incoming damage. a self.evade_chance chance to dodge the attack
        :param attack_dmg: Int: incoming damage
        :param crit: Float: the crit multiplier
        :return Bool: attack success?
        """
        if random.random() > evade_chance:
            # Subtract attack damage from defense
            self.defense -= self.attack * crit
            # If damage was greater than current defense
            if self.defense < 0:
                # Subtract excess dmg from health
                self.health += self.defense
            # If dead, die
            if self.health <= 0:
                self.perish()
            return True
        return False

    def inc_evade_chance(self):
        self.evade_chance += 0.02.5


class Dwarf(Creature):
    def __init__(self, name, dmg_inc, miss_chance):
        type_ = "dwarf"
        attack = 45
        defense = 20
        crit_mult = 1.05
        health = 100
        super().__init__(type_, name, attack, defense, crit_mult, health)
        self.dmg_inc = dmg_inc
        self.dmg_inc_chance = 0.05
        self.miss_chance = miss_chance

    def attack_creature(self, creature):
        """
        Attack a creature
        :param creature: Creature
        :return None
        """
        # If dwarf doesn't miss attack
        if random.random() > self.miss_chance:
            creature.defend(self.attack, self.crit_chance_chance)
            self.attempt_dmg_inc(self)

    def attempt_dmg_inc(self):
        """
        Has a self.dmg_inc_chance chance to increase self.damage by self.dmg_inc. It also increases self.miss_chance by 5%
        :return None
        """
        if random.random() < self.dmg_inc_chance:
            self.damage += self.dmg_inc
            self.miss_chance += 0.05



class Wizard:
    def __init__(self, name, health_steal_inc_chance):
        type_ = "wizard"
        attack = 30
        defense = 0
        crit_mult = 1
        health = 100
        super().__init__(type_, name, attack, defense, crit_mult, health)
        self.health_steal = 0.25
        self.health_steal_inc_chance = health_steal_inc_chance
    
    def attack(self, creature):
        """
        Attacks a creature; the wizards health incerases by self.health_steal percent of the damage dealth, then attempts to increase health steal
        :param creature: Creature
        :return None
        """
        if creature.defend(self.damage, crit_mult):
            self.health += self.damage *= self.health_steal
            self.attempt_inc_health_steal()
    
    def attempt_inc_health_steal(self):
        """
        Attempts to increase self.health_steal
        :return None
        """
        if random.random() > self.health_steal_inc_chance:
            self.health_steal += 0.05