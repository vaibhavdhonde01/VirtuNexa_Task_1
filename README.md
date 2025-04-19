# VirtuNexa_Task_1
#Adventure Game

# Documentation: Legends of Eldoria - Text-Based Adventure Game

## Overview
"Legends of Eldoria" is a text-based adventure game built using Python. It immerses players in a fantasy world where their choices shape the story. The game features inventory management, multiple story paths, a combat system, and persistent save/load functionality.

---

## Features

### 1. Interactive Gameplay
- Users make choices to navigate through different scenarios.
- Each decision leads to a different path or consequence.

### 2. Inventory Management
- Players collect items like weapons, maps, and treasures.
- The inventory persists during gameplay and can be viewed anytime.

### 3. Combat System
- Simple turn-based battles against enemies like goblins and trolls.
- Uses random damage values to determine the outcome of attacks.

### 4. Save and Load Game
- Players can save their progress to a file (`savegame.json`).
- Players can load a previous session and continue from where they left off.

### 5. Logging
- All player actions and events are logged to a file named `game_log.txt`.
- Useful for debugging or reviewing game sessions.

---

## Setup Instructions

### Requirements
- Python 3.7 or above

### Installation
1. Clone or download the project folder.
2. Ensure the following files are present:
    - `gane.py` (main game script)
3. Optional: If starting from scratch, install any necessary modules using:
```bash
pip install -r requirements.txt
```
*(Note: This game uses only standard libraries, so external dependencies are not required.)*

---

## How to Run
1. Open a terminal or command prompt.
2. Navigate to the project folder where `game.py` is saved.
3. Run the script using:
```bash
python game.py
```

---

## Usage Instructions

### Starting the Game
- Choose to start a new game or load a previously saved game.

### Making Choices
- At each prompt, enter the number corresponding to your chosen action (e.g., `1`, `2`).

### Combat
- Select "Attack" to damage the enemy.
- You can also choose to "Run" and skip combat.

### Saving Progress
- At the end of the game, you’ll be prompted to save your progress.

### Loading a Saved Game
- On the start screen, choose the option to load a game. It will read from `savegame.json`.

---

## Files Generated
- `savegame.json`: Contains player inventory and game state.
- `game_log.txt`: Logs all user actions and events.

---

## Optional Enhancements (Future Scope)
- Graphical UI using Tkinter
- More complex story arcs and endings
- Puzzle-solving elements
- Multiple save slots
- Leveling system and character stats

---

## Credits
Developed by Vaibhav

---

## License
This project is open for educational and non-commercial use.


