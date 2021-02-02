// https://www.hackerrank.com/challenges/abbr

#include <bits/stdc++.h>

using namespace std;

// Complete the abbreviation function below.
string abbreviation(string a, string b) {
    bool res = false;
    int idx_a = 0;
    for(char& cb : b) {
        // search uppercase char
        int idx = a.find_first_of(cb, idx_a);
        
        // if found nothing
        if (idx == string::npos){
            
            // search lowercase char
            idx = a.find_first_of(tolower(cb), idx_a);
            
            // if found nothing
            if (idx == string::npos){
                return "NO";
            } 
            else{
                a[idx] = toupper(a[idx]);
                idx_a = idx + 1;
            }
        }
        else{
            a[idx] = toupper(a[idx]);
            idx_a = idx + 1;
        }
    }
    
    int n = 0;
    for(char& c: a)
        if(isupper(c))
            n++;
    
    return (n == b.length())? "YES" : "NO";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string a;
        getline(cin, a);

        string b;
        getline(cin, b);

        string result = abbreviation(a, b);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
