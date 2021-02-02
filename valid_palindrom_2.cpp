https://leetcode.com/problems/valid-palindrome-ii/


class Solution {
public:
    bool validPalindrome(string s) {
        
        string::iterator it1 = s.begin();
        string::iterator it2 = s.end() - 1;
        bool flag1 = false; // try deleting it1 symbol
        bool flag2 = false; // try deleting it2 symbol
        
        string::iterator old_it1;
        string::iterator old_it2;
        char old_symb;
        
        while(it1 != s.end())
        {
            if(isalpha(*it1) | isdigit(*it1))
            {
                if(isalpha(*it2) | isdigit(*it2))
                {
                    if(tolower(*it1) != tolower(*it2))
                    {
                        if(flag2)
                        {
                            return false;
                        }
                        else if(flag1)   
                        {
                            *old_it1 = old_symb;
                            it1 = old_it1;
                            it2 = old_it2;
                            *it2 = '!';
                            it2--;
                            flag2 = true;
                        }
                        else
                        {
                            old_symb = *it1;
                            old_it1 = it1;
                            old_it2 = it2;
                            
                            *it1 = '!';
                            it1++;
                            flag1 = true;
                        }
                    }
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
