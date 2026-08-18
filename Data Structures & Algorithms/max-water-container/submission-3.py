class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_ptr, r_ptr = 0, len(heights)-1
        l_wall, r_wall = heights[l_ptr], heights[r_ptr]

        max_area = (r_ptr - l_ptr) * min(l_wall, r_wall)

        counter = 0
        while l_ptr < r_ptr:
            # counter += 1
            # if counter == 100:
            #     break

            l_ptr = l_ptr+1 if l_wall <= r_wall else l_ptr
            r_ptr = r_ptr-1 if r_wall <= l_wall else r_ptr

            # print(f"New left_ptr: {l_ptr}")
            # print(f"New right_ptr: {r_ptr}")

            l_wall, r_wall = heights[l_ptr], heights[r_ptr]

            area = (r_ptr - l_ptr) * min(l_wall, r_wall)

            max_area = area if area > max_area else max_area

        return max_area