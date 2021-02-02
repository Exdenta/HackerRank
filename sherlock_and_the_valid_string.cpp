// https://www.hackerrank.com/challenges/sherlock-and-valid-string

#include <bits/stdc++.h>

using namespace std;

// Complete the isValid function below.
string isValid(string s)
{

    // symbol - its frequency
    std::unordered_map<char, int> sf;
    std::string::iterator it;
    for (it = s.begin(); it != s.end(); it++)
    {
        if (sf.find(*it) == sf.end())
            sf[*it] = 1;
        else
            sf[*it]++;
    }

    int freq_1 = (*sf.begin()).second;
    int freq_2 = 0;
    std::unordered_map<char, int>::iterator sf_it;
    for (sf_it = sf.begin(); sf_it != sf.end(); sf_it++)
    {
        if ((*sf_it).second != freq_1)
        {
            if (freq_2 == 0)
                freq_2 = (*sf_it).second;
            else if ((*sf_it).second != freq_2)
                return "NO";
        }
    }

    if (freq_2 == 0)
        return "YES";

    int freq_freq_1 = 0;
    int freq_freq_2 = 0;
    for (sf_it = sf.begin(); sf_it != sf.end(); sf_it++)
    {
        if ((*sf_it).second == freq_1)
            freq_freq_1++;
        else
            freq_freq_2++;
    }

    if (freq_freq_1 == 1 && (abs(freq_1 - freq_2) == 1 | freq_1 == 1))
        return "YES";

    if (freq_freq_2 == 1 && (abs(freq_1 - freq_2) == 1 | freq_2 == 1))
        return "YES";

    std::cout << "freq_1: " << freq_1 << ", freq_freq_1: " << freq_freq_1 << std::endl;
    std::cout << "freq_2: " << freq_2 << ", freq_freq_2: " << freq_freq_2 << std::endl;

    return "NO";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s = "aaaaabc";

    string result = isValid(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
