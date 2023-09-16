# tkinter for GUI
from tkinter import *
COUNT = 0

#To limit number of total queens to four
def increment():
    global COUNT
    COUNT = COUNT+1
def decrement():
    global COUNT
    COUNT = COUNT-1
def checkCount():
    global COUNT
    if COUNT<4:
        return True
    return False
def isCount4():
    global COUNT
    if COUNT==4:
        return True
    return False

#Flag to detect all Queens are safe or not
FLAG = 0
def setFLAG():
    global FLAG
    FLAG = 1
def unsetFLAG():
    global FLAG
    FLAG = 0
def isFLAGset():
    global FLAG
    if FLAG==0:
        return True
    return False

#To place Queen
def move(row,column):
    if isFLAGset() is True:
        label.config(text=(" Place queen 👑 "),font=('consolas',25,'bold'),fg='blue')
    if buttons[row][column]['text'] == "" and checkCount() is True and isFLAGset() is True:
        stateofboaed(row,column)
        buttons[row][column]['text'] = "👑"
        increment()
       
    elif buttons[row][column]['text'] == "👑" :
        buttons[row][column]['text'] = ""
        changeOnRemove(row,column)
        global count
        decrement()
   
    if isCount4() is True and isFLAGset() is True:
        label.config(text=("❤🎉Congragulation🎉❤"),font=('segoe print',40,"bold"),fg='green',bg='#DDFFE9')
        setFLAG()

#Change after removing queen
def changeOnRemove(row,column):
    
#for column
    for i in range(4):
        if((row+i)%2==0):
            buttons[row][i]['bg'] = "#FFE4C1"
        else:
            buttons[row][i]['bg'] = "#822121" 
        unsetFLAG()
        label.config(text=(" Place queen 👑 "),font=('consolas',25,'bold'),fg='blue')

#for row
    for i in range(4):
        if((column+i)%2==0):
            buttons[i][column]['bg'] = "#FFE4C1"
        else:
            buttons[i][column]['bg'] = "#822121" 
        unsetFLAG()
        label.config(text=(" Place queen 👑 "),font=('consolas',25,'bold'),fg='blue')
   
#for left top diagonal
    i = row-1
    j = column-1
    while(i>=0 and j>=0):
        if buttons[i][j]['text'] == "👑":
            if((j+i)%2==0):
              buttons[i][j]['bg'] = "#FFE4C1"
            else:
             buttons[i][j]['bg'] = "#822121" 
            
            unsetFLAG()
            label.config(text=(" Place queen 👑 "),font=('consolas',25,'bold'),fg='blue')
        i = i-1
        j = j-1

    i = row-1
    j = column+1
    
#for right top diagonal
    while(i>=0 and j<4):
        if buttons[i][j]['text'] == "👑":
            if((j+i)%2==0):
              buttons[i][j]['bg'] = "#FFE4C1"
            else:
             buttons[i][j]['bg'] = "#822121" 
            unsetFLAG()
            label.config(text=(" Place queen 👑 "),font=('consolas',25,'bold'),fg='blue')
        i = i-1
        j = j+1

#for left bottom diagonal
    i = row+1
    j = column-1
    while(i<4 and j>=0):
        if buttons[i][j]['text'] == "👑":
            if((j+i)%2==0):
              buttons[i][j]['bg'] = "#FFE4C1"
            else:
             buttons[i][j]['bg'] = "#822121" 
            unsetFLAG()
            label.config(text=(" Place queen 👑 "),font=('consolas',25,'bold'),fg='blue')
        i = i+1
        j = j-1

#for right bottom diagonal
    i = row+1
    j = column+1
    while(i<4 and j<4):
        if buttons[i][j]['text'] == "👑":
            if((j+i)%2==0):
              buttons[i][j]['bg'] = "#FFE4C1"
            else:
             buttons[i][j]['bg'] = "#822121" 
            unsetFLAG()
            label.config(text=(" Place queen 👑 "),font=('consolas',25,'bold'),fg='blue')
        i = i+1
        j = j+1
   
