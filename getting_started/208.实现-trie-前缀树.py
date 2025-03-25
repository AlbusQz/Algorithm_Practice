#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        
        # value = ''
        self.next = []
        for i in range(26):
            self.next.append(None)
        self.end = False
            
            
    def s2i(self, s:str) -> int:
        
        return ord(s) - ord('a')
    
        
    def insert(self, word: str) -> None:
        
        node = self
        for s in word:
            i = self.s2i(s)
            if node.next[i] is None:
                node.next[i] = Trie()
            node = node.next[i]
        node.end = True

    def search(self, word: str) -> bool:
        
        node = self
        for s in word:
            i = self.s2i(s)
            if node.next[i] is None:
                return False
            node = node.next[i]
        if node.end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        
        node = self
        for s in prefix:
            i = self.s2i(s)
            if node.next[i] is None:
                return False
            node = node.next[i]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

