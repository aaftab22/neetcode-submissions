class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_item = min(strs, key=len)
        prefix = ""
        for i in range(0, len(smallest_item)):
            for j in range(0, len(strs)):
                if smallest_item[i] != strs[j][i]:
                    return prefix
            prefix += smallest_item[i]
        return prefix



        

