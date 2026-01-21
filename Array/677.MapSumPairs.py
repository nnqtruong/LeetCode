class TrieNode:    
    def __init__(self):   
        self.children = {}        
        self.sum_value = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}
        

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta = val - self.map[key]

        self.map[key]=val

        #traverse and update_sums
        node = self.root
        node.sum_value += delta

        for char in key:
            if char not in node.children:
                node.children[char]=TrieNode()
            node = node.children[char]
            node.sum_value += delta 

    def sum(self, prefix: str) -> int:
        node =self.root
        
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]

        return node.sum_value
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)