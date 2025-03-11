# Turtle Crossing Game

A simple Python game built using the `turtle` module, where the player controls a turtle trying to cross a busy road while avoiding cars. This project is inspired by the classic Frogger game.

## Features

- Player-controlled turtle movement using arrow keys.
- Randomly moving cars at different speeds.
- Increasing difficulty as the game progresses.
- Simple and colorful graphical interface.

## Installation

Ensure you have Python installed (version 3.x recommended). Clone this repository and run the script:

```sh
# Clone the repository
git clone https://github.com/IsaWng/python-turtle-crossing.git
cd python-turtle-crossing

# Run the game
python main.py
```

## How to Play

- Use the **Up Arrow Key** (`↑`) to move the turtle forward.
- Reach the top of the screen to win the level.
- Avoid getting hit by moving cars.
- Each level increases car speed, making the game more challenging.

## Project Structure

```
python-turtle-crossing/
│── main.py           # Main game loop
│── player.py         # Player (turtle) movement logic
│── car_manager.py    # Car behavior and traffic system
│── scoreboard.py     # Score and level display
│── README.md         # Project documentation
```

## Requirements

This game runs with Python's built-in `turtle` module, so no extra dependencies are needed.

## Contributing

Feel free to fork this repository and submit pull requests if you have improvements or bug fixes.

## License

This project is open-source and available under the MIT License.

---

Enjoy playing Turtle Crossing! 🐢🚗

