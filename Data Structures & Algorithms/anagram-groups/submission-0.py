from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        ans_dict = defaultdict(list)
        for string in strs:
            letters = [0] * 26
            for char in string:
                index = ord(char) - ord("a")
                letters[index] += 1
            tupled_letters = tuple(letters)
            ans_dict[tupled_letters].append(string)
        return list(ans_dict.values())