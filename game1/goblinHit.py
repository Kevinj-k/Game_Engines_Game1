import pygame, simpleGE, random



class Goblin(simpleGE.Sprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.walkAnim = simpleGE.SpriteSheet("goblinWalk.png", (64,64),4,8,.1)
        self.walkAnim.startCol = 0
        self.animRow = 0
        self.moveSpeed = 2
    
    def process(self):
        self.dx = 0
        self.dy = 0
        walking = False
        if self.isKeyPressed(pygame.K_LEFT):
            self.animRow = 3
            self.dx = -self.moveSpeed
            walking = True
        if self.isKeyPressed(pygame.K_RIGHT):
            self.animRow = 1
            self.dx = self.moveSpeed
            walking = True
        if self.isKeyPressed(pygame.K_UP):
            self.animRow = 2
            self.dy = -self.moveSpeed
            walking = True
        if self.isKeyPressed(pygame.K_DOWN):
            self.animRow = 0
            self.dy = self.moveSpeed
            walking = True
            
        if walking:
            self.copyImage(self.walkAnim.getNext(self.animRow))
        else:
            self.copyImage(self.walkAnim.getCellImage(0,self.animRow))
            
    
    
class Weapon(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("slashSpriteSingular.png")
        self.setSize(30,30)
        self.hide()
        self.flash = 0
        
    
    def Swing(self):
        if not self.visible:
            self.show()
            self.flash = 10
            
            offset = 40
            
            if self.parent.animRow == 0:
                self.position = (self.parent.x,self.parent.y + offset)
            elif self.parent.animRow == 1:
                self.position = (self.parent.x + offset, self.parent.y)
            elif self.parent.animRow == 2:
                self.position = (self.parent.x,self.parent.y - offset)
            elif self.parent.animRow == 3:
                self.position = (self.parent.x - offset, self.parent.y)
    
    def process(self):
        if self.visible:
            self.flash -= 1
            if self.flash <= 0:
                self.hide()
    

class villager(simpleGE.Sprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("villager.png")
        self.setSize(30,50)
        self.facingRight = True
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        self.y = random.randint(50, self.screenHeight - 50)
        self.x = random.randint(0, self.screenWidth)
        self.dx = random.randint(self.minSpeed, self.maxSpeed) * random.choice([-1,1])
    
    
    def checkBoundaries(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
    
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score 0"
        self.center = (100,30)
        

class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left 15"
        self.center = (500,30)
    

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("village.png")
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.score = 0
        self.goblin = Goblin(self)
        self.weapon = Weapon(self,self.goblin)
        self.numVillagers = 10
        self.villagers = []
        for i in range(self.numVillagers):
            self.villagers.append(villager(self))
            
        self.lblScore = LblScore()
        self.lblTime = LblTime()
        
        self.sprites = [self.goblin, self.weapon,self.villagers,self.lblTime,self.lblScore]
        
        
    def process(self):
        if self.isKeyPressed(pygame.K_SPACE):
            self.weapon.Swing()
            self.weapon.process()
        for villager in self.villagers:
            if self.weapon.collidesWith(villager):
                villager.reset()
                self.score += 100
                self.lblScore.text = f"Score: {self.score}"
                
             
        self.lblTime.text = f"Time left {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Final Score: {self.score}")
            self.stop()
            
        

def main():
    game = Game()
    game.start()
    

if __name__ == "__main__":
    main()
            