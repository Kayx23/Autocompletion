from trie import Trie

trie = Trie()

# https://github.com/dwyl/english-words/blob/master/words_alpha.txt
Words = open('EnglishWords/words_alpha.txt', 'r')

for word in Words:
    trie.addWord(word.rstrip('\n'))  # had to strip \n