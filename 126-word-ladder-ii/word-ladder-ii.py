from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Step 1: BFS to build parent map
        parents = defaultdict(set)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = defaultdict(set)
            for word in level:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet and newWord != word:
                            if newWord == endWord:
                                found = True
                            if newWord not in parents:
                                next_level[newWord].add(word)
                            elif word in level:
                                next_level[newWord].add(word)
            parents.update(next_level)
            level = set(next_level.keys())
            wordSet -= level

        # Step 2: Backtrack to build all paths
        res = []
        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                backtrack(p, path + [p])

        if found:
            backtrack(endWord, [endWord])
        return res
