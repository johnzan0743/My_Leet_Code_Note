class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        sliding_window = []
        current_length = max_length = 0
        
        for i in range(len(s)):
            if s[i] not in sliding_window:
                sliding_window.append(s[i])
                current_length +=1

            else:
                j = sliding_window.index(s[i])
                sliding_window = sliding_window[j+1:]
                #sliding_window = sliding_window[1:]
                sliding_window.append(s[i])
                current_length = len(sliding_window)
                
            max_length = max(max_length,current_length)
            
        return max_length