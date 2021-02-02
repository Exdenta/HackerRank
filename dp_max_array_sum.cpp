
// // https://www.hackerrank.com/challenges/max-array-sum

#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

int max(int n, int m){
    return n > m ? n : m;
}

// Complete the maxSubsetSum function below.
int maxSubsetSum(vector<int> arr) {
    arr[0] = max(0, arr[0]);
    arr[1] = max(arr[0], arr[1]);
    for(int i = 2; i < arr.size(); i++) {
        arr[i] = max(arr[i-1], arr[i] + arr[i-2]);
    }

    return arr[arr.size() - 1];
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    int res = maxSubsetSum(arr);

    fout << res << "\n";

    fout.close();

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


// #include <algorithm>
// #include <iostream>
// #include <chrono>
// #include <atomic>
// #include <vector>
// #include <ctime>

// using namespace std;

// void generateSubsets(vector<int>& arr, int sum, vector<int> &sums, int index){
    
//     // add sum to all subsets    
//     sums.push_back(sum);
    
//     for(int i = index; i < arr.size(); i++){
//         if(arr[i] > 0) {
//             // create new branch with the new element added
//             generateSubsets(arr, sum + arr[i], sums, i+2);

//             // gets rid of useless sums
//             if((arr[i + 1] < arr[i]) && (i + 1 < arr.size()))
//                 return;
//         } else {
//             // skip the negative element and go to the next one
//             continue;
//         }
//     }
//     return;
// }

// vector<int> getAllSubsets(vector<int> &arr){
//     vector<int> sums;
//     generateSubsets(arr, 0, sums, 0);
//     return sums;
// }

// // Complete the maxSubsetSum function below.
// int maxSubsetSum(vector<int>& arr) {
//     typedef std::chrono::milliseconds ms;
//     auto time1 = chrono::high_resolution_clock::now();

//     // get all subsets
//     vector<int> sums = getAllSubsets(arr);
    
//     // get all sums and compare them
//     int max_s = 0;
//     for(int sum : sums){
//         if(sum > max_s)
//             max_s = sum;
//     }

//     auto time2 = chrono::high_resolution_clock::now();
//     cout << "algorithm time: " << std::chrono::duration_cast<ms>(time2 - time1).count() << " ms." << endl;
    
//     return max_s;
// }

// int main()
// {
//     /* initialize random seed: */
//     srand(0);

//     int n = 300;
//     vector<int> arr(n);
//     for (int i = 0; i < n; i++) {
//         arr[i] = rand() % 20 - 10;
//     }

//     // cout << "input: ";
//     // for (int i = 0; i < n; i++) {
//     //     cout << arr[i] << " ";
//     // }
//     // cout << endl;
    
    
//     int res = maxSubsetSum(arr);
//     cout << "result: " << res << endl;

//     return 0;
// }
