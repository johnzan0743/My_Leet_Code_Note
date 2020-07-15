class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs or len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]
        dict1 = {}
        for i in range(len(strs)):
            temp_key = ''.join(sorted(strs[i]))
            temp_value = strs[i]
            # if temp_key in dict1:
                # dict1[temp_key].append(temp_value)
            # else:
                # dict1[temp_key] = [strs[i]]
            if temp_key not in dict1:
                dict1[temp_key] = [strs[i]]
            else:
                dict1[temp_key].append(temp_value)
        return list(dict1.values())
# 此题的要点是把每一个''.join(sorted(strs[i]))作为字典的keys，所有的变形体组成一个list,整个list作为字典的values