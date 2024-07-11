def replaceWords(dictionary: list[str], sentence: str) -> str:
    # also could've been done using trie, but don't know how to at this point.. (maybe later)
    d = set(dictionary)
    res = []
    wrd_list = sentence.split()
    for wrd in wrd_list:
        tmp, flag = '', 0
        for ch in wrd:
            tmp += ch
            if tmp in d:
                res.append(tmp)
                flag = 1
                break
        if not flag:
            res.append(wrd)
    return " ".join(res)

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(replaceWords(dictionary, sentence))