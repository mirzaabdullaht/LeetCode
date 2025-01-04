class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hash_set = {}

        for i in range(len(s)):
            if s[i] not in hash_set:
                hash_set[s[i]] = []  # Initialize the list if the key doesn't exist
            hash_set[s[i]].append(i)  # Append the index to the list

        
        subset_count = 0
        
        for i in hash_set:
            if len(hash_set[i]) == len(s):
                subset_count = 1
                break
            
            left, right = (hash_set[i][0], hash_set[i][-1])
            subset_count += len(set(s[left + 1: right]))

        return subset_count