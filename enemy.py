from mario import newboard, Bullets_arr
from bullets import Bullets

class Enemy :

    def __init__(self, x_start_coord, y_start_coord) :
        self.head_xcoord = x_start_coord
        self.head_ycoord = y_start_coord - 1
        self.legs_xcoord = x_start_coord
        self.legs_ycoord = y_start_coord
        self.flag = 0
        self.valid = 1

    def printenemy(self) :

        newboard.grid[ self.head_ycoord ][self.head_xcoord ] = '('
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 1 ] = 'E'    
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 2 ] = 'E'    
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 3 ] = ')'
        newboard.grid[ self.legs_ycoord ][self.legs_xcoord + 1 ] = '/'    
        newboard.grid[ self.legs_ycoord ][self.legs_xcoord + 2 ] = '\\'    

    def clearenemy(self) :
        
        newboard.grid[ self.head_ycoord ][self.head_xcoord ] = ' '
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 1 ] = ' '    
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 2 ] = ' '    
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 3 ] = ' '
        newboard.grid[ self.legs_ycoord ][self.legs_xcoord + 1 ] = ' '    
        newboard.grid[ self.legs_ycoord ][self.legs_xcoord + 2 ] = ' '

    def check(self):

        val = self.head_xcoord
        if(newboard.grid[ self.legs_ycoord + 1 ][ val + 1 ] == ' ' and newboard.grid[ self.legs_ycoord + 1 ][ val + 2 ] == ' ') :
            self.head_ycoord += 1	
            self.legs_ycoord += 1
    
    def moveenemy(self) :

        self.clearenemy()
        if (self.flag == 0) :
            if (newboard.grid[ self.legs_ycoord ][ self.legs_xcoord + 4 ] == ' ' and newboard.grid[self.head_ycoord][self.head_xcoord + 4] == ' ') :
                self.legs_xcoord += 1
                self.head_xcoord += 1    
            else :
                self.flag = 1

        elif (self.flag == 1) :        

            if (newboard.grid[self.legs_ycoord][self.legs_xcoord - 1] == ' ' and newboard.grid[self.head_ycoord][self.head_xcoord - 1] == ' ') :
                self.legs_xcoord -= 1
                self.head_xcoord -= 1        
            else :    
                self.flag = 0  
        self.check()    
        self.printenemy()            

class Enemy1 :

    def __init__(self, x_start_coord, y_start_coord) :
        self.x = x_start_coord
        self.y = y_start_coord
        self.head_xcoord = x_start_coord
        self.head_ycoord = y_start_coord - 1
        self.legs_xcoord = x_start_coord
        self.legs_ycoord = y_start_coord    
        self.flag = 0
        self.valid = 1

    def printenemy(self) :

        newboard.grid[ self.head_ycoord ][self.head_xcoord ] = '('
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 1 ] = 'E'    
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 2 ] = 'E'    
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 3 ] = ')'
        newboard.grid[ self.legs_ycoord ][self.legs_xcoord + 1 ] = '/'    
        newboard.grid[ self.legs_ycoord ][self.legs_xcoord + 2 ] = '\\'    

    def clearenemy(self) :
        
        newboard.grid[ self.head_ycoord ][self.head_xcoord ] = ' '
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 1 ] = ' '    
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 2 ] = ' '    
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 3 ] = ' '
        newboard.grid[ self.legs_ycoord ][self.legs_xcoord + 1 ] = ' '    
        newboard.grid[ self.legs_ycoord ][self.legs_xcoord + 2 ] = ' '

    def check(self):

        val = self.head_xcoord
        if(newboard.grid[ self.legs_ycoord + 1 ][ val + 1 ] == ' '  and newboard.grid[ self.legs_ycoord + 1 ][ val + 2 ] == ' ') :
            self.head_ycoord += 1	
            self.legs_ycoord += 1
    
    def moveenemy(self) :

        self.clearenemy()
        if (self.flag == 1) :
            if (newboard.grid[ self.legs_ycoord ][ self.legs_xcoord + 4 ] == ' ' and newboard.grid[self.head_ycoord][self.head_xcoord + 4] == ' ') :
                self.legs_xcoord += 1
                self.head_xcoord += 1    
            else :
                self.flag = 0

        elif (self.flag == 0) :        

            if (newboard.grid[self.legs_ycoord][self.legs_xcoord - 1] == ' '  and newboard.grid[self.head_ycoord][self.head_xcoord - 1] == ' ') :
                self.legs_xcoord -= 1
                self.head_xcoord -= 1        
            else :    
                self.flag = 1  
        self.check()    
        self.printenemy() 

