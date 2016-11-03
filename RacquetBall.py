def RaquetBall():
	probA,probB,n=getinputs()
	winsA,winsB=RBallsim(probA,probB,n)
	print(winsA,winsB)

def getinputs():
	try:
	    Pa=eval(input("What is the chance of Person A winning their serve(decimal)? "))
	    while Pa<0 or Pa>1:
		    print("Person A Win Percentage Input Invalid")
		    Pa=eval(input("What is the chance of Person A winning their serve(decimal)? ")) 
	    Pb=eval(input("What is the chance of Person B winning their serve(decimal)? "))
	    while Pb<0 or Pb>1:
		    print("Person B Win Percentage Input Invalid")
		    Pb=eval(input("What is the chance of Person B winning their serve(decimal)? ")) 
	    n=eval(input("How many games do they play? "))
	    while n<0:
		    print("Invalid Game Number")
		    n=eval(input("How many games do they play? "))
	except:
	    print("Error: Must enter a number for input.")
	    getinputs()
	return Pa,Pb,n
def RBallsim(probA,probB,n):
    #assume Player A always serves first
    from random import random
    Pa,Pb=probA,probB
    winsA=winsB=0
    for i in range(n):
        serve="A"
        ScoreA=ScoreB=0
        while ScoreA<15 and ScoreB<15:
            if serve=="A":
                if random()<Pa:
                    ScoreA+=1
                else:
                    serve="B"
            else:
                if random()<Pb:
                    ScoreB+=1
                else:
                    serve="A"
        if ScoreA==15:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB
def PrintFinal(winsA,winsB):
    print("Player A wins "+str(winsA)+" games and Player B wins "+str(winsB)+" games")
RaquetBall()
