# Conway's Game of Life 🧬

A terminal-based simulation of Conway's Game of Life — a classic cellular automaton — built in Python from scratch. This project allows random or user-defined starting grids, visualizes generations with Unicode blocks, and terminates on steady state or extinction.

## 🎯 Features

- Grid-based simulation with configurable size
- Clear visualization using `⬛` (alive) and `⬜` (dead) cells
- Command-line arguments for custom dimensions and iterations
- Detects steady-state (no change) and early extinction
- Easily extendable for oscillation detection or file-based seeding

## 🚀 How to Run

1. Clone this repo:

```bash
git clone https://github.com/your-username/conway-game-of-life.git
cd conway-game-of-life
python3 conway_game_of_life.py -r 10 -c 10 -n 4

```
Beginning the game ...

⬜⬛⬛⬛⬜⬛⬜⬛⬜⬛<br>
⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜<br>
⬛⬛⬜⬛⬜⬜⬛⬜⬜⬜<br>
⬛⬛⬜⬛⬛⬜⬜⬛⬛⬜<br>
⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜<br>
⬛⬜⬜⬛⬜⬜⬜⬜⬛⬜<br>
⬛⬜⬛⬜⬜⬛⬜⬛⬜⬜<br>
⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜<br>
⬛⬛⬜⬜⬛⬜⬜⬛⬜⬛<br>
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛<br>
The total number of alive cells are 50

Generation: 1<br>
⬜⬛⬛⬛⬜⬛⬛⬜⬜⬜<br>
⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜<br>
⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜<br>
⬛⬛⬜⬛⬛⬛⬜⬜⬛⬜<br>
⬛⬛⬛⬛⬛⬜⬛⬜⬜⬜<br>
⬜⬛⬜⬜⬜⬜⬜⬜⬛⬜<br>
⬛⬜⬛⬜⬜⬛⬜⬜⬜⬜<br>
⬛⬜⬛⬜⬛⬜⬜⬜⬜⬜<br>
⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛<br>
⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛<br>
The total number of alive cells are 40

Generation: 2<br>
⬜⬛⬛⬜⬛⬛⬛⬜⬜⬜<br>
⬜⬛⬛⬜⬛⬛⬜⬛⬜⬜<br>
⬛⬛⬜⬜⬜⬜⬛⬛⬜⬜<br>
⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜<br>
⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜<br>
⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜<br>
⬛⬜⬛⬛⬜⬜⬜⬜⬜⬜<br>
⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜<br>
⬛⬜⬜⬜⬜⬜⬛⬜⬛⬜<br>
⬛⬛⬛⬛⬛⬛⬛⬜⬛⬜<br>
The total number of alive cells are 34

Generation: 3<br>
⬜⬛⬛⬜⬛⬜⬛⬜⬜⬜<br>
⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜<br>
⬛⬜⬛⬜⬜⬛⬛⬛⬜⬜<br>
⬛⬛⬜⬜⬜⬜⬛⬛⬜⬜<br>
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜<br>
⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜<br>
⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜<br>
⬛⬜⬛⬛⬜⬜⬜⬜⬜⬜<br>
⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜<br>
⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜<br>
The total number of alive cells are 32

Generation: 4<br>
⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜<br>
⬜⬜⬛⬜⬛⬜⬜⬛⬜⬜<br>
⬛⬜⬜⬜⬜⬛⬜⬜⬛⬜<br>
⬛⬛⬜⬜⬜⬛⬜⬛⬜⬜<br>
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜<br>
⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜<br>
⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜<br>
⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜<br>
⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜<br>
⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜<br>
The total number of alive cells are 26

Game over
