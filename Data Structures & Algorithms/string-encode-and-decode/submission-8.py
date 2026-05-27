class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = ""
        words = ""
        for word in strs:
            lens += str(len(word)) + ","
            words += word
        return lens + "]" + words
    def decode(self, s: str) -> List[str]:
        res = []
        end_idx = s.find("]")
        lens = s[:end_idx]
        words = s[end_idx + 1:]
        while lens:
            comma_idx = lens.find(",")
            num = int(lens[:comma_idx])
            res.append(words[:num])
            words = words[num:]
            lens = lens[comma_idx + 1:]   
        return res     