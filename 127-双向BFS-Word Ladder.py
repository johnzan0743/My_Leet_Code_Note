from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        if beginWord in word_set:
            word_set.remove(beginWord)
        
        visited = set()
        visited.add(beginWord)
        visited.add(endWord)

        begin_visited = set()
        begin_visited.add(beginWord)

        end_visited = set()
        end_visited.add(endWord)

        word_len = len(beginWord)
        step  = 1

        while begin_visited and end_visited:
            if len(begin_visited) > len(end_visited):
                begin_visited,end_visited = end_visited,begin_visited
                # 交换，这样我们就只用focus on begin_visited的了
                # 实际上是begin_visited和end_visited交替BFS
            
            next_level_visited = set()
            # 此处必须要新开辟一个set，因为循环过程中，如果直接把元素加到begin_visited里面的话，循环长度会发生变化，应当在一次循环之后统一更新begin_visited set
            # 注意：begin_visited set不是累加，而是每层分别更新！
            for word in begin_visited:
                word_list = list(word)

                for j in range(word_len):
                    origin_char = word_list[j]
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        new_word = ''.join(word_list)
                        if new_word in word_set:
                            if new_word in end_visited:
                                return step + 1
                            if new_word not in visited:
                                next_level_visited.add(new_word)
                                visited.add(new_word)
                    word_list[j] = origin_char
            begin_visited = next_level_visited
            step +=1
        return 0

