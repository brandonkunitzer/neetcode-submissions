class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ",/,.".join(strs)
        if len(strs) == 1 and strs[0] == "":
            return ",/,."
        return res
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        if s == ",/,.":
            return [""]
        return s.split(",/,.")
