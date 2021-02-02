
// https://www.hackerrank.com/challenges/ctci-making-anagrams

#include <bits/stdc++.h>

using namespace std;

// Complete the makeAnagram function below.
int makeAnagram(string a, string b) {
    std::unordered_map<char, int> char_freq;
    
    for(char& c: a){
        if(char_freq.find(c) == char_freq.end()) char_freq[c] = 1;
        else char_freq[c]++;
    }

    for(char& c: b){
        if(char_freq.find(c) == char_freq.end()) char_freq[c] = -1;
        else char_freq[c]--;
    }

    int sum = 0;
    std::unordered_map<char, int>::iterator it;
    for(it = char_freq.begin(); it != char_freq.end(); it++){
        sum += abs((*it).second);
    }
    return sum;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string a;
    getline(cin, a);

    string b;
    getline(cin, b);

    int res = makeAnagram(a, b);

    fout << res << "\n";

    fout.close();

    return 0;
}
