posX = 0
posY = 200

def setup (): 
    size(400,400)
    frameRate(15)  

    
def draw():
 global slownik_kolorow  
 slownik_kolorow = {"zółty":(253,228,0,100), "różowy":(255,0,128,100), "czerwony":(255,0,0, 100), "niebieski":(0,0,255,100), "zielony":(0,255,0,100),}
 global lista_kolorow
 lista_kolorow = []
 for klucz, wartosc in slownik_kolorow.items(): 
     lista_kolorow.append(wartosc)
 global posX
 global posY


 fill(*lista_kolorow[posY%len(lista_kolorow)])
 rect(posX,posY,20,20)
 posX += 1
 posY += 1
 if posX > 200:
     posY += -2
 if posY < 200:
     posX += -2
 print(posX, posY)     
 if mousePressed:
        exit()
