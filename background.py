
def printMountain1(x_start, newboard) :

	for i in range(x_start, x_start + 12) :
		newboard.grid[ 47 - i + x_start ][ i ] = '/'

	for i in range(x_start + 12, x_start + 34) :
		newboard.grid[ 35 ][ i ] =  '_'

	for i in range(x_start + 34, x_start + 46) :
		newboard.grid[ 2 + i - x_start ][ i ] = '\\'


def printMountain2(x_start, newboard) :

	for i in range(x_start, x_start + 12) :
		newboard.grid[ 47 - i + x_start ][ i ] = '/'

	for i in range(x_start + 12, x_start + 20) :
		newboard.grid[ 24 + i - x_start ][ i ] = '\\'

	for i in range(x_start + 20, x_start + 26) :
		newboard.grid[43][i] =  '_'

	for i in range(x_start + 26, x_start + 34) :
		newboard.grid[ 69 - i + x_start ][ i ] = '/'

	for i in range(x_start + 34, x_start + 46) :
		newboard.grid[ 2 + i - x_start ][ i ] = '\\'


def printMountain3(x_start, newboard) :

	for i in range(x_start, x_start + 12) :
		newboard.grid[ 47 - i + x_start ][ i ] = '/'

	for i in range(x_start + 12, x_start + 23) :
		newboard.grid[ 24 + i - x_start ][ i ] = '\\'

	for i in range(x_start + 23, x_start + 34) :
		newboard.grid[ 69 - i + x_start ][ i ] = '/'

	for i in range(x_start + 34, x_start + 46) :
		newboard.grid[ 2 + i - x_start ][ i ] = '\\'


def printCloud1(x_start, newboard) :

	newboard.grid[ 12 ][ x_start ] = '('
	newboard.grid[ 12 ][ x_start + 13 ] = ')'		
	newboard.grid[ 11 ][ x_start + 1 ] = '_'
	newboard.grid[ 11 ][ x_start + 12 ] = '_'
	newboard.grid[ 11 ][ x_start + 2 ] = '('
	newboard.grid[ 11 ][ x_start + 11 ] = ')'
	newboard.grid[ 10 ][ x_start + 3 ] = '_'
	newboard.grid[ 10 ][ x_start + 4 ] = '('
	newboard.grid[ 10 ][ x_start + 10 ] = '_'
	newboard.grid[ 10 ][ x_start + 9 ] = ')'
	newboard.grid[ 9 ][ x_start + 5 ] = '_'
	newboard.grid[ 9 ][ x_start + 8 ] = '_'
	newboard.grid[ 9 ][ x_start + 7 ] = ')'
	newboard.grid[ 9 ][ x_start + 6 ] = '('

	for i in range(x_start + 1, x_start + 13) :
		newboard.grid[ 12 ][ i ] = '_'

def printCloud2(x_start, newboard) :

	newboard.grid[ 14 ][ x_start ] = '('
	newboard.grid[ 14 ][ x_start + 1 ] = '_'
	newboard.grid[ 14 ][ x_start + 2 ] = '_'
	newboard.grid[ 14 ][ x_start + 3 ] = '_'
	newboard.grid[ 14 ][ x_start + 4 ] = '_'
	newboard.grid[ 14 ][ x_start + 5 ] = '_'
	newboard.grid[ 14 ][ x_start + 6 ] = '_'
	newboard.grid[ 14 ][ x_start + 7 ] = ')'
	newboard.grid[ 13 ][ x_start + 1 ] = '_'
	newboard.grid[ 13 ][ x_start + 2 ] = '('
	newboard.grid[ 12 ][ x_start + 3 ] = '_'
	newboard.grid[ 13 ][ x_start + 4 ] = ')'
	newboard.grid[ 13 ][ x_start + 5 ] = '_'
	newboard.grid[ 13 ][ x_start + 6 ] = '_'

