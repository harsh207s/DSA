class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort by end coordinate
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        arrow_pos = points[0][1]  # shoot at end of first balloon
        
        for start, end in points[1:]:
            if start > arrow_pos:
                # Need a new arrow
                arrows += 1
                arrow_pos = end
        
        return arrows
