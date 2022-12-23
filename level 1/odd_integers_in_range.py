class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        spread = ((high-low) +1)
        if low % 2 == 1:
            count+=1
        if spread % 2 == 0:
            return spread//2

        else:
            spread = (high - (low+1)) + 1
            count += spread//2
            return count 
