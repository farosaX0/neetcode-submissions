class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        w1Len = len(word1)
        w2Len = len(word2)
        i = 0
        # if length of two words are equal
        if w1Len == w2Len:
            while i < w1Len:
                answer += word1[i] + word2[i]
                i += 1
        elif w1Len > w2Len:
            while i < w2Len:
                answer += word1[i] + word2[i]
                i += 1
            answer += word1[i:]
        else:
            while i < w1Len:
                answer += word1[i] + word2[i]
                i += 1
            answer += word2[i:]

        return answer
