"""
3453. Separate Squares I
"""

class Solution:
    def separateSquares(self, squares) -> float:
        total_area = sum(l*l for _,_,l in squares)
        half = total_area/2

        low = min(y for _,y,_ in squares)
        high = max(y+l for _,y,l in squares)

        def area_under(Y):
            area = 0.0
            for _,y,l in squares:
                if y<Y<y+l:
                    area+=l*(Y-y) 
                elif Y>=y+l:
                    area+=l*l
                elif Y<=y:
                    area+=0
                    
            return area
        
        for _ in range(60):
            mid = (high+low)/2
            if area_under(mid)<half:
                low = mid
            else:
                high = mid
        return mid


print(Solution().separateSquares([[0,0,1],[2,2,1]])) # == 1.
# assert Solution().separateSquares([[0,0,1],[2,0,1]]) == 1.0
# assert Solution().separateSquares([[0,0,1],[3,0,1]]) == 2.0
# assert Solution().separateSquares([[0,0,1],[0,3,1]]) == 2.0
print(Solution().separateSquares([[0,0,2],[1,1,1]])) # == 1.167