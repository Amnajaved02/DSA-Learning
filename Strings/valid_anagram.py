''' 
    Definition of Anagram: An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
    Link to leetcode: https://leetcode.com/problems/valid-anagram/

    Problem Statement: 
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

    Example 2:
    Input: s = "rat", t = "car"
    Output: false

    Solving Approach:
    1. Hashmaps:
        Iterate on strings keep frequency count in hashmap for each string
    2. Sort the strings and compare  
    3. Using counter from collections  
'''

# from collections import Counter <- to be used in approach 3

class Solution(object):

    # Solution 1 
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        freq_s = {}
        freq_t = {}

        for i in range(0, len(s)):
            if s[i] in freq_s:
                freq_s[s[i]] += 1
            else:
                freq_s[s[i]] = 1


            if t[i] in freq_t:
                freq_t[t[i]] += 1
            else:
                freq_t[t[i]] = 1    

        return freq_s == freq_t
    
    # Solution 2
    # def isAnagram(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     return sorted(s) == sorted(t)

    # Solution 3 
    # def isAnagram(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     return Counter(s) == Counter(t)

    """
    | Solution            | Time Complexity | Space Complexity |
    | ------------------- | --------------- | ---------------- |
    | **1. Manual Dicts** | **O(n)**        | **O(k)**         |
    | **2. Sorting**      | **O(n log n)**  | **O(n)**         |
    | **3. Counter**      | **O(n)**        | **O(k)**         |
    """