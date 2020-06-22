class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        else:
            current_largest = 1
            for i in range(len(s)):
                for j in range(i+1,len(s)):
                    if len(set(s[i:j])) != j - i:
                        if len(set(s[i:j]))  > current_largest:
                            current_largest = len(set(s[i:j])) 
                        break
                    else:
                        if len(set(s[i:j+1])) > current_largest:
                            current_largest = len(set(s[i:j+1]))
                    
                    # print(current_largest)
                    result = s[i:j-1]
            return current_largest