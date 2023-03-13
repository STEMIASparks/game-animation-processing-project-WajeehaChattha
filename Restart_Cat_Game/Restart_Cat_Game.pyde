#these are the variables
#img and roses makes it more efficent for show an image & change between them
img = "CAT1FINAL.png"
rose = "roses.png"
#the x and y allow me to move the rose
x = 200
y = 700
#these are the parameters around the cat, and once the rose touches them, the game ends
a = 450
b = 500
c = 505
d = 555
#score
clicks = 0

#sets up my screen, runs once, intial
def setup():
    size(1000,1000)
    background(255,255,255)
    
#loops forever unless told otherwise to stop
def draw():
#makes sure I can use them inside of the function
    global img, x, y
#creates background everytime function runs
    background(255,255,255)
#creates first cat
    image(loadImage(img), 250, 150, 500, 700)
    fill(0, 0, 0)
#creates font and prints it on screen
    font = loadFont("Futura-Medium-48.vlw")
    textFont(font, 32)
    textSize(40)
    text("Clicks:", 440, 40)
    textSize(40)
    text(clicks, 560, 40)
#makes the cat 2 change to cat 1 after the cat is changed once clicked
#allows you to click it again
    if img == "CAT2.png":
        img = "CAT1FINAL.png"
#allows the program to run a code when a condition is met
#changes the cat to the 3rd sprite when you click it 50 times
#also creates the rose
    if clicks == 50:
        img = "CAT3FINAL.png"
        image(loadImage(rose), x, y, 150, 150)
#allows you to change the x and y of the rose and move it
#when you click on keys
    if keyCode == UP:
        y = y - 50
    if keyCode == DOWN:
        y = y + 50
    if keyCode == RIGHT:
        x = x + 50
    if keyCode == LEFT:
        x = x - 50
#uses the parameters of the cat so that when the rose is in contact with the cat
#the game will "end"
#changes cat to last sprite
    if x >= a and x <= b or x >= c and x <= d:
        img = "CAT5.png"
#moves rose and displays "you win" text signifying end of the game
    if img == "CAT5.png":
        x = 475
        y = 525
        fill(0, 0, 0)
        textSize(100)
        text("You win!", 400, 400)
        
#loop, when the mouse it clicked the # of clicks changes as well as the cat sprite 
def mouseClicked(): 
    global img, clicks
    if img == "CAT1FINAL.png":
        img = "CAT2.png"
        clicks = clicks + 1
