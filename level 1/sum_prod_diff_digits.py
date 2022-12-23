class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        products, sums = 0,0
        tmp = []
        while n >0:
            tmp.append(n%10)
            n = n //10
        sums = sum(tmp)
        product = tmp[0]
        for i in tmp[1:]:
            product *= i
        return product - sums
