class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # nums = [2, 2, ] => return True
        # nums = [1, 2, ] => return False
        # ways to remember item if it exists: set (to track unique items), list ( slower for checking if item exist), dict: more complex
        # To solve: 
        #   1. Create Empty set for Unique numbers
        #   2. look at each num in the arry
        #   3. check if number is seen or not
        #   4. if yes = True, else=False
        #   5. if loop is finished without Finding Duplicates=False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
           
        return False

# Time Complexity: O(n) => look at each number once
# Space Complexity: o(n) => worst case = store all numbers
