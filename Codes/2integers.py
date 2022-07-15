class Solution:
    def __init__(self,int_1, int_2):
        self.int_1 = int_1
        self.int_2 = int_2

    def sum(self):
        return self.int_1 + self.int_2 

RequiredSum = Solution(int('12'),int('5'))

print(RequiredSum.sum())