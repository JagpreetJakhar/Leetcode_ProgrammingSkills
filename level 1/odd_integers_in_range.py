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
""" Best Solution :
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:           # If low number is even
            return (high-low+1)//2 # Then add one and return the floor of the division
        return (high-low)//2 + 1   # ELSE return the floor of the division, and add one
        
        """
