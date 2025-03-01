""" 
Jump Game 
Team: Kacie, Zedd, Dylan

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
Example 0:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index. 
"""
import math
def jump_game(nums):
    if nums.len() < 1:
        return False
    
    if idx, n in enumerate(nums):
        if idx == len(nums)-1:
            pass
        else:
            #idx plus value at index what value

    for n in nums:
        pass
    if nums[0] >= len(nums)-1:
        return True

def main():
    nums = [2,3,1,1,4]
    jump_game(nums)

if __name__ == "__main__":
    main()