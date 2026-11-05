class Trie:
    def __init__(self):
        self.array = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            index = ord(c) - ord('a')
            if cur.array[index] == None:
                cur.array[index] = Trie()
            cur = cur.array[index]
        cur.end = True

    def search(self, word: str) -> bool:

        def dfs(node, index):
            if index == len(word):
                return node.end
            if word[index] == ".":
                for trie in node.array:
                    if trie:
                        if dfs(trie, index+1):
                            return True
                return False
            else:
                i = ord(word[index]) - ord('a')
                if node.array[i]:
                    return dfs(node.array[i], index+1)
                    
                
            return False

        return dfs(self.trie, 0)
