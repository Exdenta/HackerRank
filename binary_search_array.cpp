#include <vector>
#include <stdexcept>
#include <iostream>

int countNumbers(const std::vector<int>& sortedVector, int lessThan)
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
    std::vector<int> v { 4, 10, 11, 12 };
    std::cout << countNumbers(v, 4);
}
#endif