def printbricks1(x_start, newboard) :
	
	var1 = 0
	for i in range(x_start, x_start + 4) :
		if (newboard.freq[ 39 ][ i ] <= 0) :
			var1 = 1
			break
	if(var1 == 1) :
		for i in range(36, 39) :
			for j in range(x_start, x_start + 4) :
				newboard.grid[ i ][ j ] = chr(9617)
	else :
		for i in range(36, 39) :
			for j in range(x_start, x_start + 4) :
				newboard.grid[ i ][ j ] = str(newboard.freq[ 39 ][ x_start ])	

	var2 = 0
	for i in range(x_start + 8, x_start + 12) :
		if (newboard.freq[ 39 ][ i ] <= 0) :
			var2 = 1
			break
	if(var2 == 1) :
		for i in range(36, 39) :
			for j in range(x_start + 8, x_start + 12) :
				newboard.grid[ i ][ j ] = chr(9617)
	else :
		if(newboard.freq[ 39 ][x_start + 8 ] == 4 and newboard.bricks_freq[ 39 ][x_start + 8] == 1) :
			newboard.freq[ 39 ][ x_start + 8 ] = 6
			newboard.bricks_freq[ 39 ][x_start + 8] = 0
		for i in range(36, 39) :
			for j in range(x_start + 8, x_start + 12) :
				newboard.grid[ i ][ j ] = str(newboard.freq[ 39 ][ x_start + 8 ])	

	for i in range(36, 39) :
		for j in range(x_start + 4, x_start + 8) :
			newboard.grid[ i ][ j ] = chr(9608)		

def printbricks2(x_start, newboard) :

	for i in range(26, 31) :
		for j in range(x_start, x_start + 45) : 
			newboard.grid[ i ][ j ] = chr(9608)

def printpipe1(x_start, newboard) :
	
	for i in range(x_start, x_start + 8) :
		for j in range (47, 36, -1) :
			newboard.grid[ j ][ i ] = chr(9600)
	for i in range(x_start - 1, x_start + 9) :
		newboard.grid[ 36 ][ i ] = '#'

def printpipe2(x_start, newboard) :
	
	for i in range(x_start, x_start + 8) :
		for j in range (47, 40, -1) :
			newboard.grid[ j ][ i ] = chr(9600)
	for i in range(x_start - 1, x_start + 9) :
		newboard.grid[ 40 ][ i ] = '#'		

def printpit(x_start, newboard) :

	for i in range(59, 46, -1) :
		for j in range(x_start, x_start + 25 ) :
			newboard.grid[ i ][ j ] = ' '	

def printcave(x_start, newboard) :

	for i in range(47, 5, -1) :
		for j in range(x_start, x_start + 150) :
			newboard.grid[ i ][ j ] = chr(9619)
	
	for i in range(x_start, x_start + 150) :
		newboard.grid[ 34 ][ i ] = newboard.grid[ 31 ][ i ] = newboard.grid[ 32 ][ i ] =  newboard.grid[ 33 ][ i ] = ' '
	
	for i in range(x_start, x_start + 150) :
		newboard.grid[ 20 ][ i ] = newboard.grid[ 19 ][ i ] = newboard.grid[ 21 ][ i ] =  newboard.grid[ 22 ][ i ] = ' '

	for i in range(23, 31) :
		for j in range(x_start, x_start + 150 ) :
			newboard.grid[ i ][ j ] = chr(9617)	

def printstairs(x_start, newboard) :

	for i in range(1, 6) :
		for j in range(x_start + 4*( i - 1), x_start + 4*i)	:
			for k in range(4*i) :
				newboard.grid[ 47 - k ][ j ] = chr(9608)
				 
def printrevstairs(x_start, newboard) :

	for i in range(5, 0, -1) :
		for j in range(x_start + 4*( 5 - i), x_start + 4*(6 - i)) :
			for k in range(4*i) :
				newboard.grid[ 47 - k ][ j ] = chr(9608)

def printcoins(x_start, y_start, newboard) :

	newboard.grid[y_start][x_start] = chr(9400)

def printbullets(x_start, y_start, newboard) :

	newboard.grid[ y_start ][ x_start ] = chr(9728)

def printspring(x_start, newboard) :

	for i in range(x_start, x_start + 3) :
		for j in range(46, 40, -1) :
			newboard.grid[ j ][ i ] = chr(9776)			