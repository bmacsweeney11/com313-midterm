from graphics import *
from ClassButton import *
from random import *

def main():
    win=GraphWin("com313Midterm", 600,600)
    win.setBackground("green")
    welcome = Text(Point(300,300), "In this project a simulation will be run where altruist and egoist will either keep or change there viewpoint.")
    welcome1 = Text(Point(300,320), "Press anywhere to start")
    welcome.setSize(14)
    welcome.setFill("black")
    welcome.draw(win)
    welcome1.setSize(15)
    welcome1.setFill("black")
    welcome1.draw(win)
    pt = win.getMouse()
    

    manual = Button(win, Point(100, 500), 100, 100, "Manual Input")
    automatic = Button(win, Point(300, 500), 100, 100, "Automatically Generated Input")
    exitbutton = Button(win, Point(580, 500), 30, 30, "Exit")
    pt = win.getMouse()
    welcome1.undraw()
    welcome.undraw()
    welcome3.undraw()
    
    easypic=False
    mediumpic=False
    hardpic=False
    pic=0

    while not exitbutton.isClicked(pt):

        chars= Text(Point(300,250), "")
        chars.draw(win)
        turnCount=Text(Point(300,325), "")
        turnCount.draw(win)
        guess= Entry(Point(300,400),10)
        guess.draw(win)
        guessbutton = Button(win, Point(300, 430), 40, 30, "Guess")

        
        if manual.isClicked(pt):
            turns=11
            easy="easy.txt"
            words=open(easy,'r').read()
            easypic=True
            pic = 0
            words=words.lower()
            word=words.split()
            word2=randrange(0,len(word))
            word3=word[word2]
            print(word3)
            while turns > 0: 
                Hangman.turnCounter(win, guess, word3)
                dash=[" __  "]
                dash=dash*len(word3)
                
                for blank in range(len(dash)):
                    drawDash=Point(300+blank*30,300)
                    draws=Text(drawDash, "  __  ")
                    draws.draw(win) 
                pic, turns = Hangman.play_game(win,word3,guess,pic,turns,turnCount)
                print(turns)
                pt = win.getMouse()
                if exitbutton.isClicked(pt):
                    win.close()
        elif automatic.isClicked(pt):
                if exitbutton.isClicked(pt):
                    win.close()

                    

        elif hardbutton.isClicked(pt):
                if exitbutton.isClicked(pt):
                    win.close()

        dash=[" __  "]
        dash=dash*len(word3)
        
        for blank in range(len(dash)):
            drawDash=Point(300+blank*30,300)
            draws=Text(drawDash, "  __  ")
            draws.draw(win)

         
        
main()
