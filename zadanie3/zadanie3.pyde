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

        if key == "w":
            fill(0, 255, 0, 1000)
            text("W", width/2-15, height/2)
            
            
                      ####
    x = hex(get(mouseX, mouseY)) # funkcja get pobiera kolor z pozycji myszy, pozycji samej w sobie nie można porównać z kolorem, bo to dwie różne rzeczy; przykład był w pliku ode mnie i można sprawdzić działanie tej funkcji rónież w referencjach
    if x == 'FF009696': # ten kolor wystąpi w okie programu dopiero po kliknięciu, należałobyb wyświetlać w jakimś defaultowym
        #J i W mają te same kolory, więc albo tzebaby je rozróżnić, albodadać dodatkowy warunek pozycji myszy, by wychwycić kliknięcia na samo J
        fill(250, 250, 25)
        text("J", width/2-50, height/2)

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
    
#1,5pkt
