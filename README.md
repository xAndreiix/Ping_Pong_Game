# Ping Pong Game 🎮

A classic two-player Ping Pong game built using Python and Pygame. The game features smooth paddle controls, dynamic ball physics, and real-time score tracking.

## Features

- Two-player mode: left paddle (W/S) and right paddle (UP/DOWN)
- Real-time score display
- Ball bouncing mechanics with collision detection
- Automatic ball reset and score increment when out of bounds

## Project Structure

```
ping_pong_game/
├── ping_pong_game.py      # Main game file
├── test_ping_pong_game.py # Unit tests for game components
├── .gitignore             # Ignored files and folders
├── LICENSE                # MIT License
└── README.md              # Project documentation
```

## Requirements

- Python 3.7+
- Pygame

To install Pygame:

```bash```
pip install pygame

## How to Run

```bash```
python ping_pong_game.py


## How to Test

```bash```
python -m unittest test_ping_pong_game.py