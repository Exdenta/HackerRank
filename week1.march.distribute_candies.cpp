#include <vector>
#include <algorithm>

// https: //leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3657/

// Alice has n candies, where the ith candy is of type candyType[i].
// Alice noticed that she started to gain weight, so she visited a doctor.
// The doctor advised Alice to only eat n / 2 of the candies she has (n is always even).
// Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.
// Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

// Example 1:
// Input: candyType = [1,1,2,2,3,3]
// Output: 3
// Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

// Example 2:
// Input: candyType = [1,1,2,3]
// Output: 2
// Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.

// Example 3:
// Input: candyType = [6,6,6,6]
// Output: 1
// Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.

// Constraints:
// n == candyType.length
// 2 <= n <= 104
// n is even.
// -105 <= candyType[i] <= 105

// ____________
// beats 98.79%
class Solution
{
public:
    int distributeCandies(std::vector<int> &candyType)
    {
        std::sort(candyType.begin(), candyType.end()); // O(N * logN)
        std::vector<int>::const_iterator startIt = candyType.begin();
        std::vector<int>::const_iterator endIt = candyType.begin();

        int i = 1;
        for (; endIt != candyType.end(); ++endIt) // O(N)
        {
            if (*startIt != *endIt)
            {
                ++i;
                startIt = endIt;
            }
        }

        return std::min(i, (int)(candyType.size() / 2));
    }
};

//
// SET MISMATCH
// https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658/

// You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
// one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
// You are given an integer array nums representing the data status of this set after the error.
// Find the number that occurs twice and the number that is missing and return them in the form of an array.

// Example 1:
// Input: nums = [1,2,2,4]
// Output: [2,3]

// Example 2:
// Input: nums = [1,1]
// Output: [1,2]

// Constraints:
// 2 <= nums.length <= 104
// 1 <= nums[i] <= 104

// __________________
// beats 73% - 95.75%
class Solution
{
public:
    std::vector<int> findErrorNums(std::vector<int> &nums)
    {
        std::sort(nums.begin(), nums.end());

        // [duplicated, lost]
        std::vector<int> result(2);

        std::vector<int>::iterator startIt = nums.begin();
        std::vector<int>::iterator endIt = nums.begin() + 1;

        // ------- find duplicated ------- //
        for (; endIt != nums.end(); ++startIt, ++endIt)
        {
            // if duplicated
            if (*startIt == *endIt)
            {
                result[0] = *startIt;

                // if first duplicated is not in order
                // => lost is passed
                if (*startIt != (startIt - nums.begin()) + 1)
                {
                    startIt = nums.begin();

                    // if lost is in the first position --- <corner case>
                    if (*startIt != 1)
                    {
                        result[1] = 1;
                        return result;
                    }
                }
                // if second duplicated is not in order
                // => lost is not yet passed
                else
                {
                    startIt = endIt;
                    endIt = nums.end();
                }
                break;
            }
        }

        // ------- find lost ------- //

        --endIt;
        bool atLeastOne = false;
        for (; startIt != endIt; ++startIt)
        {
            // if num[i] != num[i+1]
            if (*startIt + 1 != *(startIt + 1))
            {
                result[1] = *startIt + 1;
                atLeastOne = true;
                break;
            }
        }

        // if get to the end and didn't find lost --- <corner case>
        if (!atLeastOne)
            result[1] = *endIt + 1;

        return result;
    }
};

// _______________
// better solution
class Solution
{
public: 
    std::vector<int> findErrorNums(std::vector<int> &nums)
    {
        std::vector sort(nums.size() + 1, 0);
        int count = nums.size();
        int repetition = 0;
        int loss = 0;
        for (int i = 0; i < count; i++)
        {
            if (sort[nums[i]] == 0)
            {
                sort[nums[i]] = nums[i];
            }
            else
            {
                repetition = nums[i];
            }
        }
        for (int i = 1; i < count + 1; i++)
        {
            if (sort[i] == 0)
            {
                loss = i;
                break;
            }
        }
        std::vector res{repetition, loss};
        return res;
    }
};