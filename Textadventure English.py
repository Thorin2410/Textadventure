import random

class Item:
    def __init__(self, weigth, worth, name):
        self.weight = weigth
        self.name = name
        self.worth = worth

class Potion(Item):
    def __init__(self, weight, worth, name):
        Item.__init__(self, 3, 23, "Potion")

class HealthPotion(Potion):
    def __init__(self, weight, worth, regenerated_health):
        Potion.__init__(self, 5, 17, "Health Potion")
        self.regenerated_health = regenerated_health

class Character:
    def __init__(self, hp, ad, name):
        self.hp = hp
        self.ad = ad
        self.name = name

    def get_hit(self, ad):
        self.hp = self.hp - ad
        if self.hp <= 0:
            self.die()

    def is_dead(self):
        return self.hp <= 0

    def die(self):
        print(self.name + " died")

class Zombie:
    def __init__(self):
        Character.__init__(self, 60, 23, "Zombie")

class Skeleton:
    def __init__(self):
        Character.__init__(self, 35, 13, "Skeleton")

class Mage(Character):
    def __init__(self):
        Character.__init__(self, 73, 26, "Mage")

class Ghost(Character):
    def __init__(self):
        Character.__init__(self, 100, 20, "Spooky Ghost")

class Goblin(Character):
    def __init__(self):
        Character.__init__(self, 100, 10, "Goblin")

class Orc(Character):
    def __init__(self):
        Character.__init__(self, 300, 30, "Orc")

class Troll(Character):
    def __init__(self):
        Character.__init__(self, 240, 32, "Troll")

class Player(Character):
    def __init__(self, name, hp, ad):
        Character.__init__(self, hp, ad, name)
        self.max_hp = hp

    def die(self):
        exit("Wasted. Try again.")

    def rest(self):
        self.hp = self.max_hp


class Field:
    def __init__(self, enemies):
        self.enemies = enemies
        self.loot = []

    def print_state(self):
        print("You look around and see: ")
        for i in self.enemies:
            print(i.name)

    @staticmethod
    def gen_random():
        rand = random.randint(0,2)
        if rand == 0:
            return Field([])
        if rand == 1:
            return Field([Skeleton, Goblin(), Ghost(), Mage()])
        if rand == 2:
            return Field([Goblin(), Skeleton(), Skeleton(), Zombie(), Orc(), Ghost(), Troll(), Mage()])


class Map:
    def __init__(self, width, height):
        self.state = []
        self.x = 0
        self.y = 0
        for i in range(width):
            fields = []
            for j in range(height):
                fields.append(Field.gen_random())
            self.state.append(fields)

    def print_state(self):
        self.state[self.x][self.y].print_state()

    def get_enemies(self):
        return self.state[self.x][self.y].enemies

    def forward(self):
        if self.x == len(self.state) - 1:
            print("You see huge mountains which you can't pass.")
        else:
            self.x = self.x + 1

    def backwards(self):
        if self.x == 0:
            print("Cliffs ... don't jump!")
        else:
            self.x = self.x - 1

    def right(self):
        if self.y == len(self.state[self.x]) - 1:
            print("You see huge mountains which you can't pass.")
        else:
            self.y = self.y + 1

    def left(self):
        if self.y == 0:
            print("Cliffs ... don't jump!")
        else:
            self.y = self.y - 1

def forward(p, m):
    m.forward()

def right(p, m):
    m.right()

def left(p, m):
    m.left()

def backwards(p, m):
    m.backwards()

def save():
    pass

def load():
    pass

def sword():
    pass

def axe():
    pass

def quit_game(p, m):
    print("I told you not to jump off the cliff!")
    exit(0)

def print_help(p, m):
    print(Commands.keys())

def pickup(p, m):
    pass

def fight(p, m):
    enemies = m.get_enemies()
    while len(enemies) > 0:
        enemies[0].get_hit(p.ad)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
        for i in enemies:
            p.get_hit(i.ad)
        print("You have won and still have " + str(p.hp) + " HP left")
        if p.hp <= 125:
            print("maybe you should enter rest to regenerate life!")

def rest(p, m):
    p.rest()

Commands = {
    'help': print_help,
    'quit': quit_game,
    'pickup': pickup,
    'forward': forward,
    'right': right,
    'left': left,
    'backwards': backwards,
    'fight': fight,
    'save': save,
    'load': load,
    'rest': rest,
    'sword': sword,
    'axe': axe
}

if __name__ == '__main__':
    name = input("Enter your name: ")
    p = Player(name, 200, 100)
    map = Map(5,5)
    print("(Type help to show the commands available)\n")
    while True:
        command = input(">").lower().split(" ") #pickup
        if command[0] in Commands:
            Commands[command[0]](p, map)
        else:
            print("You run in circles and have no idea what you are doing.")
        map.print_state()
