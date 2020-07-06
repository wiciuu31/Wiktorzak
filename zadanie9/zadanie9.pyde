
def setup():

    global img
    size(1200/2, 1600/2)
    noFill()
    strokeWeight(10)

def draw():
 
    global img
    img = loadImage("legirta.jpg")
    
           ####
    try:
        image(img, 50,100, 500,500)
    except:
        print ("Błąd! zla_nazwa")
        stroke (255,0,0,90)
    else:
        stroke(0,0,255)
    finally:
        rect(50,100,500,500)
        print("zakonczono")
        
# 1pkt
