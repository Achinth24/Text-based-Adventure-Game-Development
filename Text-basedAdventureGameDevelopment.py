import time

def introduction():
    print("Welcome to Chronicles of the Lost Kingdom!")
    print("You are a brave adventurer on a quest to break the curse on Eldoria.")
    print("Your choices will determine the outcome of your journey.")

def make_choice(choices):
    print("\nChoose your path:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def forest_encounter():
    print("\nYou enter the eerie forest and encounter a mystical creature.")
    time.sleep(1)
    print("What do you do?")
    time.sleep(1)

    choices = ["Attempt to communicate.",
               "Draw your weapon and prepare for a fight."]
    choice = make_choice(choices)

    if choice == 1:
        print("\nThe creature seems to understand you and guides you deeper into the forest.")
    else:
        print("\nA fierce battle ensues, and you emerge victorious.")

def village_encounter():
    print("\nYou venture into the abandoned village and discover a hidden chamber.")
    time.sleep(1)
    print("Inside, there's a mysterious puzzle.")
    time.sleep(1)
    print("How do you proceed?")
    time.sleep(1)

    choices = ["Solve the puzzle.",
               "Ignore the puzzle and continue exploring."]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou successfully solve the puzzle, revealing a secret passage.")
    else:
        print("\nYou decide to explore further without solving the puzzle.")

def main():
    introduction()

    # Encounter 1: Forest
    forest_encounter()

    # Encounter 2: Village
    village_encounter()

    # Endings based on choices
    print("\nYour journey comes to an end.")
    print("Thank you for playing Chronicles of the Lost Kingdom!")

if __name__ == "__main__":
    main()
