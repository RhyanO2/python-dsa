class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (divisor == -1) and (dividend !=1) and (dividend !=-1):
            if(dividend>0):
                return int(dividend/divisor)
            dividend+=1
        return int(dividend/divisor)