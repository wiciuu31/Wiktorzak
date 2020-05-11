                       ##########
                       
class kwadracik():
    def __init__(self):
        
        self.x = 350  #START (pozycja startowa)
        self.y = 350  #START (pozycja startowa)
        self.dol = 0
        self.gora = 0
        self.lewo = 0
        self.szybko= 7
        self.prawo= 0
        self.wys = 100
        self.szer = 50
    def show(self):
        
        fill(0,74,200)
        rect(self.x,self.y,self.wys,self.szer)
        
    def update(self):
        
        self.y = self.y + (self.dol - self.gora)*self.szybko
        self.x = self.x + (self.prawo - self.lewo)*self.szybko
        if not (self.x >= 0):
            self.x = 0
        if not (self.x <= (700 - self.wys)):
            self.x = (700 - self.wys)
        if not (self.y >= 0):
            self.y = 0
        if not (self.y <= (700 - self.szer)):
            self.y = (700 - self.szer)
            
                       ##########
                       
                       ##########
                       
def setup():
    size(700,700)
    
    global c
    c = kwadracik()
                      
                        ##########
                        
def draw():
    
    background(82)
    
    c.update()
    c.show()
    
                        ##########
                        
                                                ##########
    
def keyPressed():
    if key == "w":
        c.gora=1
        
    if key == "s":
        c.dol=1
        
    if key == "d":
        c.prawo=1
        
    if key == "a":
        c.lewo=1
                                               
                                        ##########
                                               
def keyReleased():
    
    if key == "w":
        c.gora=0
        
    if key == "d":
        c.prawo=0
        
    if key == "s":
        c.dol=0

    if key == "a":
        c.lewo=0

        
                                            ##########
