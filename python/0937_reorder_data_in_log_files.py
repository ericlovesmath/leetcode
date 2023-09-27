from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def log_key(log):
            ident, log = log.split(" ", 1)
            if log[0].isalpha():
                return (False, log, ident)
            return (True,)

        return sorted(logs, key=log_key)
