import time
import random


def slow_print(text, delay=0.06):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # newline at the end


def end_game():
    print("YOU ARE DIE.")
    print("Thanks for playing")
    exit()


slow_print("=====WELCOME TO THE ADVENTURE GAME=====")
slow_print("you are in a dark room and you see 2 doors.")
door = input("Which door do you want to go through? (1 or 2): ")

if door == "1":
    items = ["gun", "bread", "water"]
    player = {
        "health": 100
    }
    gun = {
        "bullets": 6,
        "damage": 30,
    }

    slow_print(
        "you see a black backpack sitting on the floor and decide to open it.")
    slow_print("you find a bunch of items: ")
    for item in items:
        slow_print(item)
    slow_print("you close the bag, take it with you and continue into the room.")
    slow_print("you hear a noise and see a monster in the corner of the room.")
    slow_print("you have to choose what to do next.")
    slow_print("1. Fight the monster with your items.")
    slow_print("2. Run away and hide.")
    slow_print("3. Try to talk to the monster.")

    monster = {
        "health": 120,
        "damage": random.randint(20, 30)
    }

    def show_stats():
        slow_print("stats:")
        slow_print(f"player HP: {player['health']}")
        slow_print(f"monster HP: {monster['health']}")
        slow_print(f"bullets left: {gun['bullets']}")

    while True:
        show_stats()

        choice = input("What do you want to do? (1, 2, or 3): ")

        if choice == "1":
            slow_print("You choose to attack the monster.")
            while True:
                print(f"bullet damage: {gun['damage']}")
                key = input("press f to fire a shot at the monster: ")
                if key == "f":
                    print("BLAM")
                    gun['bullets'] -= 1
                    slow_print("Reloading...\n")
                    damage = gun['damage']
                    monster['health'] -= damage
                    if monster['health'] <= 0:
                        slow_print("monster is dead")
                        break
                    else:
                        slow_print(f"Monster Health: {monster['health']}")
                        slow_print(f"Bullets: {gun['bullets']}")
                        slow_print("the monster attacks you")
                    if gun["bullets"] == 0:
                        print("you are out of bullets")
                        slow_print("the monster attacks you and you die")
                        end_game()
                    player['health'] -= monster["damage"]
                    if player['health'] <= 0:
                        end_game()

                else:
                    print("invalid input. press f to shoot the monster")

        elif choice == "2":
            slow_print(
                "you run away and hide behind a table, the monster stalks you and kills you instantly.")
            end_game()
        elif choice == "3":
            slow_print(
                "you try to talk to the monster, but it doesn't understand you and attacks and kills you.")
            end_game()
        else:
            slow_print("input a valid choice")
        slow_print(
            "you scavenge the monsters corpse to see if its flesh is edible")
        slow_print(
            "you suddenly get teleported out and are holding a piece of paper saying:")
        slow_print("congratulations you cleaared the game")
        break
elif door == "2":
    slow_print("That was the exit you are free.")
