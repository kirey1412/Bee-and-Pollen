import pgzrun, random

TITLE="Bee and Pollen"
WIDTH=800
HEIGHT=700

speed=5

pollens=[]
flowers=[]
directions=1
gamefinish=False

score=0
bee=Actor("bee.png")
bee.dead=False
for i in range(7):
        flower=Actor("flower.png")
        flowers.append(flower)
        flowers[-1].x=100+110*i #to update recently added element
    

bee.pos=(WIDTH/2, HEIGHT-50)

def draw():
    global gamefinish  
    screen.clear()
    screen.fill("green")
    if not bee.dead:
        bee.draw()
    for i in flowers:
        i.draw()
    screen.draw.text(str(score), (50,50), color="gray")
    for p in pollens:
        p.draw()
        if gamefinish:
            screen.draw.text("GAME OVER", (WIDTH/2, HEIGHT/2), color="red")
        if len(flowers)==0:
            gamefinish=True

def update():
    global score, directions
    if keyboard.left:
        bee.x-=speed
        if bee.x<50:
            bee.x=50
    elif keyboard.right:
        bee.x+=speed
        if bee.x>WIDTH-50:
            bee.x=WIDTH-50
    if len(flowers)>0 and (flowers[-1].x>WIDTH-80 or flowers[0].x<80):
        directions=directions*(-1)
    for f in flowers:
        f.y+=2
        f.x+=5*directions
        if f.y>HEIGHT:
            flowers.remove(f)
        for p in pollens:
            if f.colliderect(p):
                flowers.remove(f)
                pollens.remove(p)
                score+=30
        
    for b in pollens:
        b.y-=5
        if b.y<0:
            pollens.remove(b)

def on_key_down(key):
    if key==keys.SPACE:
        pollens.append(Actor("pollen"))
        pollens[-1].x=bee.x
        pollens[-1].y=bee.y-50

pgzrun.go()