/*
 * @lc app=leetcode.cn id=208 lang=cpp
 *
 * [208] 实现 Trie (前缀树)
 */

// @lc code=start
class Trie {
public:
    Trie() {
        next = new Trie*[26];
        for(int i = 0;i<26;i++)
        {
            next[i] = nullptr;
        }
        end = false;
    }
    
    int s2i(char c)
    {
        return int(c) - int('a');
    }

    void insert(string word) {
        
        Trie *node = this;
        int n = word.size();
        for(int i = 0;i<n;i++)
        {
            char c = word[i];
            int j = this->s2i(c);
            if(!node->next[j])
            {
                node->next[j] = new Trie();
            }
            node = node->next[j];
        }
        node->end = true;

    }
    
    bool search(string word) {

        Trie *node = this;
        int n = word.size();
        for(int i = 0;i<n;i++)
        {
            char c = word[i];
            int j = this->s2i(c);
            if(node->next[j])
            {
                node = node->next[j];
            }
            else
            {
                return false;
            }
        }
        if(node->end)
        {
            return true;
        }
        else
        {
            return false;
        }
        
    }
    
    bool startsWith(string prefix) {
        
        Trie *node = this;
        int n = prefix.size();
        for(int i = 0;i<n;i++)
        {
            char c = prefix[i];
            int j = this->s2i(c);
            if(node->next[j])
            {
                node = node->next[j];
            }
            else
            {
                return false;
            }
        }
        return true;
        
    }

private:
    Trie **next;
    bool end;
    bool flags[26];
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
// @lc code=end

