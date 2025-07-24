class BKTreeNode:
    def __init__(self, word):
        self.word = word
        self.children = {} # keys - distances, values - BKTreeNode

class BKTree:
    """Implementing Burkhard-Keller tree"""
    def __init__(self, distance_func):
        self.root = None
        self.distance_func = distance_func
    
    def insert(self, word):
        if self.root is None:
            self.root = BKTreeNode(word)
            return

        curr = self.root
        while True:
            dist = self.distance_func(word, curr.word)

            if dist in curr.children:
                curr = curr.children[dist]
            else:
                curr.children[dist] = BKTreeNode(word)
                break
