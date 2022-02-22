from tkinter import *  # with this syntax we don't need we don't need "tkinter.[]"

window =  Tk()
window.title('Good Things Come to Those Who Work')
window.minsize(height=300, width=500)
window.config(padx=20, pady=20)

def buttonClicked():
  myLabel['text'] = input.get()

#Label

myLabel = Label(text='Label McLableton', font=('Arial', 24, 'italic'))
myLabel['text'] = 'New Labelism'
myLabel.grid(column=0, row=0)
# myLabel.config(text='newnewss')




button = Button(text='click me', command=buttonClicked)
button.grid(column=1, row=1)
button2 = Button(text='click me', command=buttonClicked)
button2.grid(column=2, row=0)

input = Entry()
input.grid(column=3, row=2)

window.mainloop()
