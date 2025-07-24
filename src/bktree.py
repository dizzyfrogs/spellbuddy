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

    def search(self, word, tolerance):
        """
        Search for all words within tolerance distance of the given word
        Returns a list of tuples: (matching_word, distance).
        """

        results = []

        def dfs(node):
            dist = self.distance_func(word, node.word)
            if dist <= tolerance:
                results.append((node.word, dist))

            # explore eligible child nodes
            for d in range(dist - tolerance, dist + tolerance + 1):
                child = node.children.get(d)
                if child is not None:
                    dfs(child)

        if self.root is not None:
            dfs(self.root)
            
        return sorted(results, key=lambda x: x[1])