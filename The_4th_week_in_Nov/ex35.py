from sys import exit


def gold_room():
    print("This room is full of gold. How much do you take?")

    next_ = input("> ")
    if "0" in next_ or "1" in next_:
        how_much = int(next_)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard.")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear.")
    bear_moved = False

    while True:
        next_ = input("> ")

        if next_ == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next_ == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
        elif next_ == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next_ == "open door" and not bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next_ = input("> ")
    if "flee" in next_:
        start()
    elif "head" in next_:
        dead("Well that is tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print('Which one do you take?')

    next_ = input("> ")

    if next_ == "left":
        bear_room()
    elif next_ == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()






