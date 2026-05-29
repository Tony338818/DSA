"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

def groupAnagrams(strs : str):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    
    hashmap = {}
    
    for s in strs:
        val = "".join(sorted(s))
        if val in hashmap: 
            hashmap[val].append(s)
        else : 
            hashmap[val] = [s]
        
    
    return hashmap.values()
    
strs = ["eat","tea","tan","ate","nat","bat"]
result = groupAnagrams(strs)
print(result)
