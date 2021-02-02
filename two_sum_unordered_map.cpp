#include <stdexcept>
#include <iostream>
#include <vector>
#include <utility>
#include <unordered_map>

std::pair<int, int> findTwoSum(const std::vector<int>& list, int sum)
{
    // numbers from list and their indicies
    std::unordered_map<int, int> pairs;
    for(int i = 0; i < list.size(); i++){
        auto pair = pairs.find(sum-list[i]);
        if(pair != pairs.end())
            return std::make_pair(pair->second, i);
        
        pairs.insert(std::make_pair(list[i], i));
    }
    
    return std::make_pair(-1, -1);
}

#ifndef RunTests
int main()
{
    std::vector<int> list = {3, 1, 5, 7, 5, 9};
    std::pair<int, int> indices = findTwoSum(list, 10);
    std::cout << indices.first << '\n' << indices.second;
}
#endif