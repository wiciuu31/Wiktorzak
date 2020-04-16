def setup():
    size(600, 600)
    textSize(120) 
def draw():
    
    print(keyPressed)
    clear()
    
                      ####
               
    if mousePressed :
        fill(0, 255, 255, 150)
        text("J", width/2-50, height/2)
        text("W", width/2-15, height/2)
        
                      ####
    if keyPressed:
        if keyCode == LEFT:
            fill(0, 255, 255, 1000)
            text("J", width/2-50, height/2)
            
        if keyCode == RIGHT:
            fill(0, 255, 255, 1000)
            text("W", width/2-15, height/2)
            
                       ####
    if keyPressed:
        key == "w"
        if key == "w":
            fill(0, 255, 0, 1000)
            text("W", width/2-15, height/2)
            
            
                      ####
    x = (mouseX, mouseY)
    if x == hex(FF009696): ## Nie wiem naprawde jak rozwiązac ten problem z najechaniem myszki
        fill(25, 25, 25, 500) ## w pliku lekcyjnym nie ma zadnych wskazówek :(
        text("J", width/2-50, height/2) ## Trzeba skasowac te 4 linijki aby program zadziałał

                      #### 
                                   
    print(mouseX, mouseY)
    print(hex(get(mouseX, mouseY)))
    s = createShape()
    s.beginShape()
    s.fill(255,200,0,200) 
    s.stroke(255,200,1,255)
    s.vertex(255, 200) 
    s.vertex(255, 140) 
    s.vertex(290, 170) 
    s.vertex(320, 140) 
    s.vertex(350, 170) 
    s.vertex(380, 140)
    s.vertex(380, 200)
    s.endShape(CLOSE)
    shape(s, 5, 0)   
    
    if keyPressed:
        if key == "x":
            exit()
        
