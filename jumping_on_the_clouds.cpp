
// https://www.hackerrank.com/challenges/jumping-on-the-clouds

#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the jumpingOnClouds function below.
int jumpingOnClouds(vector<int> c) {
    int m = 0;
    for(int i = 0; i < c.size() - 1;){
        if(c[i+1] == 1){
            i+=2;
        } else if(i+1 < c.size() && c[i+2] == 0){
            i+=2;
        } else {
            i++;
        }
        m++;
    }
    return m;
}

int main()
{
    int n = 7;
    vector<int> c{0, 0, 1, 0, 0, 1, 0};
    int result = jumpingOnClouds(c);
    cout << result << "\n";
    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
