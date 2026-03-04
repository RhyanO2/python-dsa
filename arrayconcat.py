def getConcatenation(self, nums):
        for i in nums[:]:
          # print(i)
          nums.append(i)
        return nums

print(getConcatenation(1,[1,3,4]))