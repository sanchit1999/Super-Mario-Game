# Python Terminal Mario

## Introduction
A game similar to popular Mario Game.

This game has been written using _Almost_ Vanilla Python. Important to note that the game has been tested on ONLY Linux-based OSs, and may not work on Windows.

## Structure

The application demonstrates inheritance, encapsulation, polymorphism and abstraction.
<!-- - Each "object" is a derived class of the `Object` class. -->
- Each player/enemy is a derived class of the `Character` class.
- The `board` has its own class and and captures all objects placed on it.

## Features and Gameplay

- Jumps have gravity like effect.
- Jump on enemies or fire towards them to kill them.
- Collect coins to get additional points.
- Jumping inside pits will lead to losing a chance.
- Getting hit by enemies or by boss fire will lead to losing a life.
- On losing a chance you will respawn with one less life.
- Jump on spring for higher jumps.

## Running the program

- Running the program is easy
	- `python3 main.py
  
## Controls

- Controls follow traditional classic titles (W,S,A,D)
- To fire `f` or `g`
- To quit, press `q`
