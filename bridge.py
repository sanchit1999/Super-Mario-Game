class Bridge :

    def __init__(self, x_coord) :

        self.x = x_coord
        self.y = 47
        self.direction = 1

    def printbridge(self, newboard) :

        for i in range(self.y, self.y - 4, -1) :

            for j in range(self.x, self.x + 18) :

                newboard.grid[ i ][ j ] = chr(9993)

    def clearbridge(self, newboard) :

        for i in range(self.y, self.y - 4, -1) :

            for j in range(self.x, self.x + 18) :

                newboard.grid[ i ][ j ] = ' '

    def movebridge(self, newboard) :

        self.clearbridge(newboard)

        if(self.direction == 1) :

            if(self.y == 28) :
                self.direction = 0
            else :
                self.y -= 1
        
        else :

            if(self.y == 54) :
                self.direction = 1
            else :
                self.y += 1

        self.printbridge(newboard)                             
                           

    