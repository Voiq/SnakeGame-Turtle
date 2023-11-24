import turtle
import time
import random

delay = 0.1

score =0
high_score=0


#Setup the screen

wn=turtle.Screen()
wn.title =("Snake Game")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)


#Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction="stop"

#Food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []


#Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0   High Score:0",align="center",font=("Courier",24,"normal"))


#Functions

def go_up():
    if head.direction !="down":
        head.direction="up"
def go_down():
    if head.direction !="up":
        head.direction="down"
def go_left():
    if head.direction !="right":
        head.direction="left"        
def go_right():
    if head.direction !="left":
        head.direction="right"  

def move():
    if head.direction=="up":
        head.sety(head.ycor()+20)
    if head.direction=="down":
        head.sety(head.ycor()-20)
    if head.direction=="left":
        head.setx(head.xcor()-20)
    if head.direction=="right":
        head.setx(head.xcor()+20)

#Keyboard Bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")





#Main Game Loop
while True:
    wn.update()
    #checks collisions
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)
            
        #Clearing the list 
        segments.clear()
        
            
        
    if head.distance(food) < 20:
        #Food goes to random spot
        food.goto(random.randint(-290,290),random.randint(-290,290))
        
        #Add  segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        
        #Increasing the score
        score +=1
        
        if score > high_score:
            high_score=score
        pen.clear()    
        pen.write(f"Score : {score}  High Score: {high_score}",align="center",font=("Courier",24,"normal"))    
    
    #Make segments move with the head
    for index in range(len(segments)-1,0,-1):
        segments[index].goto(segments[index-1].xcor(),segments[index-1].ycor())    
    
    # Move first segment to the head
    if len(segments) > 0:
        segments[0].goto(head.xcor(),head.ycor())    

    move()
    #Check for head collision
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            #Hide the segments
            for segment in segments:
                segment.goto(1000,1000)
                
            #Clearing the list 
            segments.clear()
            #Clear the score
            score = 0
            pen.clear()    
            pen.write(f"Score : {score}  High Score: {high_score}",align="center",font=("Courier",24,"normal"))
    time.sleep(delay)


wn.mainloop()