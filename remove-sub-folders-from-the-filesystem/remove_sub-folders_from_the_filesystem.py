from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        for i in range(1, len(folder)):
            if (res[-1] + "/") in folder[i][:len(res[-1])+1]:
                continue
            res.append(folder[i])

        return res