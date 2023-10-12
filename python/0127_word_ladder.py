from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Goal: Create adjacency matrix, BFS

        wordList.append(beginWord)
        adj = [[] for _ in range(len(wordList))]

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                is_adj = False
                for k in range(len(beginWord)):
                    if wordList[i][k] != wordList[j][k]:
                        if is_adj:
                            is_adj = False
                            break
                        is_adj = True
                if is_adj:
                    adj[i].append(j)
                    adj[j].append(i)
                
        depth = 1
        curr = [len(wordList) - 1]
        visited = [False for _ in range(len(wordList))]
        visited[len(wordList) - 1] = True
        while len(curr) != 0:
            next = []
            for i in curr:
                if wordList[i] == endWord:
                    return depth
                for neighbor in adj[i]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        next.append(neighbor)
            curr = next
            depth += 1
        return 0
