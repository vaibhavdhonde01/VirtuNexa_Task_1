import json
import os
import random
import logging

# Setup logging
logging.basicConfig(filename="game_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

SAVE_FILE = "savegame.json"

def get_user_choice(valid_choices):
    while True:
        choice = input("Enter your choice: ").strip()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please try again.")

def init_inventory():
    return []

def add_to_inventory(inventory, item):
    inventory.append(item)
    logging.info(f"Added to inventory: {item}")

def show_inventory(inventory):
    print("\nYour Inventory:")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("(empty)")

def combat_system():
    print("\nA wild goblin appears! Prepare for combat!")
    player_health = 20
    goblin_health = 15

    while player_health > 0 and goblin_health > 0:
        print(f"\nYour Health: {player_health} | Goblin's Health: {goblin_health}")
        print("1. Attack")
        print("2. Run")
        choice = get_user_choice(["1", "2"])

        if choice == "1":
            damage = random.randint(3, 7)
            goblin_health -= damage
            logging.info(f"Player attacks for {damage} damage.")
            print(f"You hit the goblin for {damage} damage!")
        else:
            print("You escaped from the battle!")
            logging.info("Player escaped from battle.")
            return False

        if goblin_health > 0:
            damage = random.randint(2, 5)
            player_health -= damage
            logging.info(f"Goblin attacks for {damage} damage.")
            print(f"The goblin strikes you for {damage} damage!")

    if player_health <= 0:
        print("\nYou were defeated by the goblin. Game over.")
        logging.info("Player was defeated in combat.")
        return False
    else:
        print("\nYou defeated the goblin!")
        logging.info("Player defeated the goblin.")
        return True

def forest_path(inventory):
    print("\nYou enter the forest and stumble upon a glowing sword stuck in a tree.")
    print("1. Take the sword")
    print("2. Ignore it and keep walking")
    choice = get_user_choice(["1", "2"])

    if choice == "1":
        add_to_inventory(inventory, "Glowing Sword")
        print("You have acquired a Glowing Sword!")
    else:
        print("You decide to move on cautiously.")

    # Encounter combat
    if not combat_system():
        return

    print("You reach a hidden cave. Inside you find a treasure chest.")
    print("1. Open it")
    print("2. Leave it alone")
    choice = get_user_choice(["1", "2"])

    if choice == "1":
        add_to_inventory(inventory, "Enchanted Gem")
        print("You found an Enchanted Gem!")
    else:
        print("You leave the cave quietly.")

    print("\nForest path adventure ends. Thanks for playing!")
    show_inventory(inventory)

def river_path(inventory):
    print("\nYou follow the river and find a mysterious old man fishing.")
    print("1. Talk to him")
    print("2. Steal his fish and run")
    choice = get_user_choice(["1", "2"])

    if choice == "1":
        print("The old man blesses you with a map to hidden treasure.")
        add_to_inventory(inventory, "Treasure Map")
    else:
        print("The old man curses you. You feel weak.")

    print("You continue and reach a bridge guarded by a troll.")
    print("1. Fight the troll")
    print("2. Bribe the troll with a fish")
    choice = get_user_choice(["1", "2"])

    if choice == "1":
        if not combat_system():
            return
    else:
        print("You bribe the troll and cross the bridge safely.")

    print("\nRiver path adventure ends. Thanks for playing!")
    show_inventory(inventory)

def start_game(inventory):
    print("You find yourself at the edge of a dark forest. Two paths lie ahead.")
    print("1. Take the forest path")
    print("2. Follow the river")
    choice = get_user_choice(["1", "2"])

    if choice == "1":
        forest_path(inventory)
    else:
        river_path(inventory)

def save_game(inventory):
    with open(SAVE_FILE, "w") as f:
        json.dump({"inventory": inventory}, f)
    print("Game saved successfully.")
    logging.info("Game saved.")

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            print("Game loaded successfully.")
            logging.info("Game loaded.")
            return data["inventory"]
    else:
        print("No saved game found.")
        return init_inventory()

def main():
    print("\n=== Welcome to the Text-Based Adventure Game: 'Legends of Eldoria' ===\n")
    print("1. Start New Game")
    print("2. Load Game")
    choice = get_user_choice(["1", "2"])

    if choice == "1":
        inventory = init_inventory()
    else:
        inventory = load_game()

    start_game(inventory)

    print("\nWould you like to save your progress? (y/n)")
    if input().strip().lower() == "y":
        save_game(inventory)

if __name__ == "__main__":
    main()
