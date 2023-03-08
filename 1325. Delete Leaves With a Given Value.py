from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        columns = ['' for _ in range(max_len)]
        for word in words:
            for i, c in enumerate(word):
                columns[i] += c
            for i in range(len(word), max_len):
                columns[i] += ' '
        return [col.rstrip() for col in columns]
