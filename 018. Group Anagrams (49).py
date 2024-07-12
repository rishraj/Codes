def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # instead of sorting, could've used a list of 26 size to indicate frequency of that character
    # time of that would've been len(strs) * max_len(str)
    # time of below code is len(strs) * (max_len(str) * log(max_len(str))) coz of sorting
    
    d = {}
    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s in d:
            d[sorted_s].append(s)
        else:
            d[sorted_s] = [s]
            
    return [x for x in d.values()]

    
    
    
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))