from BuildTrie import loadTrie
from tkinter import *

# build trie
trie_en = loadTrie('en')
trie_fr = loadTrie('fr')

language = 'en'

# window config
window = Tk()
window.title('Word Check')
window.geometry('390x130')

# label
Label1 = Label(window,
               text='Enter a word below to check if it is valid',
               font='Arial 14 bold',
               width=35)
Label1.grid(row=0, column=0, padx=30, pady=20)

msg = Label(window, foreground='Red')
msg.grid(row=2, column=0)


# function to update word to whatever there is in the input box
def checkWord(*args) -> None:
    """Called whenever the user writes to the 'Input' Entry."""
    Word = Input.get()
    # look up word in the respective trie
    if not eval("trie_" + language).existWord(Word):
        Input.config({'foreground': 'Red'})
        if language == 'en':
            msg.config(text='Not a valid word!')
        else:
            msg.config(text='Pas un mod valide!')
    else:
        Input.config({'foreground': 'Black'})
        msg.config(text='')


# define val as StringVar so we can track 'write' using trace_add
val = StringVar()
val.trace_add('write', checkWord)

# Entry; set textvariable of the Entry as val
Input = Entry(window, textvariable=val, width=15)
Input.grid(row=1, column=0, padx=30)


def switchLanguage():
    """Called when the language button is hit."""
    global language  # need to udpate global var
    if lan['text'] == 'fr':
        language = 'fr'
        lan.config(text='en')
        window.title('Vérification d\'Orthographe')
        Label1.config(text='Entrez un mot pour vérifier s’il est valide')
        checkWord()
    else:
        language = 'en'
        lan.config(text='fr')
        window.title('Word Check')
        Label1.config(text='Enter a word below to check if it is valid')
        checkWord()


# language buttom
lan = Button(window, text='fr', width=3, pady=5, command=switchLanguage)
lan.grid(row=0, column=1)

window.mainloop()