class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_pre = []
        if strs and len(strs) > 0:
            strs.sort()
            first, last = strs[0], strs[-1]
            for i in range(len(first)):
                if first[i] == last[i]:
                    longest_pre.append(last[i])
                else:
                    return "".join(longest_pre)
        return "".join(longest_pre)