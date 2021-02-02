#include <vector>
#include <stdexcept>
#include <iostream>

// Implement function countNumbers that accepts a sorted vector of unique integers and, efficiently with respect to time used, 
// counts the number of vector elements that are less than the parameter lessThan.
// For example, for vector v containing { 1, 3, 5, 7 }, countNumbers(v, 4) should return 2 because there are two vector elements less than 4.

int search(const std::vector<int>& sortedVector, int lessThan)
{
    if(sortedVector.size() == 0) return 0;
    
    int start_idx = 0;
    int end_idx = sortedVector.size();
    
    while(end_idx - start_idx > 1){
        int idx = (end_idx + start_idx) / 2;
        int value = sortedVector[idx];
        if (value < lessThan){
            start_idx = idx;
        } else if (value >= lessThan) {
            end_idx = idx;
        }
    }
    
    if(sortedVector[start_idx] >= lessThan) return 0;
    
    
    return end_idx;
}

#ifndef RunTests
int main()
{
    std::vector<int> v { 1, 3, 5, 7 };
    std::cout << search(v, 4);
}
#endif