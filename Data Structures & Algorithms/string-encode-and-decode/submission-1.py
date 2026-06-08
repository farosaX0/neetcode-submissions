class Solution:

    def encode(self, arr: list) -> str:
        # new empty list contains new strings
        # each string is the len(string) + # + original string
        # join them using the join depending on the matched above
        result = []
        for string in arr:
            result.append(f"{4 * len(string)}#")
            result.append(string)
        return "".join(result)

    def decode(self, string: str):
        # ex: input = 5#Hello5#world
        result = []
        i = 0
        while i < len(string):
            j = i
            while string[j] != "#":
                j += 1
            # input = 5#Hello5#world
            # make i stands at the index of "H" and j at the index of the next word length
            length = int(string[i:j]) // 4 # j is exclusive, so the extracted will be 5 -> convert to int
            # i will be after current j, increment j by 1 and make it the value of i 
            i = j + 1
            # j will be after the len of the word, then i + length = j
            j = i + length
            result.append(string[i:j])
            i = j
        return result