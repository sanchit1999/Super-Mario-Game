import os
from mario import Mario, newboard, Bullets_arr
import time
from background import printbricks1, printbricks2, printCloud1, printCloud2, printMountain1, printMountain2, printMountain3, printpipe1, printpit, printcave, printstairs,printrevstairs, printpipe2, printcoins, printbullets, printspring
from enemy import Enemy, Enemy1, BossEnemy
from bridge import Bridge

enemy_arr = []
obj = Mario()
bridg = Bridge(1113)    
obj.printMario()
boss = BossEnemy(1260)    

newboard.printBoard(obj, boss)
enemy_arr.append(Enemy(135, 30))
enemy_arr.append(Enemy1(545, 40))
enemy_arr.append(Enemy(585, 40))
enemy_arr.append(Enemy1(920, 40))
enemy_arr.append(Enemy(950, 40))
enemy_arr.append(Enemy(230, 22))
enemy_arr.append(Enemy(260, 22))
enemy_arr.append(Enemy(305, 22))
enemy_arr.append(Enemy(340, 22))
enemy_arr.append(Enemy(970, 40))

for i in enemy_arr :
	i.printenemy()
for i in range(35, 5000, 80) :
	printCloud1(i, newboard)
for i in range(80, 5000, 80) :
	printCloud2(i, newboard)	
pipe1_arr = [530, 980]
pipe2_arr = [590, 910]
pit_arr = [700, 1110]
stairs_arr = [800, 1090]
rev_stairs_arr = [830, 1135]
bricks2_arr = [80, 540]
coins_arr1 = [84, 92, 102, 112, 120, 230, 362, 930, 960]
coins_arr2 = [25, 25, 25, 25, 25, 22, 22, 46, 46]
bullets_arr1 = [260, 300, 330, 826, 566]
bullets_arr2 = [22, 22, 22, 46, 46]
spring_arr = [215, 372]

for i in pipe1_arr :
	printpipe1(i,newboard)
for i in pipe2_arr :
	printpipe2(i, newboard)
for i in pit_arr :
	printpit(i, newboard)
for i in stairs_arr :
	printstairs(i, newboard)
for i in rev_stairs_arr :
	printrevstairs(i, newboard)
for i in bricks2_arr :
	printbricks2(i, newboard)
for i in spring_arr :
	printspring(i, newboard)		
printcave(220, newboard)
printcoins(84, 25, newboard)
printcoins(92, 25, newboard)
printcoins(102, 25, newboard)
printcoins(112, 25, newboard)
printcoins(120, 25, newboard)
printcoins(230, 22, newboard)
printcoins(362, 22, newboard)
printbullets(260, 22, newboard)
printbullets(300, 22, newboard)
printbullets(330, 22, newboard)
printbullets(826, 46, newboard)
printcoins(930, 46, newboard)
printcoins(960, 46, newboard)
printbullets(566, 46, newboard)

def checkcollission() :
	
	for i in enemy_arr :
		for j in Bullets_arr :
			if(j.direction == 1) :
				if ( j.x == i.head_xcoord - 1 and j.y == i.head_ycoord ) :
					i.clearenemy()
					j.clearbullets(newboard)
					enemy_arr.remove(i)
					Bullets_arr.remove(j)

				if ( j.x == boss.llbody_xcoord - 1 and j.y <= boss.legs_ycoord and j.y >= boss.head_ycoord and boss.health > 0) :
					boss.health -= 1
					j.clearbullets(newboard)
					Bullets_arr.remove(j)
			else :
				if (newboard.grid[ j.y ][ j.x - 1] == chr(9608)) :
					j.clearbullets(newboard)
					Bullets_arr.remove(j)
					break

				else :	
					if ( j.x == i.head_xcoord + 4 and j.y == i.head_ycoord ) :
						j.clearbullets(newboard)
						i.clearenemy()
						enemy_arr.remove(i)
						Bullets_arr.remove(j)
						break

				if ( j.x == boss.llbody_xcoord + 4 and j.y <= boss.legs_ycoord and j.y >= boss.head_ycoord and boss.health > 0) :
					boss.health -= 1
					j.clearbullets(newboard)
					Bullets_arr.remove(j)
					break

	if (boss.health == 0) :
		boss.alive = 0
		boss.clearenemy()		

