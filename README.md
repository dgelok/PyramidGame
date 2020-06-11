# Pyramid Game

Pyramid Game is a python-based RPG to be run on the command line. This is a self-guided educational project, and my version of exercise 45 from Zed Shaw's *Learn Python the Hard Way* (found [here](https://www.amazon.com/Learn-Python-Hard-Way-Introduction/dp/0134692888/ref=sr_1_1?keywords=python+the+hard+way&qid=1577465107&sr=8-1)).

In developing Pyramid Game, my goals were as follows:
- write using classes / familiarize with OOP concepts
- finish a large (200+ lines) independent project 
- work with Git/GitHub more
- make it more user-friendly than the previous game ([Zorklon5](https://github.com/dgelok/Zorklon5)) 


## Developed by

Dan Gelok

[email me](dgelok@gmail.com) / [github](https://github.com/dgelok)


## Requirements

- Python3 or later (built on Python3.8)
- random, textwrap, and sys modules


## To run

- On Mac Terminal: `python3 pyramidGame.py`
- On Windows Command Line: `python pyramidGame.py`


## Similar projects

I've designed two more text-based RPG games that are similar in concept; [heroRPG](https://github.com/dgelok/heroRPG) and [Zorklon 5](https://github.com/dgelok/zorklon5). HeroRPG is more developed and utilizes OOP principles, and was made as part of DigitalCrafts curriculum (June 2020 Houston cohort). 


## How it works

| Feature | Description |
| ----------- | ----------- |
| Rooms | Rooms are objects with an enter() method. When this method is called, the player is described a scenario and makes a multiple-choice selection. Based on that choice, the function returns the next room to get to - either progressing linearly through the rooms of the game, dying, or replaying the current room. |
| Engine | The Engine is a class designed to take a Room class object as an argument. The engine runs the room class's enter() method, takes the next room that is returned from that method, and then runs the enter() method on whatever was returned from the previous room. |
| Death | Death is a room that can be entered from any other room, and it has a series of snarkly clips that make fun of the user for dying. It then exits the main program.|
| Winning | Since each room naturally only leads successfully to one other room, there is only one 'path' that users can take through the rooms. Upon reaching the last room and answering the question properly, they are sent to the final room and beat the game. |


