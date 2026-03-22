# Terminal Souls 🧾
## System description 🧩
This program simulates a turn-based battle between a hero and an enemy.
The player can attack, heal themselves, or use a special ability, while the enemy responds automatically.

## System logic ⚙️
The game runs in loops.
In each loop:

- The player chooses an action
- Effects (damage or healing) are applied
- The game checks to see if anyone has been defeated
- If the game continues, the enemy attacks
- The game checks the current status again
- The current status (HP) is displayed

## Main functions 🧠
1. generate_damage (): Generates a random damage value within a range.

2. player_turn (): Handles the player's turn.
Allows the player to choose between attacking, healing, or using a special ability.
Returns the updated health and potion values.

3. enemy_turn (): Automatically deals damage to the player.

4. verify_winner (): Checks whether the player or the enemy has lost all their health.
If either reaches 0, the game ends.

5. show_state (): Displays the current health of the hero and the enemy on the screen.

## Rule's program 🎮

- The hero starts with 100 HP
- The enemy starts with 120 HP
- The player has 3 potions
- Each action affects the health points
- The game ends when a player reaches 0 HP

[Ver diagrama](Terminal_souls.drawio.pdf)