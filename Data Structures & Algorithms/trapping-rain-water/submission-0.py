class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        water_trapped = 0

        left = 0
        right = len(height) - 1

        leftTallest = height[left]
        rightTallest = height[right]

        while left < right:
            if leftTallest < rightTallest:
                left += 1
                leftTallest = max(leftTallest, height[left])
                water_trapped += leftTallest - height[left]
            else:
                right -= 1
                rightTallest = max(rightTallest, height[right])
                water_trapped += rightTallest - height[right]

        return water_trapped

            

            

            


        