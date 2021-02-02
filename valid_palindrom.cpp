
// https://leetcode.com/problems/valid-palindrome/

class Solution {
public:
    bool isPalindrome(string s) {
        
        string::iterator it1 = s.begin();
        string::iterator it2 = s.end() - 1; 
        
        while(it1 != s.end())
        {
            if(isalpha(*it1) | isdigit(*it1))
            {
                if(isalpha(*it2) | isdigit(*it2))
                {
                    if(tolower(*it1) != tolower(*it2)) return false;
                    it1++;
                    it2--;
                }
                else
                {
                    it2--;
                    continue;
                }
            }
            else 
            {
                it1++;
                continue;
            }
        }
        return true;
    }
};