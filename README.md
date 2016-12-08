# ant_world

Python Ants (P-ants)
You are an ant looking for the last bit of food.
This is the basic code. We start by making a turtle object, called ant, and a window to be the ant's
world. The ant wanders around aimlessly in the main loop. First forward or backward, then turns to a
random new direction. I know, an ant is not a turtle, but it is close enough for this to work. Trust me.
```
  import turtle
  import random
  window=turtle.Screen()
  ant=turtle.Turtle()
  
  while True:
  ant.forward(random.randint(-20,80))
  ant.right(random.randint(-75, 120))
```

Once this is working, we can add some new functions to keep it from wandering off the screen, and
know when it has found food.
I've expanded the program to help find out the best strategy and produce the fittest ant. This is a
simulation of what happens in the real world as creatures evolve to succeed in their environment. Any
animal that is more successful at finding food is going to be able to have more offspring and will pass
their genes to them. Any animal that cannot find food (or gets sick or is eaten) dies and has no
children.
A simulation on a computer is when you try to make a computer model of something in the real world,
like the weather, evolution, or the stock market. A good one can be very helpful. This one could be
helpful for our Robot competition.
Your assignment is to program the fittest Python Ant that can find the food before any other ants in a
head to head, on screen competition.
Rules
•
 
•
Ant's are not especially smart, at least not a single ant. However, there a lot of them so they
must be doing something right. Your ant can only wander about in her world until she stops at
the place food is.
Food is placed randomly in the field by the computer.
You can only change the code in sub walk() and must use the default settings
You will run your ant against another student's 3 times. The first to get to the food 2 times
wins and goes on the the next round.
There are also prizes for the best name and the most stuck or lost ant.How to proceed
• The program can be set to run automatically many times and collect all the results. You can try
different strategies and see which seems to work the best. Read the code, especially the names
of the functions. Even if you do not understand all the Python yet. For example def end() runs
the code to end the program and def success() checks to see if the ant has found the food.
• Think of how you want your ant to wander. Randomly? In circles? Back and forth in lines,
the way you would if you lost your car at the mall?
• Translate your idea into turtle. https://docs.python.org/3/library/turtle.html#turtle.home
explains turtle and we will go over that in class.
• The code for that should go into sub walk() and can replace mine.
• Let the program run. It is set to automatically run 100 times and will keep track of how many
moves it took your ant to find the food as well as the average number of moves and the range
between your best and worst run. Smaller is better. In math this is called the range and smaller
is also better.
• Save your code and try a completely new strategy. Run this and compare your average and
range. Do this at least 3 times.
• Submit your best def move() for the competition.
May the best ant win
