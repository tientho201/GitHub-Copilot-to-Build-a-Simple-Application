import sys
import time

def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def intro():
    slow_print("=" * 55)
    slow_print("🌲 WELCOME TO THE MYSTERIOUS FOREST ADVENTURE 🌲")
    slow_print("=" * 55)
    slow_print("You wake up at the crossroads of an enchanted ancient forest.")
    slow_print("There are two paths ahead of you:")
    slow_print("1. Take the left path into the Whispering Cavern.")
    slow_print("2. Take the right path across the Misty River Bridge.")
    choice = input("\nWhich path do you choose? (1 or 2): ").strip()
    
    if choice == "1":
        cavern_path()
    elif choice == "2":
        bridge_path()
    else:
        slow_print("Invalid choice. You wander in circles and find yourself back at start.")
        intro()

def cavern_path():
    slow_print("\nInside the cavern, you spot a chest gleaming under crystal lights.")
    slow_print("Beside it lies a slumbering dragon.")
    slow_print("1. Sneak past quietly to loot the chest.")
    slow_print("2. Cast a sleep spell to ensure the dragon stays asleep.")
    choice = input("\nYour move? (1 or 2): ").strip()

    if choice == "1":
        slow_print("You open the chest quietly and retrieve the Sun Amulet! You escaped rich! 🏆")
    elif choice == "2":
        slow_print("The spell backfires, waking the dragon! You barely escape with your life. 🏃💨")
    else:
        cavern_path()

def bridge_path():
    slow_print("\nThe wooden bridge creaks ominously above a roaring chasm.")
    slow_print("A mysterious cloaked stranger stands at the midpoint.")
    slow_print("1. Answer the stranger's riddle.")
    slow_print("2. Try to sprint past him.")
    choice = input("\nWhat will you do? (1 or 2): ").strip()

    if choice == "1":
        answer = input("\nStranger asks: 'What has keys but no locks?' ").strip().lower()
        if "piano" in answer or "keyboard" in answer:
            slow_print("The stranger bows and grants you safe passage to the Golden Citadel! 🏰✨")
        else:
            slow_print("Wrong answer! The bridge collapses into water, but you swim ashore safely.")
    elif choice == "2":
        slow_print("You slip on the mossy planks, but manage to grapple across to the other side!")
    else:
        bridge_path()

if __name__ == "__main__":
    intro()