import random

star = []
locx = []
locy = []

map = ["..........","..........","..........","..........","..........","..........","..........","..........","..........",".........."]
def placeNM():
    #build a random star name
    start = ["Gi","Ro","Ah","Mi","Pa","Ki","Re","Sy","Th","Zo"]
    mid = ["eu","af","gh","uu","a","e","i","o","u","y"]
    end = ["nk","as","of","z","d","n","ll","ah","ei","ie"]

    Place = random.choice(start)+random.choice(mid)+random.choice(end)
    return (Place)

def chartStars():
    star = []
    locx = []
    locy = []

    for i in range(random.randrange(3,11,1)):
        star.append(placeNM())
        locx.append(random.randrange(10))
        locy.append(random.randrange(10))

        s = map[locy[i]]
        s = s[:locx[i] ] + "*" + s[locx[i]+1:]
        map[locy[i]] = s
        return (locx,locy,map,star)

    
def printMap(locx,locy,map,star):
    
    for i in range(len(star)):
        print (star[i] + ":" + str(locx[i])+", " + str(locy[i]))

    for i in range(10):
        print (map[i])