#After placing queen checking all quenes are safe or not   
def stateofboaed(row,column):
    for i in range(4):
        if buttons[row][i]['text'] == "👑":
            buttons[row][i]['bg'] = "#FF4D4A"
            setFLAG()
            label.config(text=(" Backtrack current move "),font=('consolas',25,'bold'),fg='#FD0210',bg='#A9FFD8')
    for i in range(4):
        if buttons[i][column]['text'] == "👑":
            buttons[i][column]['bg'] = "#FF4D4A"
            setFLAG()
            label.config(text=(" Backtrack current move "),font=('consolas',25,'bold'),fg='#FD0210',bg='#A9FFD8')
   
    i = row-1
    j = column-1
    while(i>=0 and j>=0):
        if buttons[i][j]['text'] == "👑":
            buttons[i][j]['bg'] = "#FF4D4A"
            setFLAG()
            label.config(text=(" Backtrack current move "),font=('consolas',25,'bold'),fg='#FD0210',bg='#A9FFD8')
        i = i-1
        j = j-1

    i = row-1
    j = column+1
    while(i>=0 and j<4):
        if buttons[i][j]['text'] == "👑":
            buttons[i][j]['bg'] = "#FF4D4A"
            setFLAG()
            label.config(text=(" Backtrack current move "),font=('consolas',25,'bold'),fg='#FD0210',bg='#A9FFD8')
        i = i-1
        j = j+1

    i = row+1
    j = column-1
    while(i<4 and j>=0):
        if buttons[i][j]['text'] == "👑":
            buttons[i][j]['bg'] = "#FF4D4A"
            setFLAG()
            label.config(text=(" Backtrack current move "),font=('consolas',25,'bold'),fg='#FD0210',bg='#A9FFD8')
        i = i+1
        j = j-1

    i = row+1
    j = column+1
    while(i<4 and j<4):
        if buttons[i][j]['text'] == "👑":
            buttons[i][j]['bg'] = "#FF4D4A"
            setFLAG()
            label.config(text=(" Backtrack current move "),font=('consolas',25,'bold'),fg='#FD0210',bg='#A9FFD8')
        i = i+1
        j = j+1



def new_game():
    pass

# function to create Solution window
def openNewWindow():
     
    newWindow = Toplevel(window)
 
    newWindow.title("New Window")
    newWindow.configure(bg='#B2B2FF')
 
    newWindow.geometry("600x600")
    Label(newWindow,
          text ="💡♟ Solution ♟💡",font=('consolas',32,'bold'),fg='#5E00F8',bg='#FFFFB2').pack(pady=45)
    
    buttons2 = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    
    solveUntil(buttons2,0);
    #printSolution(buttons2);
    
    frame2 = Frame(newWindow,highlightbackground="#191919", highlightthickness=10)
    frame2.pack(pady=10)

    for row in range(4):
        for column in range(4):
            ans = buttons2[row][column]
            if(ans==0):
                ans2 = ""
            else:
                ans2="👑"
            if((row+column)%2==0):
                 buttons2[row][column] = Button(frame2, text=ans2,bd=4,font=('consolas',30), width=3, height=1,bg="#FFF4E6")
            else:
             buttons2[row][column] = Button(frame2, text=ans2,bd=4,font=('consolas',30), width=3, height=1,bg="#822121")          
           
            buttons2[row][column].grid(row=row,column=column)

    
#Backtracking code for Solution

global N
N = 4


def isSafe(board, row, col):
    
#check queens along row
	for i in range(row):
		if board[i][col] == 1:
			return False
        
#check queens along left top diagonal
	for i, j in zip(range(row, -1, -1),
					range(col, -1, -1)):
		if board[i][j] == 1:
			return False
        
#check queens along right top diagonal
	for i, j in zip(range(row, -1, -1),
					range(col, N, +1)):
		if board[i][j] == 1:
			return False

	return True

#Placing queens from row 1 to row 4 using recursive function to implement backtracking
def solveUntil(board, row):
	
	if row >= N:
		return True

	for i in range(N):
#for row=row checking every column  
		if isSafe(board, row,i):
			
			board[row][i] = 1
			
			if solveUntil(board, row + 1) == True:
				return True

			
			board[row][i] = 0

	
	return False


    
# main window using tkinker library
    
window = Tk()
window.title("4 Queen")
window.geometry("750x750")
window.configure(bg='#FFDDF3')
label = Label(text =" 👑 Start Game  ",font=('consolas',25,"bold"),fg='#003AFF',bg='#1FFF00')
label.pack(pady=70,side="top")

# initiliazing board as 4x4 matrix
buttons = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

# creating frame within window
frame = Frame(window,highlightbackground="#d24e4e", highlightthickness=20)
frame.pack(pady=10)

#for GUI color and Button to take input from GUI to code
for row in range(4):
    for column in range(4):
        if((row+column)%2==0):
             buttons[row][column] = Button(frame, text="",bd=4,font=('consolas',30), width=3, height=1,bg="#FFE4C1",
                                      command= lambda row=row, column=column:move(row,column))
        else:
         buttons[row][column] = Button(frame, text="",bd=4,font=('consolas',30), width=3, height=1,bg="#822121",
                                      command= lambda row=row, column=column:move(row,column))          
       
        buttons[row][column].grid(row=row,column=column)

#Help button to open solution window
reset_button = Button(text="Help", font=('consolas',), command=openNewWindow)
reset_button.pack(pady=30)

window.mainloop()