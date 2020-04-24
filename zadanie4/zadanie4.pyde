


add_library('pdf') 


def setup():

    global img
    global img1
    global img2
    size(1200/2, 1600/2) 
    #size(600, 800, PDF, "outZadanko.pdf")
    img = loadImage("legirt.jpg")
    img1 = loadShape("bot1.svg")
    img2 = loadImage("12.png")
    
    beginRecord(PDF, "outZadanko.pdf")
    
    global l
    global r

    l = loadImage("l.png")
    r = loadImage("r.png")
    
    
    
    
    print(type(img))


def draw():

    global img
    global img1
    global img2
    image(img, 0,0, 600, 800) 
    shape(img1,50,600, 100, 100) 
    image(img2,480,600, 100, 100)
    image(l,117, 670,120, 120)
    image(r,435, 670, 120, 120)
    endRecord() 

               ####

    if keyPressed:
        if keyCode == LEFT:
    
             shape(img1, 130,200, height/2, width/1.5)

            
        if keyCode == RIGHT:
        
             image(img2, 130,230, height/2, width/2)
            
               ####

def mousePressed():
    exit()
