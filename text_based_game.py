import time
A = "a"
B = "b"
C = "c"
D = "d"
yes = ["y","yes"]
no = ["n","not"]
response = None


def intro():
    print("Welcome to WORLD OF MAGIC")
    time.sleep(2)
    print("YOU ARE ABOUT TO ENTER THE MAGE'S QUEST!")
    time.sleep(1)
    print("What is your identity?")
    player = input("Enter Your Name: ").strip().upper()
    time.sleep(1)
    print("who is your Enemy?")
    Enemy = input("Enter name of youe Enemy: ").strip().upper()
    time.sleep(1)
    response = input("""Are you ready to enter the quest?
    Y/N:\n""").lower()
    if response in yes:
        scene1(player, Enemy)
        response = ""
    if response in no:
        response = None
        time.sleep(2)
        print (f" Become Stonger And Comeback To Complete The Quest Of Your Fate,{player}!")
        time.sleep(2)
        start()

def start():
    response = input("Do You Want To Start The Game? Y/N\n: ").lower()
    if response in yes :
        response =""
        intro()
    if response in no :
        response = None
        print("See you Next Time!\n")
        time.sleep(3)
        return start()
def scene1(player, Enemy):
    print(f"{player} you are in the middle of war against dark mage,{Enemy}.")
    time.sleep(1)
    print(f"You are a fourth year student of magic school.")
    time.sleep(1)
    print(f"you saw all your friends getting captured by demon servants")
    time.sleep(1)
    print(f"you are the only hope to save magic school now.")
    time.sleep(1)
    print(f"This your chance to show bravery and save entire magic kind from dark world.")
    time.sleep(1)
    print(f"you are hiding behind a wall ,you see your wand between wrakage.")
    time.sleep(1)
    print(f"You cast accio spell and get your wand back but {Enemy} saw wand flying towards you and sudenly appears in front of you.")
    time.sleep(1)
    print(f"{Enemy} casts crucio spell on you!")
    print("What will you do?")
    time.sleep(2)
    print("""    a] defend crucio with Noor spell
    b] Escape wearing invisiblity cloak 
    c] Surrender
    d] Quit game 
""")
    response = input("Enter you choice:(a/b/c/d)\n").strip().lower()
    if response == A:
        scene2a(player, Enemy)
    if response == B :
        scene2b(player)
    if response == C :
        death(player, Enemy)
    if response == D :
        time.sleep(1)
        print(f"THANKS FOR PLAYING THE GAME, {player}. I HOPE YOU ENJOYED IT!!!!")
        start()

def scene2a(player, Enemy):
    print(f"Noor speel worked! you have disarmed {Enemy}. {Enemy} is weakest without wand ")
    time.sleep(1)
    print("What will you do?")
    time.sleep(2)
    print(f"""    a] You use spell Aveda Cadevra
    b] you forgave dark mage and tell {Enemy} to leave
    d] Quit game 
""")
    response = input("Enter you choice:(a/b/c/d)\n").strip().lower()
    if response == A:
        time.sleep(1)
        print(f"The {Enemy} takes direct hit and dies!!!!")
        time.sleep(1)
        victory(player, Enemy)
    if response == B :
        print(f"{Enemy} does noi play by rule and in turn attacks you!!")
        death(player, Enemy)
    if response == D :
        time.sleep(1)
        print(f"THANKS FOR PLAYING THE GAME, {player}. I HOPE YOU ENJOYED IT!!!!")
        start()
def scene2b(player):
    print("You Escape School Wearing Cloak. But The school is distroyed!")
    print(" YOU HAVE FAILED THE QUEST!!!!!")
    print(f"THANKS FOR PLAYING THE GAME, {player}. I HOPE YOU ENJOYED IT!!!!")
    time.sleep(2)
    start()
def death(player, Enemy):
    print(f" the {Enemy} kills you with Aveda Cadevra spell")
    time.sleep(1)
    print(f"THANKS FOR PLAYING THE GAME, {player}. I HOPE YOU ENJOYED IT!!!!")
    start()
def victory(player, Enemy):
    print(f"{player},YOU HAVE DEFETED THE DARK MAGE {Enemy}.\nyou have saved mgic world and raised the honour of school!")
    print("you have earned the title:")
    print(f"THE SLAYER MAGE {player}")
    print(f"THANKS FOR PLAYING THE GAME, {player}. I HOPE YOU ENJOYED IT!!!!")
    start()
if response == None:
   start()