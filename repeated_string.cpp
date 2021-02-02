
// https://www.hackerrank.com/challenges/repeated-string

#include <bits/stdc++.h>

using namespace std;

// Complete the repeatedString function below.
long repeatedString(string s, long n) {
    long result = 0;
    int l = 0;
    for(char c : s)
        if(c == 'a')
            l++;
    
    long long b = n / s.length();
    result += b * l;
    
    int res = n % s.length();
    for(int i = 0; i < res; i++)
        if(s[i] == 'a')
            result++;
    
    return result;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    long n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    long result = repeatedString(s, n);

    fout << result << "\n";

    fout.close();

    return 0;
}
