# PythonLife

An interactive Conway's Game of Life simulation running on NumPy and Pygame.

<img width="1920" height="1063" alt="f7a5492a-d73e-4699-a540-76f1919ec61b" src="https://github.com/user-attachments/assets/23481b92-e8a4-4a94-bbb9-42619325f635" />

## Quick Start

### 1. Go to [github release](https://github.com/egraich/PythonLife/releases/tag/v1.0.0).
### 2. Download `PythonLife.exe` file.
### 3. Open it!

## Features

* **Interactive Canvas**: Left-click to draw living cells, right-click to clear them.
* **Time Controls**: Press Space to freeze time for building, and use keys 1, 2, or 3 to speed up or slow down the simulation loop on the fly.
* **Seamless Window Scaling**: Supports native window resizing and F11 borderless fullscreen. The simulation auto-extends on the fly, introducing random noise into newly opened space while preserving your existing patterns intact.
* **Separated Configuration**: All constants, visual styles, initial scale properties, and custom keybindings are completely isolated within `config.py`.

## Local Setup

### Requirements
* Python 3.10+
* NumPy
* Pygame

### Running the Project
1. Clone the repository or download the source files.
2. Install the required packages:
```bash
pip install -r requirements.txt
```
3. Start the application:
```bash
python main.py
```

## How It Works

Instead of using slow nested `for` loops to check every single cell one by one (which lags terribly on large screens), this project uses NumPy matrix math to update everything at once.

The code shifts the entire grid in 8 directions using `np.roll()` and adds them up. This counts the neighbors for all cells simultaneously. After that, it applies the game rules using basic array masking in a single step. It's way faster and keeps the FPS stable even in fullscreen mode.

## Credits

* Ruleset based on John Conway's Game of Life.
* Built using the Pygame framework and NumPy library.