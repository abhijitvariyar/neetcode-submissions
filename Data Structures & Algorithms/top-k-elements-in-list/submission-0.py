class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq, ranking = {}, {}
        max_freq = 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            num_freq = freq[num]

            if num_freq not in ranking:
                ranking[num_freq] = set()
                max_freq += 1

            prev_key = num_freq-1
            curr_key = num_freq
            print(f"max_freq: {max_freq}")
            print(f"prev_key: {prev_key}")
            print(f"curr_key: {curr_key}")
            
            if num_freq > 1:
                ranking[num_freq-1].remove(num)
                ranking[num_freq].add(num)
            
            else:
                ranking[num_freq].add(num)

        print(ranking)
        res = []
        while k > 0:
            res += ranking[max_freq]
            k -= len(ranking[max_freq])
            max_freq -= 1
            
        return res