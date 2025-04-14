# 1- 58. Length of Last Word

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s.split()[-1])
        return length
            
        # length = len(s.split().pop())
        # word = s.split()
        # return word     #output: ['Masfa', 'Nasrullah']

    
solution = Solution()
result = solution.lengthOfLastWord("Masfa Nasrullah ")

print (result)


        