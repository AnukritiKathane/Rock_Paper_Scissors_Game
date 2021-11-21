#Player1 name: Rashi
#Player2 name: Vashi

def rock_paper_scissors(num1,num2,bit1,bit2):
  p1=int(num1[bit1])%3
  p2=int(num2[bit2])%3
  if(player1[p1]==player2[p2]):
    print("Draw")
  elif(player1[p1]=="Scissors" and player2[p2]=="Rock"):
    print("Vashi wins:)),Rashi has scissors and Vashi has rock")
  elif(player1[p1]=="Scissors" and player2[p2]=="Paper"):
    print("Rashi wins:)),Rashi has scissors and Vashi has Paper")
  elif(player1[p1]=="Rock" and player2[p2]=="Paper"):
    print("Vashi wins:)),Rashi has Rock and Vashi has Paper")
  elif(player1[p1]=="Rock" and player2[p2]=="Scissors"):
    print("Rashi wins:)),Vashi has scissors and Rashi has rock")  
  elif(player1[p1]=="Paper" and player2[p2]=="Scissors"):
    print("Vashi wins:)),Vashi has scissors and Rashi has Paper")  
  elif(player1[p1]=="Paper" and player2[p2]=="Rock"):
    print("Rashi wins:)),Rashi has Paper and Vashi has rock")    

player1={0: "Rock",1: "Paper",2:"Scissors"}
player2={0: "Paper",1:"Rock", 2:"Scissors"}
while(1):
    num1=input("Rashi,Enter your choice ")
    num2=input("Dear Vashi,Enter your choice ")
    bit1=int(input("Rashi,Enter secret bit position"))
    bit2=int(input("Dear Vashi,Enter secret bit position"))
    rock_paper_scissors(num1,num2,bit1,bit2)
    ch=input("Do u wanna continue ? y/n") 
    if(ch=='n'):
        break

   
