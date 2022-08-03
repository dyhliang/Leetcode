class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        buildings_with_view = []

        for val in range(len(heights)):
            while buildings_with_view and heights[buildings_with_view[-1]] <= heights[val]:
                buildings_with_view.pop()
            buildings_with_view.append(val)
            
        return buildings_with_view
    