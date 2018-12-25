
class Bullets :

    def __init__(self, x_coord, y_coord, range_begin, range_end, direction, source) :

        self.x = x_coord
        self.y = y_coord
        self.range_begin = range_begin
        self.range_end = range_end
        self.direction = direction        
        self.source = source         

    def print_bullets(self, newboard) :

        if(self.direction == 1) :
            newboard.grid[ self.y ][ self.x ] = chr(9197)
        else :
            newboard.grid[ self.y ][ self.x ] = chr(9198)

    def clearbullets(self, newboard) :

        if(self.direction == 1) :
            newboard.grid[ self.y ][ self.x ] = ' '
        else :
            newboard.grid[ self.y ][ self.x ] = ' '        

    def movebullets(self, newboard) :

        self.clearbullets(newboard)
        if (self.direction == 1) :
            self.x += 1
        else :
            self.x -= 1

                
