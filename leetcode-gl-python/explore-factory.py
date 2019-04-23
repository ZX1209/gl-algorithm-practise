# explore-factory.py
import random

# generate a random rect in [xstart,xend] and [ystart,yend]
# width and height will not out of range.. and be as x and y
# return (x, y, width, height)


def randomRect(xstart, xend, ystart, yend):
    x = random.randint(xstart, xend)
    y = random.randint(ystart, yend)
    width = random.randint(x+1, xend)
    height = random.randint(y+1, yend)
    return {'x':x,'y':y,'width':width,'height':height}

test = randomRect(0,123,5,67)
print(test)
