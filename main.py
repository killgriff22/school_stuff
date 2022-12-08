########
#import modules
#######
from os import system
#check modules
try:
    import colorama
    import rainbowtext
except:
    system("python3 -m pip install colorama")
    system("python3 -m pip install rainbowtext")
from colorama import Fore,Back,init
from time import sleep
from rainbowtext import text
init()
RESET_ALL=f"{Fore.RESET}{Back.RESET}"
system("clear")
########
#define functions
#######
def start():
    print(text("Welcome"),RESET_ALL)
    sleep(1)
    room1()
def room1():
    global mirrorside
    sleep(1)
    system("clear")
    print("You are in a room with a TV, a locked door and a table!")
    if not "key" in inventory:
        move = input("\nWhat would you like to do? Say one of these choices:\n\tCheck TV\n\tCheck Table\n")
    elif "key" in inventory:
        move = input("\nWhat would you like to do? Say one of these choices:\n\tCheck TV\n\tCheck Table\n\tOpen door\n")
    if move.lower() in ["tv","check tv"]:
        if "key" not in inventory:
            inventory.append("key")
            print(f"{Fore.GREEN}Behind the TV was a key!\nYou picked it up!{RESET_ALL}")
        elif key in inventory:
            print("You already picked the key up!\n")
        room1()
    elif move.lower() in ["table","check table"]:
        print(f"{Fore.BLUE}Underneath the table was a code!\n1738{RESET_ALL}")
        sleep(1)
        room1()
    elif key in inventory and move.lower() in ["door","open door"]:
        room2()
    elif move == "384077":
        mirrorside=True
        for item in ["key1", "key2", "key3", "key4"]:
            inventory.append(item)
        room3()
    else:
        print(f"{Fore.RED}NOT RECOGNIZED{RESET_ALL}")
        room1()

def room2():
    sleep(1)
    system("clear")
    global trapdooropen
    print("You are in The second room!\nIn this room are 2 boxes and a locked trapdoor.\nOne box has a 5 letter code\nthe other box has a 4 digit code and a\nmessage on top that says\n\"B HI ND U\"")
    if not trapdooropen:
        move = input("\nWhat would you like to do? Say one of these choices:\n\tnumber box\n\tletter box\n\tdoor\n")
    elif trapdooropen:
        move = input("\nYou can only go forward or backward.Say one of these choices:\n\tdoor\n\ttrapdoor\n")
    if move.lower() == "number box" and not trapdooropen:
        attempt = input(f"{Fore.BLUE}Please enter a 4 digit number\n")
        print(f"{RESET_ALL}",end="")
        if attempt == "1738":
            print(f"{Fore.GREEN}CORRECT!!!!!!!!\nInside the box you find a paper that says \"UZYPD11\"{RESET_ALL}")
            sleep(1)
        else:
            print(f"{Fore.RED}INCORRECT!!!!!!!!\nTRY AGAIN\nHINT: room behind\n")
        room2()
    elif move.lower() == "letter box" and not trapdooropen:
        attempt = input(f"{Fore.BLUE}Please enter a 5 letter word\n")
        print(f"{RESET_ALL}",end="")
        if attempt == "JONES":
            print(f"{Fore.GREEN}Good Job!\nThe trapdoor opens!{RESET_ALL}")
            sleep(1)
            trapdooropen=True
        else:
            print(f"{Fore.RED}INCORRECT!!!!!!!!\nTRY AGAIN\nHINT: CEASAR WILL RULE NEW VEGAS\n{RESET_ALL}")
        room2()
    elif move.lower() == "door":
        room1()
    elif move.lower() == "trapdoor" and trapdooropen:
        room3()
    else:
        print(f"{Fore.RED}NOT RECOGNIZED{RESET_ALL}")
        room2()

def room3():
    sleep(1)
    system("clear")
    global mirrorside
    global mirrorbroken
    global inventory
    if mirrorside:
        print(f"{Fore.RED}You are not in room3{RESET_ALL}, there is a box, a shard of glass and two doors\nOne door says \"EXIT\" with 4 locks on it\nThe other says \"ROOM 1\"")
    else:
        print(f"{Fore.GREEN}You are in room3, there is a crowbar and a mirror{RESET_ALL}")
    if "key1" in inventory and "key2"in inventory and "key3" in inventory and "key4" in inventory:
        move = input("\nYou can only exit Say one of these choices:\n\texit\n")
    elif "crowbar" in inventory and not mirrorbroken:
        move = input("\nWhat would you like to do? Say one of these choices:\n\tbreak mirror\n\topen trapdoor\n")
    elif mirrorbroken and not mirrorside:
        move = input("\nYou smash the mirror!\nYou can only go forward or backward.Say one of these choices:\n\tpass mirror\n\topen trapdoor\n")
    elif mirrorside:
        move = input("\nWhat would you like to do? Say one of these choices:\n\tpass mirror\n\texamine glass\n\tenter room1\n\topen box\n")
    if mirrorbroken:
        if move.lower() in ["pass mirror","mirror"]:
            mirrorside=True
            inventory.remove("crowbar")
            room3()
    if "crowbar" in inventory:
        if not mirrorbroken:
            if move.lower() in ["break mirror","mirror"]:
                mirrorbroken=True
                room3()
    if mirrorside:
        if (move.lower() == "exit") and ("key1" in inventory and "key2"in inventory and "key3" in inventory and "key4" in inventory):
            system("clear")
            print("Hooray for you!!!!\nYou escaped!!!!")
        if move.lower() in ["pass mirror","mirror"]:
            mirrorside=False
            room3()
        elif move.lower() in ["examine glass","glass"]:
            print("You Found a code!\n",text("69420"))
            sleep(2)
            room3()
        elif move.lower() in ["open box","box"]:
            code = input("Enter a 5 digit code\n")
            if code == "69420":
                inventory.append("key1")
                print("You found a key! enscribed is \"Key#1\"\n")
                sleep(2)
                room3()
        elif move.lower() in ["open door","room1","room 1","door"]:
            room4()
    else:
        print(f"{Fore.RED}NOT RECOGNIZED{RESET_ALL}")
        room3()
def room4():
    sleep(1)
    system("clear")
    print(f"You are in room1.....{Fore.RED}But something feels off{RESET_ALL}")
    move = input(f"\nWhat would you like to do? Say one of these choices:\n\tCheck TV\n\tCheck Table\n\tCheck under TV\n\tleave\n")
    if move.lower() in ["tv","check tv"]:
        if "key4" not in inventory:
            inventory.append("key4")
            print(f"{Fore.GREEN}Behind the TV was a key!\nYou picked it up!{RESET_ALL}")
        elif "key4" in inventory:
            print("You already picked the key up!\n")
        room4()
    elif move.lower() in ["table","check table"]:
        if "key3" not in inventory:
            inventory.append("key3")
            print(f"{Fore.GREEN}under the table was a key!\nYou picked it up!{RESET_ALL}")
        elif "key3" in inventory:
            print("You already picked the key up!\n")
        room4()
    elif move.lower() in ["under tv", "check under tv"]:
        if "key2" not in inventory:
            inventory.append("key2")
            print(f"{Fore.GREEN}under the TV was a key!\nYou picked it up!{RESET_ALL}")
        elif "key2" in inventory:
            print("You already picked the key up!\n")
        room4()
    elif move.lower() in ["door","leave"]:
        room3()
    else:
        print(f"{Fore.RED}NOT RECOGNIZED{RESET_ALL}")
        room4()
########
#main
#######
inventory = []
key="key"
trapdooropen = False
mirrorside=False
mirrorbroken=False
start()