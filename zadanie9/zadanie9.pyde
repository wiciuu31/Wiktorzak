
def setup():

    global img

    size(1200/2, 1600/2) 


    


def draw():
 

    global img
    img = loadImage("legirt.jpg")


    image(img, 50,100, 500,500) 





               ####
    try:
 
        f= open("legirt.jpg")
        if f.name == "legirt.jpg":
            raise Exception

               
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print ("Błąd! zla_nazwa")
        print rect(50,100,500,500)
        fill (255,0,0,90)
        
    else:
    
    
        print rect(50,100,500,500)
        fill (0,0,255,0)
        stroke(0,0,255)
    finally:
        print("zakonczono")
