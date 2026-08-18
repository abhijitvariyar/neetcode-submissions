class Solution:
    '''
        Algorithm -
        1. Sort the list in ascending order
        2. Iterate from index 'i' = 0
        3. For each number 'num' at i, find the target = -num.
           We need to find the two sum combinations for each number after 'num' such that this target is met.
        4. If number becomes greater than 0, then it is not possible to find any sum which will become 0, so stop the loop
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        target = 0

        for i, num in enumerate(nums):
            target = (-1)*num
            twosum = {}
            if (num > 0):
                # print("Returing triplets")
                return triplets

            if i > 0 and num == nums[i-1]:
                continue

            # print(f"target: {target}")
            twosum_list = self.twosum(nums[i+1:], target)
            # print(f"TwoSum: {twosum_list}")
            if twosum_list is not None:
                for twosums in twosum_list:
                    triplets.append([num]+twosums)

        return triplets

    def twosum(self, nums, target):
        ind = {}
        twosums = []
        # print(f"twosum() invoked")
        # print(f"nums: {nums}")
        for i, num in enumerate(nums):
            diff = target - num
            # print(f"TwoSum target: {target}\nDifference: {diff}")

            if diff in ind:
                combo = [nums[ind[diff]], nums[i]]
                if combo not in twosums:
                    twosums.append(combo)
            else:
                ind[num] = i
        # print(f"Returning twosums: {twosums}")
        return twosums