def check_mario_collission() :

	if(obj.legs_ycoord >= boss.head_ycoord and obj.head_ycoord <= boss.legs_ycoord) :
		if(obj.legs_xcoord + newboard.curr_pos + 5 == boss.legs_xcoord or obj.legs_xcoord + newboard.curr_pos - 2 == boss.legs_xcoord + 4) :
			obj.lives -= 1

	if(obj.lives == 0) :
		print("GAME OVER")
		print("YOUR SCORE :", str(obj.score))
		quit()	
	for i in Bullets_arr :

		if(i.source == 1) :
			if(i.y >= obj.head_ycoord and i.y <= obj.legs_ycoord) :
				if(i.x == obj.legs_xcoord + newboard.curr_pos + 4 or i.x == obj.legs_xcoord + newboard.curr_pos - 1 and obj.lives > 0) :
					i.clearbullets(newboard)
					Bullets_arr.remove(i)
					obj.lives -= 1
					
		if(obj.lives == 0) :
			print("GAME OVER")
			print("YOUR SCORE :", str(obj.score))
			quit()


def checkrange() :

	for i in Bullets_arr :
		if (i.x < i.range_begin or i.x > i.range_end) :
			i.clearbullets(newboard)
			Bullets_arr.remove(i)

while True :

	os.system("tput reset")
	printbricks1(65, newboard)
	printbricks1(129, newboard)
	printMountain1(150, newboard)
	printMountain2(400, newboard)
	printMountain3(620, newboard)
	printMountain3(1040, newboard)		
	bridg.movebridge(newboard)
	
	newboard.printBoard(obj, boss)

	for j in enemy_arr :
		
		if (obj.legs_ycoord == j.head_ycoord - 1 and obj.legs_xcoord + newboard.curr_pos + 1 >= j.head_xcoord and obj.legs_xcoord + newboard.curr_pos + 1 <= j.head_xcoord + 3 and obj.legs_xcoord + newboard.curr_pos + 2 >= j.head_xcoord and obj.legs_xcoord + newboard.curr_pos + 2 <= j.head_xcoord + 3) :
			j.clearenemy()
			enemy_arr.remove(j)
			obj.score += 100

		if ( ((obj.legs_xcoord + newboard.curr_pos + 4 == j.legs_xcoord or obj.legs_xcoord + newboard.curr_pos - 1 == j.legs_xcoord + 4) and obj.legs_ycoord >= j.head_ycoord and obj.head_ycoord < j.legs_ycoord) or obj.legs_ycoord == 58 ) :
			obj.lives -= 1
			if (obj.lives == 0) :
				print("GAME OVER")
				print("YOUR SCORE :", str(obj.score))
				quit()
			else :
				if (newboard.curr_pos == 0) :
					obj.clearMario()
					obj.legs_xcoord -= 60
					obj.legs_ycoord = 32
					obj.body_xcoord -= 60
					obj.body_ycoord = 31
					obj.head_xcoord -= 60
					obj.head_ycoord = 30
				else :
					obj.clearMario()
					newboard.curr_pos -= 60
					obj.legs_ycoord = 32	
					obj.body_ycoord = 31
					obj.head_ycoord = 30
			
	obj.moveMario(bridg)
	
	if (boss.alive == 1) :
		if (obj.legs_xcoord + newboard.curr_pos > 1400) :
			obj.clearMario()
			newboard.curr_pos = 1313
			obj.printMario()
	
	for i in Bullets_arr :
		
		checkcollission()
		if(len(Bullets_arr) == 0) :
			break
		checkrange()
		i.movebullets(newboard)
		i.print_bullets(newboard)
	
	if (boss.alive == 1) :
		boss.moveenemy(obj)
		boss.shootmario(obj)
		check_mario_collission()

	for j in enemy_arr :
			j.moveenemy()