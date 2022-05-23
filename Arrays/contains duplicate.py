class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # for i in range(len(nums)):
        #     a=nums[i]                
        #     for j in range(i+1,len(nums)):     #iterating over other loops
        #         b=nums[j]
        #         if a==b:
        #             return True
        # else:
        #     return False   
#         this part shown time limit exceeded because of time complexity O(n^2)
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
                break
            
        else:
            return False
#           here time copmlexity is O(n logn)+O(n)
          
#     more better approach using hash set:--
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
      
#       in this space complexity O(n) and time complexity O(n)
