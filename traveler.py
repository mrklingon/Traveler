import time
import random
from wise import *

star = []
locx = []
locy = []

map = ["..........","..........","..........","..........","..........","..........","..........","..........","..........",".........."]
def dist(l1,l2):
    dst = (((locx[l1]-locx[l2])**2+((locy[l1]-locy[l2])**2))**.5)
    return dst


def showDists(loc):
    print("location = " + star[loc])
    for i in range(len(star)):
        print (star[i] + ":" + str(locx[i])+", " + str(locy[i])+": "+str(dist(i,loc)))

def showCourse():
    choices = "123456789"
    for i in range (len(star)):
        print (str(1+i)+": "+star[i])
    print ()
    print ("Where to?")
    destination = eval(intpt(choices))-1
    if destination != Where:
        print ("OK, heading to "+star[destination])
    return (destination)

def placeNM():
    #build a random star name
    start = ["Gi","Ro","Ah","Mi","Pa","Ki","Re","Sy","Th","Zo"]
    mid = ["eu","af","gh","uu","a","e","i","o","u","y"]
    end = ["nk","as","of","z","d","n","ll","ah","ei","ie"]

    Place = random.choice(start)+random.choice(mid)+random.choice(end)
    return (Place)

def chartStars():

    for i in range(random.randrange(3,9,1)):
        star.append(placeNM())
        locx.append(random.randrange(10))
        locy.append(random.randrange(10))
        s = map[locy[i]]
        s = s[:locx[i] ] + "*" + s[locx[i]+1:]
        map[locy[i]] = s
    return (locx,locy,map,star,random.randrange(len(star))) 

    
def printMap(locx,locy,map,star,Where):
    
    for i in range(len(star)):
        print (star[i] + ":" + str(locx[i])+", " + str(locy[i]))

    print("Current location: "+star[Where])
    print()
    for i in range(10):
        print (map[i])


# important: set radius to define size of map. set map to the file of room descriptions
radius = 3 # change to width of A x A matrix of rooms. 
MAP = "ship.adv"  #change to file listing rooms for adventure
pics ="imgs" #list of ascii art file matching rooms. "x" is a blank file
WRAP = False # True for a 'torus' map, False for non-torus

(locx,locy,map,star,Where) = chartStars()
destination = Where

def intpt(chars):
    Done = False

    while not Done:
        dir = input("Choose  ("+chars+") >")
        if chars.find(dir) >= 0:
            Done = True
    return (dir)

 
def loc(x,y):
    l = x + (y*radius)
    return l

px = 1 #set to starting room X position
py = 1 #set to starting room Y position

def cat(file):
    l = file_len(file)
    for ln in range(l):
        print(wisdom(ln,file))

def where(x,y): #return location text based on location
    loctxt = wisdom(loc(x,y),MAP)
    picture = wisdom(loc(x,y),pics)
    cat(picture)
    if loc(x,y) == 1:
        shipdisplay()
        
    loctxt.strip("\n")
    l= loctxt.split("|")
    if len(l)==2:
        return (l[0],l[1])
    else:
        return (l[0],"nsew")
        
def chgloc(dir): #change location 
    global px
    global py
    if dir == "n":
        py = py - 1
    if dir == "s":
        py = py + 1
    if dir == "w":
        px = px - 1
    if dir == "e":
        px = px + 1
    if WRAP:
        if px < 0:
            px = radius - 1
        if px >= radius:
            px = 0
        if py < 0:
            py = radius - 1
        if py >=radius:
            py = 0
    else:
        if px < 0:
            px = 0
        if px >= radius:
            px = radius-1
        if py < 0:
            py = 0
        if py >= radius:
            py = radius - 1
            


def shipdisplay():
    if destination == Where:
        print("Current Location: " + star[Where])
    else:
        print("Traveling from "+star[Where] + " to " + star[destination])
            
(location,cmds)=where(px,py)
print("Current location: "+location)

while True:
  
  
    print("Next action? "+cmds+"?")
    dir = intpt(cmds)
    if dir in "nsew":
        chgloc(dir)
        (location,cmds)=where(px,py)
        print("Current location: "+location)
    else:
        if dir == "M":
            printMap(locx,locy,map,star,Where)
        if dir == "D":
            #show destinations
            showDists(Where)
        if dir == "C":
            #set destination
            destination = showCourse()


