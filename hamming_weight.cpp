
https://leetcode.com/problems/number-of-1-bits/

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int hamming_weight = 0;
        
        // 2^31 - max uint32
        int weight = 0;
        for(int i = 0; i < 32; i++){
            hamming_weight += n & 1;
            n = n >> 1;
        }
        
        return hamming_weight;
    }
};