# Ping Pong Game

## Overview
Welcome to the Ping Pong Game! This project is a fun and interactive implementation of the classic ping pong game using Pygame, a Python library for game development. It features two-player paddle control, a bouncing ball, scoring mechanics, light/dark mode options, and a game-over screen for an enjoyable gaming experience.

## Features
- **Two-Player Gameplay**: Control paddles with keyboard keys (Arrow Keys for Player 1, W/S for Player 2).
- **Ball Dynamics**: The ball's speed increases upon hitting a paddle, and it changes direction dynamically based on collisions.
- **Modes**: Choose between Light and Dark mode for enhanced visual preference at the start of the game.
- **Score Tracking**: Keep track of player scores displayed on-screen.
- **Game Over Screen**: Displays the final scores when a player wins, along with a short delay before exiting.

## Gameplay Instructions
1. **Choose a Mode**: At the start of the game, select Light or Dark mode by pressing L or D on the keyboard.
2. **Control the Paddles**:
    - **Player 1**: Use the Up and Down arrow keys to move the paddle vertically.
    - **Player 2**: Use the W (up) and S (down) keys to control the paddle.
3. **Start the Game**: Press the **Spacebar** to start moving the ball.
4. **Scoring**: Players earn points when their opponent fails to hit the ball, allowing it to pass beyond their paddle.
5. **Win Condition**: First player to reach the target score wins (default: 3 points).
6. **Game Over**: View the final scores and the “Game Over” message when the game ends.

## Project Structure
```
Ping_pong/
├── src/ # Source code files.
│    ├── config.py # Configuration settings for the project.
│    ├── main.py # Main access point to the program.
│    └── ping_pong.py # Main script for the game logic.
├── .gitignore # Specifies files and directories to ignore in Git.
├── LICENSE # License information for the project.
├── README.md # Documentation and overview of the project.
└── requirements.txt # Dependencies required for the project.
```

## Code Architecture
The `PingPong` class encapsulates all game mechanics. Below is a summary of the main methods:

- `__init__()`: Initializes game objects like paddles, ball, scores, mode, and more.
- `draw_objects()`: Renders paddles and ball on the screen.
- `move_paddle()`: Updates paddle positions based on player input and ensures boundary checks.
- `check_collision()`: Detects collision between paddles and the ball.
- `reset_ball_position()`: Resets the ball’s position after each round with random initial directions.
- `reset_paddle_position()`: Returns paddles to their starting positions.
- `show_scores()`: Displays player scores.
- `show_game_over_message()`: Renders the “Game Over” message and final scores.
- `set_mode()`: Allows the player to select Light or Dark mode.
- `play()`: The main game loop for handling input, collisions, rendering, and game logic.

## Usage
**Clone the Repository**: Open your terminal and run the following command to clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
```
Replace **your-username** and **your-repo** with the actual GitHub username and repository name.

Navigate to the main project directory and add the current working directory to `PYTHONPATH`:
```bash
cd Ping_pong
export PYTHONPATH=$(pwd)
```
Install neccessary libraries.
```bash
pip install -r requirements.txt
```
Run the script to run the game.
```bash
python src/main.py
```

## Customization
You can modify several aspects of the game by editing the constants in `src/config.py` (example: `PADDLE_WIDTH`, `BALL_SPEED`, `SCREEN_HEIGHT`, etc.). For example:
- Change target score by editing the `target_round` variable in the `play()` method.
- Customize the colors of paddles, ball, and background by updating the color constants.

## License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.
