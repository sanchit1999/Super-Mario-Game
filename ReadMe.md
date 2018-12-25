Coded By : Sanchit Saini
Roll No : 20171191

The file has following sections :

1) Information about the game
2) Rules of the Game
3) Description of components created
4) Instructions of running the game
5) Requirements
6) SPECIAL FEATURES ADDED

1.   About the Game

	 Browse this link for info : https://en.wikipedia.org/wiki/Super_Mario_Bros.

2.   Rules of the game

	1) You control mario to cross various obstacles and fight enemies which lie in the way of protecting princess.
	2) You get bonus points and coins on the way, you can also kill enemies by jumping on them
	3) You get 5 lives and a timer to predict ur final score.
	4) In the end ,the boss enemy comes, the boss shoots bullets once you come in his line of sight.
	5) Boss is SMART and CHASES the mario character and shoots bullets in that direction.
	6) Boss can be killed by killing it with bullets, if you touch anywhere else, You lose a life. 

3.   Description

	1) Bridge Class : This class contains init as well as different functions for construction and movement of bridge.
	2) Enemy, Enemy1, BossEnemy classes : These classes handle various function and check functions for enemies.
	3) Board class : This class contains the basic structure for the board and various elements inside it.
	4) Background functions : These functions are used to print scenery using the coordinates given.
	5) Bullets class : This class handles the functioning of mario as well as boss enemy bullets.

4.   Instructions to play 

	Run the following command in the directory :

	1)python3 main.py

	2) Use the following controls:
		a) w,a,d,f,g to jump, move left, move right, shoot right and shoot left respectively.
		b) press q to quit the game

5.  Requirements

	1) Python3 

6.  Special Features 

	1) The boss enemy is smart and follows the character around wherever he goes and shoots in that direction.
	2) Springs around the boss to facilitate jumping above him.
	3) Bridge is also present in the game.

