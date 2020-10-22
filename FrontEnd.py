from tkinter import *

# window config
window = Tk()
window.title("Autocompletion")
window.geometry('300x80')

# label
Label(window, text='Word', font="Arial 14 bold").grid(row=0,
                                                      column=0,
                                                      padx=30,
                                                      pady=20)


# function to update word to whatever there is in the input box
def updateWord(*args) -> None:
    """Called whenever the user writes to the 'Input' Entry."""
    Word = Input.get()
    # print(Word)


# define val as StringVar so we can track "write" using trace_add
val = StringVar()
val.trace_add("write", updateWord)

# Entry; set textvariable of the Entry as val
Input = Entry(window, textvariable=val, width=15)
Input.grid(row=0, column=1, pady=20)

window.mainloop()