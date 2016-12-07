import turtle
import random
import math

#******************************Set Up Game***************************
"""
Change the game by changing the values of variables between here and
who.color()
"""
anti = turtle.Turtle()          #don't change name in this version   
wndow = turtle.Screen()
number_of_runs = 400            #how many times to run simulation

def setup(who):
    board_size = 110
    food_size = 80              #how big to make target, 80 is easy
    moves_allowed = 1000        #die if no success
    who.shape('turtle')
    who.color('green')
    
    #************* Do Not Change Settings Below This Line *************
    moves_used = 0
    offset = board_size - food_size / 2     #keep food inside border
    food_location = (random.randint(-offset, offset),random.randint(-offset, offset))
    who.penup()
    who.goto (food_location)
    who.dot(food_size, 'red')
    who.home()
    who.pendown()
    return [board_size, moves_allowed, moves_used, food_location, food_size]

#******************************End Setup *******************************

#***********************************************************************
#*************REPLACE CODE IN WALK() WITH YOUR ANT'S STRATEGY***********
def walk(who):
    """move turtle randomly around the board 
       This is a very basic algorithm.  Feel free to try a different one
       or just change the numbers to see the effect.
    """
    who.forward(random.randint(-100,100))
    who.right(random.randint(-90, 70))
#***********************************************************************
#***********************************************************************
   
def get_back(who, board_size):
    #stay inside boundary, turtle can pass boundary, but will turn back
    where = who.position()
    global last_place

    if (abs(where[0]) > board_size or abs(where[1]) > board_size):
        #go to last spot.
        who.goto(last_place)
    else:
        #remember last spot
        last_place = where
    
def success(who, food_location,target_size=20):
    """Flag if player has found food (colision detection)
    define left, right, top and bottom of food rectangle
    right and up are positive
    """
    f_left=food_location[0]-target_size/2
    f_right=food_location[0]+target_size/2
    f_top=food_location[1]+target_size/2
    f_bottom=food_location[1]-target_size/2
    ax = who.position()[0]
    ay = who.position()[1]

    if (ax > f_left) and (ax < f_right) and (ay < f_top) and (ay > f_bottom):
        return True
        
def median(list):
    """Finds median of scores of all the runs.
    Half the games take fewer moves and half take more.
    A (useful) side effect of this function is that is sorts the list 
    """
    length = len(list)
    middle = length // 2
    list.sort()
    if length % 2 == 1:         #odd number
        med = list[middle]
    else:                       #even number
        middle = length // 2
        med = (list[middle - 1] + list[middle]) /2
    return med 
    
def count(moves):
    # remember how many moves each run takes
    games.append (moves)

def end(who):
    """Do some statistics
    Once the player class is being used, save scores, to compare
    different strageies
    """
    who.hideturtle()
    turtle.clear()
    who.penup()
    range=int(max (scores) - min (scores))
    avg = float(sum(scores))/len(scores)
    avg = round(avg,2)
    med = median(scores)
    who.setx(-200)
    who.write("Average number of moves per game: " + str(avg) + " In "+ str(len(scores)) + " tries",False,"left","60px")
    who.sety(-40)
    who.write("Median: " + str(med),False,"left","60px")
    who.sety(-80)
    who.write("Best game: " + str(min(scores)) + " moves. Worst game: " + str(max(scores)) + " moves", False, "left","60px")
    who.sety(-120)
    who.write("Range: " + str(range) ,False,"left","60px")
       
    wndow.exitonclick()
    
    #save results to 3 text files.  You can use this information to test
    #your ant's food gathering ability.  
    #.csv files are used by programs like spreadsheets
    
    #This one is for people to read directly
    f = open('antgame_results.txt','a')
    f.write('Average = '+ str(avg)+':')
    f.write('Median =' + str(med)+ ':')
    f.write('Min = '+ str(min(scores))+':')
    f.write('Max = '+ str(max(scores))+':')
    f.write('Range = '+ str(range)+':')
    f.write('Tries = '+ str(len(scores))+':')
    #f.write('Raw Scores = '+str(scores)+'\n')
    f.close()

    #The data from this file can be easily made in a spreadsheet chart
    f = open('antgame_histogram.csv','w')        #just keep last run
    run_number = 1
    s={}             #dict for 
    for score in scores:
        s[score]=scores.count(score)
    for key, value in s.items():
        f.write( str(key) +','+  str(value) + '\n')
    f.close()    
    
    #This one can be loaded into a spreadsheet for analysis
    #The headings are'Average,'+'Min,'+'Max,'+'Range,'+ '# of Tries\
    f = open('antgame_results.csv','a')
    f.write(str(avg)+',')
    f.write(str(med)+',')
    f.write(str(min(scores))+',')
    f.write(str(max(scores))+',')
    f.write(str(range)+',')
    f.write(str(len(scores))+'\n')
    f.close()
    
#***********************************  Game  ****************
#Ants wander around looking for food
scores=[]

def main():
    #our ant is called anti
    board_size, moves_allowed, moves_used, food_location, food_size = setup(anti)
    anti.speed(0)
    while True:
        get_back(anti, board_size)     # check that ant has not gone too far
        walk(anti)                     # simpler function
        if success(anti, food_location, food_size):
             anti.stamp()
             anti.hideturtle()
             anti.penup()
             scores.append(moves_used + 1)
             #print(scores)
             break
            
        moves_used = moves_used + 1
        if moves_allowed == moves_used:
            #a.write ("You have expired! ",True,"center","40px")
            scores.append(moves_used + 1)
            print(scores)
            break
            
#Runs  game multiple times 
for i in range (number_of_runs):
    main()
    anti.reset()

end(anti)
