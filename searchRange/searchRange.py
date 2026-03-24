class Solution(object):
    def searchRange(self, nums, target):
        
        def findLeft():
            left, right = 0, len(nums) - 1
            res = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    res = mid
                    right = mid - 1  # keep searching LEFT
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return res
        
        def findRight():
            left, right = 0, len(nums) - 1
            res = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    res = mid
                    left = mid + 1  # keep searching RIGHT
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return res
        
        return [findLeft(), findRight()]