class BossEnemy :

    def __init__(self, x_start) :
        self.head_xcoord = x_start
        self.head_ycoord = 42
        self.ubody_xcoord = x_start
        self.ubody_ycoord = 43
        self.lbody_xcoord = x_start
        self.lbody_ycoord = 44
        self.llbody_ycoord = 45
        self.llbody_xcoord = x_start
        self.legs_xcoord = x_start
        self.legs_ycoord = 46   
        self.alive = 1
        self.health = 20
        self.direction = 1

    def printenemy(self) :
        
        newboard.grid[ self.head_ycoord ][self.head_xcoord ] = '|'
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 1 ] = '^'    
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 2 ] = '^'    
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 3 ] = '|'
        newboard.grid[ self.ubody_ycoord ][self.ubody_xcoord + 1 ] = '\\'
        newboard.grid[ self.ubody_ycoord ][self.ubody_xcoord + 2 ] = '/'  
        newboard.grid[ self.ubody_ycoord ][self.ubody_xcoord ] = '*'    
        newboard.grid[ self.ubody_ycoord ][self.ubody_xcoord + 3 ] = '*'    
        newboard.grid[ self.lbody_ycoord ][self.lbody_xcoord ] = '@'    
        newboard.grid[ self.lbody_ycoord ][self.lbody_xcoord + 1 ] = '/'    
        newboard.grid[ self.lbody_ycoord ][self.lbody_xcoord + 2 ] = '\\'
        newboard.grid[ self.lbody_ycoord ][self.lbody_xcoord + 3 ] = '@'    
        newboard.grid[ self.llbody_ycoord ][self.llbody_xcoord ] = '|'    
        newboard.grid[ self.llbody_ycoord ][self.llbody_xcoord + 3 ] = '|'    
        newboard.grid[ self.legs_ycoord ][self.legs_xcoord + 1 ] = '/'
        newboard.grid[ self.legs_ycoord ][self.legs_xcoord + 2 ] = '\\'

    def clearenemy(self) :

        newboard.grid[ self.head_ycoord ][self.head_xcoord ] = ' '
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 1 ] = ' '    
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 2 ] = ' '    
        newboard.grid[ self.head_ycoord ][self.head_xcoord + 3 ] = ' '
        newboard.grid[ self.ubody_ycoord ][self.ubody_xcoord + 1 ] = ' '
        newboard.grid[ self.ubody_ycoord ][self.ubody_xcoord + 2 ] = ' '  
        newboard.grid[ self.ubody_ycoord ][self.ubody_xcoord ] = ' '    
        newboard.grid[ self.ubody_ycoord ][self.ubody_xcoord + 3 ] = ' '    
        newboard.grid[ self.lbody_ycoord ][self.lbody_xcoord ] = ' '    
        newboard.grid[ self.lbody_ycoord ][self.lbody_xcoord + 1 ] = ' '    
        newboard.grid[ self.lbody_ycoord ][self.lbody_xcoord + 2 ] = ' '
        newboard.grid[ self.lbody_ycoord ][self.lbody_xcoord + 3 ] = ' '    
        newboard.grid[ self.llbody_ycoord ][self.llbody_xcoord ] = ' '    
        newboard.grid[ self.llbody_ycoord ][self.llbody_xcoord + 3 ] = ' '    
        newboard.grid[ self.legs_ycoord ][self.legs_xcoord + 1 ] = ' '
        newboard.grid[ self.legs_ycoord ][self.legs_xcoord + 2 ] = ' '

    def moveenemy(self, obj) :

        self.clearenemy()
        
        var, var1 = 0, 0
        for i in range(42, 47) :
            
            if ( not(newboard.grid[ i ][ self.legs_xcoord - 1 ] == ' ') ) :
                var = 1

            if ( not(newboard.grid[ i ][ self.legs_xcoord + 4 ] == ' ' ) ) :
                var1 = 1
        
        if (obj.legs_xcoord + newboard.curr_pos + 4 < self.legs_xcoord) :

            if (self.legs_xcoord > 1200) :
                if (var == 0) :
                    self.legs_xcoord -= 1
                    self.llbody_xcoord -= 1
                    self.lbody_xcoord -= 1
                    self.ubody_xcoord -= 1
                    self.head_xcoord -= 1

                elif (var1 == 0) :
                    self.legs_xcoord += 1
                    self.llbody_xcoord += 1
                    self.lbody_xcoord += 1
                    self.ubody_xcoord += 1
                    self.head_xcoord += 1

        else :

            if (var1 == 0) :
                self.legs_xcoord += 1
                self.llbody_xcoord += 1
                self.lbody_xcoord += 1
                self.ubody_xcoord += 1
                self.head_xcoord += 1

            elif (var == 0) :
                self.legs_xcoord -= 1
                self.llbody_xcoord -= 1
                self.lbody_xcoord -= 1
                self.ubody_xcoord -= 1
                self.head_xcoord -= 1

        if(abs(self.legs_xcoord- obj.legs_xcoord - newboard.curr_pos) <= 50) :
            
            if(self.direction == 1) :
                
                if (self.head_ycoord >= 35) :
                    self.legs_ycoord -= 1
                    self.llbody_ycoord -= 1
                    self.lbody_ycoord -= 1
                    self.ubody_ycoord -= 1
                    self.head_ycoord -= 1
                
                else :
                    self.direction = 0

            if(self.direction == 0) :
    
                if(self.legs_ycoord <= 45) :
                    self.legs_ycoord += 1
                    self.llbody_ycoord += 1
                    self.lbody_ycoord += 1
                    self.ubody_ycoord += 1
                    self.head_ycoord += 1
                
                else :
                    self.direction = 1     
    
        self.printenemy()         

    def shootmario(self, obj) :
        
        if(abs(self.legs_xcoord- obj.legs_xcoord - newboard.curr_pos) <= 50) :

            if (self.legs_ycoord == 45 and self.direction == 1) :
                if (self.legs_xcoord > obj.legs_xcoord + newboard.curr_pos + 4 ) :
                    for i in range(self.head_ycoord, self.legs_ycoord + 1) :
                        if (not(i == self.head_ycoord + 1 or i == self.head_ycoord + 3)) :
                            temp_bullet = Bullets(self.legs_xcoord - 1, i, self.legs_xcoord - 70, self.legs_xcoord - 1, -1, 1)
                            Bullets_arr.append(temp_bullet)
                else :
                    for i in range(self.head_ycoord, self.legs_ycoord + 1) :
                        if (not(i == self.head_ycoord + 1 or i == self.head_ycoord + 3)) :
                            temp_bullet = Bullets(self.legs_xcoord + 4, i, self.legs_xcoord + 4, self.legs_xcoord + 70, 1, 1)
                            Bullets_arr.append(temp_bullet)





