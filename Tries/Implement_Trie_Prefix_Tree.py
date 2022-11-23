class TrieNode:
    def __init__(self):
        self.isEnd = False #Initialize isEnd to be False
        self.children = [None]*26 #Initialize children with None for length of 26
class Trie(object):

    def __init__(self):
        self.root = TrieNode() #Initializing a TrieNode as root
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root #Changing root to curr
        for char in word:
            key = ord(char) - ord('a') #Finding the key by subtracting the Ascii value of char with Ascii value of 'a'
            if curr.children[key]==None: #If curr.children[key] is equal to None
                curr.children[key]= TrieNode() #Then initialize TrieNode to that children
            curr = curr.children[key] #Change curr as curr.children[key]
        curr.isEnd = True #Change curr.isEnd to be True at the end of insertion

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root #Changing root to curr
        for char in word:   #For every char in word
            key = ord(char)-ord('a') #Finding the key by subtracting the Ascii value of char with Ascii value of 'a'            
            if curr.children[key]==None: #If curr.children[key] is equal to None return False
                return False
            curr = curr.children[key] #Change curr as curr.children
        return curr.isEnd #Return curr.isEnd

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root #Changing root to curr
        for char in prefix: #For every char in prefix
            key = ord(char) - ord('a')#Finding the key by subtracting the Ascii value of char with Ascii value of 'a'
            if curr.children[key]==None:#If curr.children[key] is equal to None return False
                return False
            curr = curr.children[key] #Change curr as curr.children
        return True #Return True if it start with that prefix
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)