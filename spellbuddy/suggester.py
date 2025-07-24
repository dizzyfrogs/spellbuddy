from spellbuddy.bktree import BKTree
from spellbuddy.edit_distance import edit_distance

class SpellingSuggester:
    def __init__(self, word_list):
        """
        Build BK-tree using the given word list.
        """
        self.tree = BKTree(edit_distance)
        for word in word_list:
            self.tree.insert(word.lower())

    def suggest(self, word, tolerance=2):
        """
        Suggest words from the dictionary within the given edit distance tolerance.
        Returns a list of (word, distance) tuples, sorted by distance.
        """
        return self.tree.search(word.lower(), tolerance)
