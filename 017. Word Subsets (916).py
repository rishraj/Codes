def wordSubsets(words1: list[str], words2: list[str]) -> list[str]:
    # combine all words2 list in a single dict; but think about how this should be done
    # for the next time, reduce size of dict d; don't need to have all alphabets as keys (see notes)
    
    res = []
    d = {chr(key): 0 for key in range(ord('a'), ord('z') + 1)}
    for w2 in words2:
        w2_dict = {}
        for ch in w2:
            w2_dict[ch] = w2_dict.get(ch, 0) + 1
        for key in d:
            if key in w2_dict:
                d[key] = max(d[key], w2_dict[key])
    for w1 in words1:
        d1, flag = {}, 0
        for ch in w1:
            d1[ch] = d1.get(ch, 0) + 1
        for key in d:
            if (d[key] > 0) and (key not in d1 or d1[key] < d[key]):
                flag = 1
                break
        if not flag:
            res.append(w1)
    return res

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["lo","eo"]
print(wordSubsets(words1, words2))
