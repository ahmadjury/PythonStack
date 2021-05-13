import random
def randInt(min= 0  , max=100  ):
    if(min>max or max<0):
        return"try again"    
    num = random.random() *max + min
    return num
print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(50, 500))    # should print a random integer between 50 and 500
print(randInt(500, 50))
print(randInt(-5, -1))