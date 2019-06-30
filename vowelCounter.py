from tkinter import*
import tkinter.messagebox

        
root = Tk ()
root.title("count vowels App")
root.geometry("600x700+0+0")
root.configure(background = "black")
        
#variables
enterWord = StringVar()
vowelNumber = StringVar()
           # n is our counter
n = IntVar()

#functions
def quit():
    quit =tkinter.messagebox.askyesno("vowels counter"," Do you want to close program?")
    if quit > 0:
        root.destroy()
        return
def reset():
    enterWord.set(" ")
    vowelNumber.set(" ")
    txtcountVowels.delete("1.0",END)
def countVowels():
    txtcountVowels.delete("1.0",END)
    s = (enterWord.get())
    n = 0
    
    for letter in s:
        txtcountVowels.insert(END, letter + "\n")
        textInput = (letter)
        
        if letter == "a" or letter == "e" or letter == "A" or letter == "E":
            n = n+1
        elif letter == "i" or letter == "o" or letter == "u" or letter == "I" or letter == "O" or letter == "U" :
            n = n+ 1
    txtcountVowels.insert(END, letter + "\n The number of vowels is :" + str(n))
    vowelNumber.set(n)
    
           
#Main Frame
mainFrame = Frame(root)
mainFrame.grid()
           
topFrame = Frame(mainFrame, bd = 20, width = 1350, relief = RIDGE)
topFrame.pack(side=TOP)

lblTitle = Label(topFrame, padx = 74,  font = ('arial',40,'bold'), text = "Count vowels" )
lblTitle.grid()
           
countFrame = Frame(mainFrame, width = 1350, height = 500, pady = 5, relief = RIDGE, bd = 20)
countFrame.pack(side = BOTTOM)
           
countVowelsBtnFrame= Frame( countFrame, width = 450, height = 400, relief = RIDGE, bd = 10)
countVowelsBtnFrame.pack()
           
frameName = LabelFrame(countVowelsBtnFrame, width = 150, height = 250, bd = 10, font = ('arial',12,'bold'), text ="Vowel Counter", relief = RIDGE)
frameName.grid(row = 0, column = 0)
           
countVowelsFrame = LabelFrame(countVowelsBtnFrame, width = 350, height = 300,  font = ('arial',12,'bold'), text ="Count Vowels", relief = RIDGE)
countVowelsFrame.grid(row = 1, column = 0)
           
buttonFrame = LabelFrame(countVowelsBtnFrame, width = 350, height = 100, relief = RIDGE)
buttonFrame.grid(row = 2, column = 0)

#Widgets
##Enter word
lblenterWord = Label(frameName, font = ('arial',12,'bold'), padx = 20, text = "Enter words here", bd = 7)
lblenterWord.grid(row = 0, column = 0, sticky = W)
txtenterWord = Entry(frameName, font = ('arial',12,'bold'), textvariable = enterWord, bd = 7, insertwidth = 4, justify = LEFT)
txtenterWord.grid(column = 1, row = 0)

##Display number of vowels
lblvowelNumber = Label(frameName, font = ('arial',12,'bold'), padx = 20, text = "Number of Vowels", bd = 7)
lblvowelNumber.grid(row = 2, column = 0, sticky = W)
txtvowelNumber = Entry(frameName, font = ('arial',12,'bold'), textvariable = vowelNumber, bd = 7, insertwidth = 4, justify = LEFT)
txtvowelNumber.grid(column = 1, row = 2)

#Text widget
txtcountVowels = Text(countVowelsFrame, width = 40, height = 10, font = ('arial',12,'bold'))
txtcountVowels.grid(row = 1, column = 0)

#Buttons
btnCountVowels = Button(buttonFrame, padx = 18, bd =7, font = ('arial',16,'bold'), width = 8, text = "Count", bg ='green', command = countVowels).grid(padx = 8, column = 0, row = 0)
btnReset = Button(buttonFrame, padx = 18, bd =7, font = ('arial',16,'bold'), width = 8, text = "Reset", bg ='grey', command = reset).grid(padx = 9, column = 1, row = 0)
btnExit = Button(buttonFrame, padx = 18, bd =7, font = ('arial',16,'bold'), width = 8, text = "Exit", bg = 'red', command = quit).grid(padx = 9, column = 2, row = 0)


        
        
        

root.mainloop ()
        