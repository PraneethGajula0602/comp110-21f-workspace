"""Hope you survive!"""
__author__ = "730394749"

from random import randint

points: int = int()
player: str = str("")

CHANCE_OF_DYING: int = 2


def main() -> None:
    greet()
    play_again: bool = True
    while(play_again):
        enter_experience()
        print("You died with " + str(points) + " points! ")
        print("Thank you for playing! Would you like to play again?")
        entered: str
        entered = (input("Enter 'Y' to play again, or type 'N' or 'E' to exit "))
        while(input_is_bad(entered, "Y", "y", "n", "N")):
            entered = (input("Enter 'Y' to play again, or type 'N' or 'E' to exit "))
        play_again = (entered == "Y" or entered == "y")

    return None


def greet() -> None:
    """Greet the player."""
    print("Welcome to my game! I hope you survive!")
    global player
    player = input("Enter your name: ")
    return None


def enter_experience() -> None:
    """Start the game."""
    print("You've angered some very rich people. They will either set loose lions to kill you, or use a bomb to blow you up. You only have a moment - you see pliers and a gun next to you. Which do you pick?")
    entered: str = str(input("Type 'G' for the gun, 'P' for the pliers, or 'E' to exit the game. "))
    while(input_is_bad(entered, "G", "g", "P", "p")):
        entered = str(input("Type 'G' for the gun, 'P' for the pliers, or 'E' to exit the game. "))
    if(entered == "G" or entered == "g"):
        experience_gun()
    elif(entered == "P" or entered == "p"):
        experience_pliers()
    else:
        print("Exiting... ")
    return None


def input_is_bad(entered: str, option_one: str, option_two: str, option_three: str, option_four: str) -> bool:
    """Make sure player gives valid inputs."""
    return entered != option_one and entered != option_two and entered != option_three and entered != option_four and entered != "E" and entered != "e"


def experience_gun() -> None:
    """Player chooses gun."""
    print(player + " grabs the gun. It only has one bullet!")
    is_lion: bool = (randint(1, CHANCE_OF_DYING) == 1)
    if(is_lion):
        print("A lion bursts through the door! You shoot the lion at the last second and kill it! You get one point!")
        global points 
        points += 1
        print("The rich people are now going to send their goons to kill you, or they will tax you to death. You see piles of money and a sword next to you. Which do you choose?")
        entered: str = str(input("Type 'M' for the money, 'S' for the sword, or 'E' to exit. "))
        while(input_is_bad(entered, "S", "s", "g", "G")):
            entered = str(input("Type 'M' for the money, 'S' for the sword, or 'E' to exit. "))
        if(entered == "S" or entered == "s"):
            experience_sword()
        elif(entered == "M" or entered == "m"):
            experience_money()
    else:
        print("A bomb comes flying through the door. You die.")
    return None


def experience_sword() -> None:
    """Player chooses sword."""
    print(player + " grabs the sword. Let's hope this works! ")
    is_goons: bool = (randint(1, CHANCE_OF_DYING) == 1)
    if(is_goons):
        print("Some goons crash through the door! You kill them all with your sword! You get two points!")
        global points 
        points += 2
        print("The rich people are still angrily shouting. It feels like you're back at square one!")
        enter_experience()
    else:
        print("The IRS storms in and murders you for tax fraud! Was the lamborghini worth it? You die.")
    return None


def experience_money() -> None:
    """Player chooses money."""
    print(player + " grabs the money. Let's hope this works! ")
    is_tax: bool = (randint(1, CHANCE_OF_DYING) == 1)
    if(is_tax):
        print("The IRS storms in. You show them all your 'clean' money, they take it and leave. You get two points!")
        global points 
        points += 2
        print("The rich people are still angrily shouting. It feels like you're back at square one!")
        enter_experience()
    else:
        print("Some goons crash through the door and kill you gruesomely. You die. ")
    return None


def experience_pliers() -> None:
    """Player chooses pliers."""
    print(player + " grabs the pliers. Let's hope this works! ")
    is_bomb: bool = (randint(1, CHANCE_OF_DYING) == 1)
    if(is_bomb):
        print("A bomb comes flying through the door! You defuse the bomb at the last second! You get one point!")
        global points 
        points += 1
        print("The rich people are now going to send a lawsuit to kill you, or they will poison you with toxic gas. You see a mask and a lawyer next to you. Which do you choose?")
        entered: str = str(input("Type 'L' for the lawyer, 'M' for the mask, or 'E' to exit. "))
        while(input_is_bad(entered, "M", "L", "m", "l")):
            entered = str(input("Type 'L' for the lawyer, 'M' for the mask, or 'E' to exit. "))
        if(entered == "L" or entered == "l"):
            experience_lawyer()
        elif(entered == "M" or entered == "m"):
            experience_mask()
    else:
        print("A bomb comes flying through the door. You die.")
    return None


def experience_lawyer() -> None:
    """Player chooses lawyer."""
    print(player + " tells the lawyer that political science is a real science. He is now on your side! ")
    is_lawsuit: bool = (randint(1, CHANCE_OF_DYING) == 1)
    if(is_lawsuit):
        print("The supreme court judges run in and accuse you of having a bomb. The lawyer argues back that you don't know how bombs even work and couldn't defuse one to save your life. They find you innocent! You get two points! ")
        global points 
        points += 2
        print("The rich people are still angrily shouting. It feels like you're back at square one!")
        enter_experience()
    else:
        print("Poisonous gas seeps into the room. You and the lawyer die. ")
    return None


def experience_mask() -> None:
    """Player chooses mask."""
    print(player + " grabs the mask. Let's hope this works! ")
    is_gas: bool = (randint(1, CHANCE_OF_DYING) == 1)
    if(is_gas):
        print("Poisonous gas seeps into the room. You breathe it just fine, and survive! You get two points!")
        global points 
        points += 2
        print("The rich people are still angrily shouting. It feels like you're back at square one!")
        enter_experience()
    else:
        print("The supreme court runs in and finds you guilty for having a bomb! They kill you for it! You die. ")
    return None


if __name__ == "__main__": 
    main()