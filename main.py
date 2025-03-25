from tkinter import *

def main():
    # Create the main window
    root = Tk()
    
    root.title("Custom calculator") #ikkunan otsikko
    root.geometry("300x200") #ikkunan koko

    frame = Frame(root)

# geometry method
    frame.pack()
    # Create a label widget
    label = Label(root, text='Tästä tulee vielä joskus oma laskin!')
    label.pack()

    button1 = Button(frame, text='1')
    button1.pack(side = LEFT, expand = True)

    button2 = Button(frame, text='2')
    button2.pack(side = LEFT, expand = True)


    button3 = Button(frame, text='3')
    button3.pack(side = LEFT, expand = True)

    button4 = Button(frame, text='4')
    button4.pack(side = LEFT, expand = True)

    button5 = Button(frame, text='5')
    button5.pack(side = LEFT, expand = True)

    button6 = Button(frame, text='6')
    button6.pack(side = LEFT, expand = True)

    button7 = Button(frame, text='7')
    button7.pack(side = LEFT, expand = True)

    button8 = Button(frame, text='8')
    button8.pack(side = LEFT, expand = True)

    button9 = Button(frame, text='9')
    button9.pack(side = LEFT, expand = True)





    
    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()