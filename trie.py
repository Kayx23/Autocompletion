# Data Structure: Trie (where each letter node stores one letter)
# This is an alternative implementation using nested dictionaries as opposed to using nodes that I found quite interesting
# Inspiration: https://youtu.be/hjUJFjcrbR4


class Trie:
    """
    A Trie implemented using nested dictionaries. 
    The start of the trie and the end (of a word) are indicated by a "*"
    """
    def __init__(self) -> None:
        self.root = {"*": "*"}  # a dictionary

    def addWord(self, word: str) -> None:
        """Adds a word."""
        curr_trie = self.root
        for letter in word:
            if letter not in curr_trie:
                # create a dictionary under that letter
                curr_trie[letter] = {}
            # move down one level
            curr_trie = curr_trie[letter]
        # now we're at the end of the word
        curr_trie["*"] = "*"

    def existWord(self, word: str) -> None:
        """Checks if a word exist in the trie; returns a Boolean value."""
        curr_trie = self.root
        for letter in word:
            if letter not in curr_trie:
                return False
            else:
                # move down one level
                curr_trie = curr_trie[letter]
        # finally make sure the end of word mark is there
        return "*" in curr_trie