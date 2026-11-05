class PrefixTree:
    def __init__(self):
        self.array = [None] * 26
        self.end = False

    def insert(self, word: str) -> None:
        if word:
            index = ord(word[0])-ord('a')
            if self.array[index] == None:
                self.array[index] = PrefixTree()
            self.array[index].insert(word[1:])
        else:
            self.end = True
            return

    def search(self, word: str) -> bool:
        if word == "":
            return self.end

        index = ord(word[0])-ord('a')
        if self.array[index] == None:
            return False
        
        return self.array[index].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if prefix == "":
            return True
        
        index = ord(prefix[0])-ord('a')
        if self.array[index] == None:
            return False
        return self.array[index].startsWith(prefix[1:])
        