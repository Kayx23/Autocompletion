from BuildEnglishTrie import loadTrie
from tkinter import *

# build trie
trie = loadTrie()

# window config
window = Tk()
window.title("Word Check")
window.geometry('370x130')

# label
Label(window,
      text='Enter a word below to check if it is valid',
      font="Arial 14 bold").grid(row=0, column=0, padx=30, pady=20)

msg = Label(window, foreground="Red")
msg.grid(row=2, column=0)


# function to update word to whatever there is in the input box
def updateWord(*args) -> None:
    """Called whenever the user writes to the 'Input' Entry."""
    Word = Input.get()
    if not trie.existWord(Word):
        Input.config({"foreground": "Red"})
        msg.config(text='Not a valid word!')
    else:
        Input.config({"foreground": "Black"})
        msg.config(text='')


# define val as StringVar so we can track "write" using trace_add
val = StringVar()
val.trace_add("write", updateWord)

# Entry; set textvariable of the Entry as val
Input = Entry(window, textvariable=val, width=15)
Input.grid(row=1, column=0, padx=30)

window.mainloop()