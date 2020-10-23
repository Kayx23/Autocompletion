from trie import Trie


def loadTrie(language: str) -> Trie:
    trie = Trie()

    if language == 'en':
        # taken from https://github.com/dwyl/english-words/blob/master/words_alpha.txt
        Words = open('WordList/English.txt', 'r')
    elif language == 'fr':
        # taken from https://www.freelang.com/download/misc/liste_francais.zip
        Words = open('WordList/French.txt', 'r', encoding='latin1')

    for word in Words:
        trie.addWord(word.rstrip('\n'))  # had to strip \n

    return trie
