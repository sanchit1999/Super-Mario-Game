import os
import time

class Board:
	
	def __init__(self):

		self.tot_width = 12000
		self.width = 203
		self.height = 60
		self.roof_thickness = 3
		self.side_thickness = 6
		self.floor_thickness = 6
		self.curr_pos = 0
		self.temp_string = ""
		self.grid = [ [ ' ' for i in range(self.tot_width) ] for j in range(self.height) ]
		self.freq = [ [ 4 for i in range(self.tot_width) ] for j in range(self.height) ]
		self.coins_freq = [ [ 1 for i in range(self.tot_width) ] for j in range(self.height) ]
		self.bricks_freq = [ [ 1 for i in range(self.tot_width) ] for j in range(self.height) ]
		self.bullet_freq = [ [ 1 for i in range(self.tot_width) ] for j in range(self.height) ]

		for i in range(self.roof_thickness):
			for j in range(self.tot_width):
				self.grid[i][j] = '*'

		for j in range(self.tot_width):
			self.grid[self.height - 2 * self.floor_thickness - 1][j] = '_'

		for i in range(self.height - 2 * self.floor_thickness, self.height - 1):
			for j in range(self.tot_width):

				if (i % 2 == 1):
					self.grid[i][j] = '-'
				else:
					if (i % 4 == 0) and (j % 8 == 0) :
						self.grid[i][j] = '|'

					elif (i % 4 == 2) and (j % 8 == 4) :
						self.grid[i][j] = '|'

					else:
						self.grid[i][j] = ' '

		for j in range(self.tot_width):
			self.grid[self.height - 1][j] = '_'					  						

	def printBoard(self, obj, boss):
		
		temp_str = ""
			
		for j in range(self.width):

			if (j == 5) :
				temp_str += "Score : "
				temp_str += str(obj.score)

			elif (j == 25) :
				temp_str += "Coins Collected : "
				temp_str += str(obj.coins_collected)
			
			elif ( j == 40) :
				temp_str += "Lives : "
				if(obj.lives >= 0) :
					for k in range(obj.lives) :
						temp_str += chr(9829) + ' '
			elif (j == 60) :
				temp_str += "Bullets : "
				temp_str += str(obj.bullets)
			elif (j == 85) :
				temp_str += "Boss Enemy Health : "
				temp_str += str(boss.health)
			elif (j == 105) :
				temp_str += "Time : "
				temp_str += str(int(time.time()-obj.curr_time))
				temp_str += " s"
			elif (len(temp_str) < self.width) :
				temp_str += ' '			

		self.temp_string = temp_str

		print()
		temporary_String = [ " " for i in range(self.height) ]

		for i in range(self.height):
			if (i == self.roof_thickness + 1):
				temporary_String[i] += self.temp_string
			else:		
				for j in range(self.curr_pos, self.curr_pos + self.width):
					temporary_String[i] += self.grid[i][j]
		
		for i in range(self.height):
			print(temporary_String[i])
		print()
