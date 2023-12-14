import turtle as trtl

wn = trtl.Screen()
#-----sets back ground-----
Town = 'Town_background.gif'
wn.bgpic(Town)
trtl.screensize()

#----------iniciates all the turtles------------

#-----Button-----
Button = 'red_button.gif'
wn.addshape(Button)
mascot = trtl.Turtle(shape = Button)

#-----Nuke-----
Nuke = 'Nuke.gif'
wn.addshape(Nuke)
mascot2 = trtl.Turtle(shape = Nuke)

#-----Nuclear Explosion-----
Explosion = 'Nuke_Explosion.gif'
wn.addshape(Explosion)
mascot3 = trtl.Turtle(shape = Explosion)
mascot3.penup()
mascot3.hideturtle()

#----------initial positions------------

#----Drawer-----
drawer = trtl.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.speed(9000)

#-----button-----
mascot.speed(9000)
mascot.penup()
mascot.goto(633,-329)

#-----Nuke-----
mascot2.speed(9000)
mascot2.penup()
mascot2.goto(-50,100)

#-----Explosion-----
mascot3.speed(9000)
mascot3.penup()
mascot3.goto(-56,90)

#----------Functions------------

#----Drops the bomb----
def drop():
    mascot2.speed(1)
    mascot2.goto(-50,-10)
    mascot3.showturtle()
#----Password set up----
entered = ""
armed = False

def Password():
    global armed
    if (entered == "42351"):
        drawer.goto(-650,340)
        drawer.color("black")
        drawer.write("Correct Password! Press the button to drop the bomb. :)))", font=("Arial", 35, "bold"))
        armed = True
        
def four_pressed():
    global entered
    entered = entered + "4"
    Password()
def Two_pressed():
    global entered
    entered = entered + "2"
    Password()
def Three_pressed():
    global entered
    entered = entered + "3"
    Password()
def Five_pressed():
    global entered
    entered = entered + "5"
    Password()
def one_pressed():
    global entered
    entered = entered + "1"
    Password()

def fire_missle(x,y):
    if (armed == True):
        drop()
    else:
        print("fail to launch")

#------------Events--------------
wn.onkeypress(four_pressed, "4")
wn.onkeypress(Two_pressed, "2")
wn.onkeypress(Three_pressed, "3")
wn.onkeypress(Five_pressed, "5")
wn.onkeypress(one_pressed, "1")

#------Password + Drop------
mascot.onclick(Password)
mascot.onclick(fire_missle)


wn.listen()
wn.mainloop()