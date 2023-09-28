def display(arr=[[1,2,3],[4,5,6],[7,8,9]]):
    # we are representing the board with a list which has 3 lists inside corresponding to 3 rows ; by default this function prints the namespace showing which position is what 
    print("      |      |     ")
    print("  {0}   |  {1}   |  {2}   ".format(arr[0][0],arr[0][1],arr[0][2]))
    print("      |      |     ")
    print("-------------------")
    print("      |      |     ")
    print("  {0}   |  {1}   |  {2}   ".format(arr[1][0],arr[1][1],arr[1][2]))
    print("      |      |     ")
    print("-------------------")
    print("      |      |     ")
    print("  {0}   |  {1}   |  {2}   ".format(arr[2][0],arr[2][1],arr[2][2]))
    print("      |      |     ")

def choice():
    while True:
        p1=input("Player 1 : X or O? ")
        if p1== "X" or p1=="O":break
        else: print("Invalid Choice")
    p2= "X" if p1=="O" else "O"
    print("Alright player1 is",p1,"and player2 is",p2)
    return p1,p2

def validPos(var,lst):
    if var.isdigit():
        var=int(var)
        if var <1 or var>9: return False
        else:
            if var in [1,2,3]:
                if lst[0][var-1]!="_":return False
            if var in [4,5,6]:
                if lst[1][var-4]!="_":return False
            if var in [7,8,9]:
                if lst[2][var-7]!="_":return False
            return True
    else: 
        return False

def mark(lst,pos,symbol):
    if pos in [1,2,3]:
        lst[0][pos-1]=symbol
    if pos in [4,5,6]:
        lst[1][pos-4]=symbol
    if pos in [7,8,9]:
        lst[2][pos-7]=symbol


def game(p1,p2):
    l=[['_','_','_'],['_','_','_'],['_','_','_']]
    print("Choose which position you enter according to this: ")
    display()
    while True:
        cho=input("Player1 enter position (1-9) or type \"help\" if you want to see the table again: ")
        
        if cho=="help":
            display()
            continue
        
        if validPos(cho,l):
            cho=int(cho)
            mark(l,cho,p1)
            display(l)
        else:
            print("Invalid Choice")
            continue

        if(checkwin(l)):
            print("Player1 WINS!")
            ch=input("Play again Y or N? ")
            if ch=="Y":
                p1,p2=choice()
                game(p1,p2)
                break
            else:
                break       
       
        if not(checkEmpty(l)):
            print("Draw")
            ch=input("Play again Y or N? ")
            if ch=="Y":
                p1,p2=choice()
                game(p1,p2)
                break
            else:
                break 

        while True:
            ch=input("Player2 enter position (1-9) or type \"help\" if you want to see the table again: ")
            if ch=="help":
                display()
                continue
            
            if validPos(ch,l):
                ch=int(ch)
                mark(l,ch,p2)
                display(l)
                break
            else:
                print("Invalid Choice")
                continue
        
        if(checkwin(l)):
            print("Player2 WINS!")
            ch=input("Play again Y or N? ")
            if ch=="Y":
                p1,p2=choice()
                game(p1,p2)
                break
            else:
                break 
        
        if not(checkEmpty(l)):
            print("Draw")
            ch=input("Play again Y or N? ")
            if ch=="Y":
                p1,p2=choice()
                game(p1,p2)
                break
            else:
                break 

def checkwin(table):
    win = False
    #checking horizontally
    for i in range(3):
        if table[i][0] == table[i][1] and table[i][1] == table[i][2] and table[i][0]!="_":
            return True
    #checking vertically
    for i in range(3):
        if table[0][i] == table[1][i] and table[1][i] == table[2][i] and table[0][i]!="_":
            return True
    #checking diagonally
    win = False
    if table[0][0] == table[1][1] and table[1][1] == table[2][2] and table[0][0]!="_": 
        win=True
    if table[0][2] == table[1][1] and table[1][1] == table[2][0] and table[0][2]!="_": 
        win=True
    return win

def checkEmpty(l):
    empty=False
    for row in l:
        for el in row:
            if el=="_":
                empty=True
    return empty

p1,p2=choice()
game(p1,p2)