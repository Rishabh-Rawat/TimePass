import random
import mysql.connector

def isvalid(a):
    '''This function checks whether the passed argument is a four digit number with non-repeating digits'''
    if a.isdigit() and  len(a)==4:
        for i in range(0,4):
            x=a[i]
            temp=list(a)
            del temp[i]
            if x in temp:
                return False
        else:
            return True
    else:
        return False
    
def key():
    '''This function generates a four digit number with non-repeating digits'''
    a=str(random.randint(1,9))
    b=str(random.randint(0,9))
    c=str(random.randint(0,9))
    d=str(random.randint(0,9))
    n=a+b+c+d
    while not isvalid(n):
        a=str(random.randint(1,9))
        b=str(random.randint(0,9))
        c=str(random.randint(0,9))
        d=str(random.randint(0,9))
        n=a+b+c+d
    return n


def game():
    global name
    name=input("Enter player's name")
    print("LET'S SEE IF YOU CAN GUESS A FOUR DIGIT NUMBER WITH NON-REPEATING DIGITS\n")
    k=key()                                                     # k variable stores the value of the key/answer
    global result
    global tries
    tries=1
    while True:
        g=input("Enter your guess")                             # g variable stores the value of the guess given by the user
        perfect=0                                               # perfect variable stores the number of digits which are at correct positon  
        correct=0                                               # correct variable stores the number of digits which are correct in the guess
        if isvalid(g):
            print("\n",tries,"st guess = ",g,sep="")            # this statement displays the nth guess by the user
            if k==g:
                message="\nCONGRATULATIONS! YOU WON IN "+str(tries)+" TRIES"
                result='W'
                break
            else:
                for i in range(0,4):
                    for j in range(0,4):
                        if k[i]==g[j] and i==j:                 # condition when the digit is placed at correct position
                            perfect+=1                            
                            correct+=1                          
                        elif k[i]==g[j]:                        # condition when the digit is present in key but not at correct position   
                            correct+=1
                        else:
                            continue
                print(correct,"digits in your number are correct")
                print(perfect,"digits are at perfect position")
            tries+=1
        else:
            print("Invalid Guess")
            continue
        ch=input("\nEnter Y to quit and N to continue\n").upper()
        if ch=="Y":
            message="YOU ARE A LOSER TO QUIT IN JUST "+str(tries-1)+" TRIES\nTHE ANSWER WAS = "+k
            result='L'
            break
        elif ch=="N":
            continue
        else:
            print("Invalid Choice entered\nNow continue the game")
            continue

    print(message)

#_main_
game()
while True:
        if result=='W':
            print("\nDo you want to save your last game score ?\n")
            ch=input("Enter Y for yes otherwise press any other key ").upper()
            if ch=='Y':
                mycon=mysql.connector.connect(host='localhost',user='root',database='rishabh',passwd='')
                cur=mycon.cursor()
                try:
                    cur.execute("insert into record values('{}',{})".format(name,tries))
                    mycon.commit()
                except:
                    cur.execute("create table record(name varchar(50) ,tries integer)")
                    cur.execute("insert into record values('{}',{})".format(name,tries))
                    mycon.commit()
                else:
                    print("Score Saved")
        ch=input("\nEnter Y to see previous winners' scores otherwise press any other key").upper()
        if ch=='Y':
            mycon=mysql.connector.connect(host='localhost',user='root',database='rishabh',passwd='')
            cur=mycon.cursor()
            try:
                cur.execute("select * from record order by tries")
                for i in cur.fetchall():
                    print(i[0],"had completed this game in",i[1],"tries")
            except:
                print("NO ONE HAD EVER COMPLETED THIS GAME")
        ch=input("Enter Y to play this game again otherwise press any other key")
        if ch=='Y':
            game()
        else:
            print("THANKS FOR PLAYING")
            break
