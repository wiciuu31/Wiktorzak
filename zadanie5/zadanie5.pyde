                       ##########
                       
class Kwadracik(): # nazwy klas zwyczajowo dużą literą
    dol = 0 # dzięki przerzuceniu ich do atrybutów klasy zamiast obiektu będą wspólne dla wszystkich obiektów tej klasy
    gora = 0
    lewo = 0
    prawo= 0
    
    def __init__(self, pos):
        
        self.x = pos  #START (pozycja startowa) ustawienie przez konstruktor umożliwi pojawienie się kolejnych obiektów  nie na sobie, a w innych pozycjach
        self.y = pos  #START (pozycja startowa)
        self.szybko= 7 # proponowałabym też dodać możliwość ustawienia przez konstruktor, wówczas każdy obiekt będzie mógł mieć indywidualną prędkość ;D
        self.wys = 100
        self.szer = 50
    def show(self):
        
        fill(0,74,200)
        rect(self.x,self.y,self.wys,self.szer)
        
    def update(self):
        
        self.y = self.y + (Kwadracik.dol - Kwadracik.gora)*self.szybko
        self.x = self.x + (Kwadracik.prawo - Kwadracik.lewo)*self.szybko
        print(self.x, self.y)
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
    
    global c, k
    c = Kwadracik(350)
    k = Kwadracik(150) # miały być dwa obiekty :)
                      
                        ##########
                        
def draw():
    
    background(82)
    
    c.show()
    k.show()
    if keyPressed: # teraz będziemy updeatować tylko, gdy będzie taka potrzeba (kliknięto)
        c.update()
        k.update()
    
                        ##########
                        
                                                ##########
    
def keyPressed():
    if key == "w":
        Kwadracik.gora=1 # dzięki temu, że nie jest to właściwość obiektu a klasy, nie musimy mnożyć linijek dla każdego obiektu
        
    if key == "s":
        Kwadracik.dol=1
        
    if key == "d":
        Kwadracik.prawo=1
        
    if key == "a":
        Kwadracik.lewo=1
                                               
                                        ##########
                                               
def keyReleased():
    
    if key == "w":
        Kwadracik.gora=0
        
    if key == "d":
        Kwadracik.prawo=0
        
    if key == "s":
        Kwadracik.dol=0

    if key == "a":
        Kwadracik.lewo=0

        
                                            ##########
                                            
# w ramach ćwiczenia stwórz nowy obiekt i zachwycaj sięjak wszystkie tańczą ;D
#1,75pkt
