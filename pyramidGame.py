''' 

To-do list:
-- make look nicer
-- add some more deaths
'''


from sys import exit
from random import randint
from textwrap import dedent


class Room(object):

    def enter(self):
        print("This room is not yet formatted.")
        print("Implement your enter() for this room.")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.goNext('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.goNext(next_scene_name)

        current_scene.enter()
        

class Death(Room):

    quips = [
        "Too bad, you could have done so much with your life.",
        "Your mom shakes her head and lets out a sign of exasperation.",
        "lol",
        "I'm so proud of you.",
        "HUEHUEHUEHUE",
        "You should try again, just... less terrible.",
        "Way to go!",
        "Smooth move, Ferguson.",
        "Nerd.",
        "Why don't you give the computer to someone else so they can try?"
    ]

    def enter(self):
        print("You have died.")
        print(Death.quips[randint(0, len(self.quips) - 1)])
        print("Would you like to play again? Y/N")
        answer = input("> ")
        answer = answer.lower()

        if answer == "y":
            return('entrance')
        else:
            print("Bye-bye, loser!")
            exit(1)

class Entrance(Room):

    def enter(self):
        print(dedent("""
        \n\n\n\n\n\n\n\n\n
        You are the famous archeologist Illinois Smith. 
        You have just discovered where the door to the pyramid is, and you have the key...
        but you do not know where the keyhole is. Is it:

        A. In the rock
        B. In the door
        C. In the ground
        D. Turn around and run away

        What would you like to do?
        """))

        action = input("> ")
        action = action.lower()

        if action == 'a':
            print("That's a rock. It does not have a keyhole. Are you dense or something?")
            print("You slip while trying to open a rock and impale yourself on the key.")
            return('death')
        elif action == 'b':
            print("You enter the key into the keyhole, and open the door.")
            print("A mummy comes out and eats your face.")
            return('death')
        elif action == 'c':
            print("You slip the key into the hidden keyhole in the ground. It creaks and opens a trapdoor, leading down into the dusty earth.")
            return('anteroom')
        elif action == 'd':
            print("You coward! \nYou trip while running and fall down the stairs and break your neck.")
            return('death')
        else:
            print("I'm sorry, that's not a possible choice.")
            return('entrance')

class Anteroom(Room):

    def enter(self):
        print(dedent("""
        Finding yourself in a dimly-lit anteroom, you proceed with caution. There are probably traps. 
        Which way should you go?

        A. Straight ahead, like an idiot
        B. Left side of the room
        C. Right side of the room
        D. Spiderman across the ceiling

        What would you like to do?
        """))

        action = input("> ")
        action = action.lower()

        if action == 'a':
            print("I mean, I guess you could.")
            print("You walk straight ahead. A trap door marked 'For Stupid Idiots' opens up beneath you.")
            return('death')
        elif action == 'b':
            print("Spikey Spikes stick out of the wall. They spike you.")
            return('death')
        elif action == 'c':
            print("You walk with caution down the right side of the room, carefully avoiding all the traps.")
            print("You make your way through the door at the end, into the vault.")
            return('vault')
        elif action == 'd':
            print("Being NOT Spiderman, you can't do that.")
            print("You try to climb the ceiling. You fall off immediately and break your neck.")
            return('death')
        else:
            print("I'm sorry, that's not a possible choice.")
            return('anteroom')   

class Vault(Room):

    def enter(self):
        print(dedent("""
        Your eyes are dazzled by countless gems, golden utensils, coins, and other gorgeous artifacts.
        Riches blind your eyes as far as you can see. 
        What do you do?

        A. Take a little treasure
        B. Take a lot of treasure
        C. Run away screaming
        D. Don't touch any of it

        What would you like to do?
        """))

        action = input("> ")
        action = action.lower()

        if action == 'a':
            print("As you reach out your hand to pocket the treasure, a voice shrieks 'OH NO HE DI'N'T!!")
            print("The door slams shut and all the lights go out! You have been buried alive!")
            return('death')
        elif action == 'b':
            print("You try to pick up a life-sized golden moose.")
            print("It crushes you to death.")
            return('death')
        elif action == 'c':
            print("Spooked by a feealing of dread, You run away screaming.")
            print("You trip on your shoelace and fall into a giant chasm.")
            return('death')
        elif action == 'd':
            print("Nice work. I mean, if you've seen Aladdin you kinda know where this one is going.")
            print("You walk through the room safely, and enter the Temple.")
            return('temple')
        else:
            print("I'm sorry, that's not a possible choice.")
            return('vault')

class Temple(Room):

    def enter(self):
        print(dedent("""
        You enter a hall rich with the somber settings of ancient Egyptian religion.
        There are three doors at the end of the temple, all seeming to lead different directions.
        What do you do?

        A. Left door
        B. Center door
        C. Right door
        D. None of them

        What would you like to do?
        """))

        action = input("> ")
        action = action.lower()

        if action == 'a':
            print("You have chosen... wisely.")
            print("The door leads down a hallway deeper and deeper into the earth.")
            print("You emerge into the crypt")
            return('crypt')
        elif action == 'b':
            print("Something happens. You die a funny death.")
            return('death')
        elif action == 'c':
            print("This door opens up into a pit of lava.")
            print("Since you never look where you're going, you step straight into it.")
            return('death')
        elif action == 'd':
            print("Taking too long to make up your mind, a giant ghost Aardvark emerges out of nowhere and eats your soul.")
            return('death')
        else:
            print("I'm sorry, that's not a possible choice.")
            return('temple')

class Crypt(Room):

    def enter(self):
        print(dedent("""
        You find yourself in a dimly-lit, foul-smelling crypt. A mummy sits on a throne made of bones.
        He challenges you to a duel. He lets you pick the form.
        What do you do? 

        A. Suggest Monopoly
        B. Set him on fire
        C. Play Uno
        D. Fight with swords

        What would you like to do?
        """))

        action = input("> ")
        action = action.lower()

        if action == 'a':
            print("The mummy doesn't know what you're talking about, since he died like 10,000 years before Monopoly was created.")
            print("He eats you.")
            return('death')
        elif action == 'b':
            print("Nice call. Mummies are famously covered in toilet paper, which makes poor fire defense.")
            print("He goes up like an over-toasted marshmellow and disappears.")
            print("You follow the back exit and enter into the grand Courtroom!")
            return('courtroom')
        elif action == 'c':
            print("This is the mummy's favorite game.")
            print("Unfortunately he cheats. Then he eats you.")
            return('death')
        elif action == 'd':
            print("Bravely, you engage the mummy in the noble duel of swords!")
            print("You are not a good swordsperson.")
            print("Also, you don't have one. But he does.")
            print("This does not end well for you.")
            return('death')
        else:
            print("I'm sorry, that's not a possible choice.")
            return('crypt')

class Courtroom(Room):

    def enter(self):
        print(dedent("""
        You finally make it to the grand courtroom, where Pharaohs of old held court. 
        The majesty of it all is overwhelming.
        You see one final test: there are four scepters to choose from. 
        Which do you choose?

        A. The grey one
        B. The grey one
        C. The grey one
        D. The grey one, but in grey

        What would you like to do?
        """))

        action = input("> ")
        action = action.lower()

        if action == 'a':
            print("Good choice! You spotted the true one from the imposters.")
            print("This is what you came to get, I guess.")
            print("Man, we probably should have done a better job setting that up.")
            return('finished')
        elif action == 'b':
            print("You die.")
            return('death')
        elif action == 'c':
            print("You die.")
            return('death')
        elif action == 'd':
            print("You die, but in grey.")
            return('death')
        else:
            print("I'm sorry, that's not a possible choice.")
            return('Courtroom')

class Finished(Room):

    def enter(self):
        print("You win! Great job!")
        exit(1)


class Map(object):

    rooms = {
        'entrance': Entrance(),
        'death': Death(),
        'anteroom': Anteroom(),
        'vault': Vault(),
        'temple': Temple(),
        'crypt': Crypt(),
        'courtroom': Courtroom(),
        'finished': Finished()
    }

    def __init__(self, goHereNow):
        self.goHereNow = goHereNow

    def goNext(self, room):
        val = Map.rooms.get(room)
        return val

    def opening_scene(self):
        return self.goNext(self.goHereNow)

myMap = Map('entrance')
myGame = Engine(myMap)
myGame.play()