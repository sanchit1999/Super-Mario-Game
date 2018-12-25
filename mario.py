import signal
from board import Board
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from bullets import Bullets
import time

newboard = Board()
Bullets_arr = []

class Mario:

	def __init__(self) :

		self.head_xcoord = 15
		self.head_ycoord = 44
		self.body_xcoord = 15
		self.body_ycoord = 45
		self.legs_xcoord = 15
		self.legs_ycoord = 46
		self.flag = 0
		self.lives = 5
		self.coins_collected = 0
		self.score = 0
		self.bullets = 35
		self.curr_time = time.time()

	def printMario(self) :

		newboard.grid [ self.head_ycoord ][ newboard.curr_pos + self.head_xcoord ] = ']'
		newboard.grid [ self.head_ycoord ][ newboard.curr_pos + self.head_xcoord + 1 ] = 'M'
		newboard.grid [ self.head_ycoord ][ newboard.curr_pos + self.head_xcoord + 2 ] = 'M'
		newboard.grid [ self.head_ycoord ][ newboard.curr_pos + self.head_xcoord + 3 ] = '['
		newboard.grid [ self.body_ycoord ][ newboard.curr_pos + self.body_xcoord ] = '|'
		newboard.grid [ self.body_ycoord ][ newboard.curr_pos + self.body_xcoord + 3 ] = '|'
		newboard.grid [ self.legs_ycoord ][ newboard.curr_pos + self.legs_xcoord + 1 ] = '/'
		newboard.grid [ self.legs_ycoord ][ newboard.curr_pos + self.legs_xcoord + 2 ] = '\\'

	def clearMario(self) :

		newboard.grid [ self.head_ycoord ][ newboard.curr_pos + self.head_xcoord ] = ' '
		newboard.grid [ self.head_ycoord ][ newboard.curr_pos + self.head_xcoord + 1 ] = ' '
		newboard.grid [ self.head_ycoord ][ newboard.curr_pos + self.head_xcoord + 2 ] = ' '
		newboard.grid [ self.head_ycoord ][ newboard.curr_pos + self.head_xcoord + 3 ] = ' '
		newboard.grid [ self.body_ycoord ][ newboard.curr_pos + self.body_xcoord ] = ' '
		newboard.grid [ self.body_ycoord ][ newboard.curr_pos + self.body_xcoord + 3 ] = ' '
		newboard.grid [ self.legs_ycoord ][ newboard.curr_pos + self.legs_xcoord + 1 ] = ' '
		newboard.grid [ self.legs_ycoord ][ newboard.curr_pos + self.legs_xcoord + 2 ] = ' '

	def check(self) :

		check_flag = -1
		val = self.head_xcoord + newboard.curr_pos

		for i in range(val, val + 4) :
			if(not(newboard.grid[ self.legs_ycoord + 1 ][ i ] == ' ' or newboard.grid[ self.legs_ycoord + 1 ][ i ] == '/' or newboard.grid[ self.legs_ycoord + 1 ][ i ] == '\\')) :
				check_flag = 0
				break

		if (check_flag == -1) :
			self.head_ycoord += 1
			self.body_ycoord += 1	
			self.legs_ycoord += 1
			return 1

		return 0					

	def moveMario(self, bridg) :

		def alarmhandler(signum, frame):
				raise AlarmException
		
		def user_input(timeout=0.1) :

			signal.signal(signal.SIGALRM, alarmhandler)
			signal.setitimer(signal.ITIMER_REAL, timeout)
			try:
				text = getChar()()
				signal.alarm(0)
				return text
			except AlarmException:
				pass
			signal.signal(signal.SIGALRM, signal.SIG_IGN)
			return ''
		char = user_input()

		if (newboard.grid[ self.legs_ycoord ][ self.legs_xcoord + newboard.curr_pos + 3 ] == chr(9400) and newboard.coins_freq[self.legs_ycoord ][self.legs_xcoord + newboard.curr_pos + 3 ] == 1 ) :
			self.score += 50
			newboard.coins_freq[ self.legs_ycoord ][ self.legs_xcoord + newboard.curr_pos + 3 ] = 0	
		
		if( newboard.grid[ self.legs_ycoord ][ self.legs_xcoord + newboard.curr_pos - 2 ] == chr(9400) and newboard.coins_freq[self.legs_ycoord ][self.legs_xcoord + newboard.curr_pos - 2 ] == 1 ) :
			self.score += 50
			newboard.coins_freq[ self.legs_ycoord ][ self.legs_xcoord + newboard.curr_pos - 2 ] = 0
		
		if ( newboard.grid[ self.legs_ycoord ][ self.legs_xcoord + newboard.curr_pos + 5 ] == chr(9728) and newboard.bullet_freq[self.legs_ycoord ][ self.legs_xcoord + newboard.curr_pos + 5 ] == 1 ) :
			self.bullets += 5
			newboard.bullet_freq[self.legs_ycoord ][ self.legs_xcoord + newboard.curr_pos + 5 ] = 0

		if ( newboard.grid[ self.legs_ycoord ][ self.legs_xcoord + newboard.curr_pos - 2 ] == chr(9728) and newboard.bullet_freq[self.legs_ycoord ][ self.legs_xcoord + newboard.curr_pos - 2 ] == 1 ) :
			self.bullets += 5
			newboard.bullet_freq[self.legs_ycoord ][ self.legs_xcoord + newboard.curr_pos - 2 ] = 0
			
		if (char == 'q') :
			print("GAME OVER")
			print("YOUR SCORE :", str(self.score))
			quit()

		if (char == 'w' or char == 'a' or char == 'd') :
			self.clearMario()

		self.flag = 0

		if (char == 'w' and self.head_ycoord > 8) :
			
			check_flag = -1
			val = self.head_xcoord + newboard.curr_pos
	
			for j in range(val, val + 4):

				for i in range(self.head_ycoord - 1, self.head_ycoord - 9, -1) :
					
					if (not(newboard.grid[ i ][ j ] == ' ' or newboard.grid[ i ][ j ] == '/' or newboard.grid[ i ][ j ] == '\\' or newboard.grid[ i ][ j ] == chr(9400))) :
						check_flag = i
						break
				if (not(check_flag == -1 )) :
					break		

			if (check_flag == -1) :
				if (self.legs_ycoord > 28) : 

					self.head_ycoord -= 8
					self.body_ycoord -= 8	
					self.legs_ycoord -= 8

			else :
				self.head_ycoord = check_flag + 1
				self.body_ycoord = check_flag + 2
				self.legs_ycoord = check_flag + 3

			self.flag = 1

		if (char == 'a' and self.legs_xcoord > 11) :
			
			check_flag = -1
			val = self.head_xcoord + newboard.curr_pos
		
			for i in range(self.head_ycoord, self.legs_ycoord + 1):

				for j in range(val - 1, val - 3, -1) :
					if (not(newboard.grid[ i ][ j ] == ' ' or newboard.grid[ i ][ j ] == '/' or newboard.grid[ i ][ j ] == '\\' or newboard.grid[ i ][ j ] == chr(9400) or newboard.grid[ i ][ j ] == chr(9728) )) :
						check_flag = j
						break
				if (not(check_flag == -1 )) :
					break

			if (check_flag == -1) :
				if (self.legs_xcoord < 86) :
					self.head_xcoord -= 2
					self.body_xcoord -= 2
					self.legs_xcoord -= 2

				else :	
					newboard.curr_pos -= 2	

			self.flag = 2				

		if (char == 'd') :

			check_flag = -1
			val = self.head_xcoord + newboard.curr_pos
			self.score += 5
			for i in range(self.head_ycoord, self.legs_ycoord + 1) :

				for j in range(val + 4, val + 6) :

					if (not(newboard.grid[ i ][ j ] == ' ' or newboard.grid[ i ][ j ] == '\\' or newboard.grid[ i ][ j ] == '/' or newboard.grid[ i ][ j ] == chr(9400) or newboard.grid[ i ][ j ] == chr(9728) )) :
						check_flag = j
						break
				if (not(check_flag == -1 )) :
					break

			if (check_flag == -1) :
				if (self.legs_xcoord < 86) :
					self.head_xcoord += 2
					self.body_xcoord += 2
					self.legs_xcoord += 2

				else :	
					newboard.curr_pos += 2

			self.flag = 3										

		if (not(self.flag == 1)) :	
			if (not(self.legs_ycoord == 46)) :
				self.clearMario()	
			self.check()

		if (not(self.flag == 0)):
			
			x = self.head_xcoord + newboard.curr_pos
			newboard.freq[ self.head_ycoord ][ x ] -= 1
			if( newboard.grid[ self.head_ycoord - 1][ x ] <= '6' and newboard.grid[self.head_ycoord - 1 ][ x ] >= '0') :
				self.score += 20	

		if(newboard.grid[self.legs_ycoord + 1][self.legs_xcoord + newboard.curr_pos + 1 ] == chr(9776) or newboard.grid[ self.legs_ycoord + 1 ][ self.legs_xcoord + newboard.curr_pos + 3] == chr(9776)) :
			self.clearMario()
			self.head_ycoord -= 20
			self.body_ycoord -= 20
			self.legs_ycoord -= 20	

		if (newboard.grid[ self.legs_ycoord + 1 ][ self.legs_xcoord + newboard.curr_pos + 1 ] == chr(9993)) :
			if(bridg.direction == 1) :
				if(bridg.y >= 31) :
					self.clearMario()
					self.head_ycoord -= 1
					self.body_ycoord -= 1
					self.legs_ycoord -= 1
				else :
					self.clearMario()
					self.head_ycoord -= 2
					self.body_ycoord -= 2
					self.legs_ycoord -= 2	

			else :
					self.clearMario()
					self.head_ycoord += 2
					self.body_ycoord += 2
					self.legs_ycoord += 2			

		self.printMario()

		if (char == 'f') :

			if (self.bullets > 0) :
				temp_bullet = Bullets(self.body_xcoord + newboard.curr_pos + 4, self.body_ycoord, self.body_xcoord + newboard.curr_pos + 4, self.body_xcoord + newboard.curr_pos + 74, 1, 0)
				Bullets_arr.append(temp_bullet)
				self.bullets -= 1

		if (char == 'g') :

			if (self.bullets > 0) :
				temp_bullet = Bullets(self.body_xcoord + newboard.curr_pos - 1, self.body_ycoord, self.body_xcoord + newboard.curr_pos - 71, self.body_xcoord + newboard.curr_pos - 1, -1, 0)
				Bullets_arr.append(temp_bullet)
				self.bullets -= 1
		
	



