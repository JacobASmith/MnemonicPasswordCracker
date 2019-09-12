def checkHash(candidate, hashes):
    import hashlib
    m = hashlib.sha1()
    m.update(str.encode(candidate))
    newHash = m.hexdigest()
    if newHash in hashes:
        return 1
    return 0


def makeTransforms(word):
    word2char = {
        "one"       : ["1", '2'],
        "won"       : ["1", '2'],
        "first"     : ["1", '2'],
        "ones"      : ["1", '2'],
        "two"       : ["2", '3'],
        "to"        : ["2", '3'],
        "too"       : ["2"],
        "second"    : ["2"],
        "three"     : ["3"],
        "third"     : ["3"],
        "four"      : ["4"],
        "for"       : ["4"],
        "fourth"    : ["4"],
        "fore"      : ["4"],
        "forth"     : ["4"],
        "five"      : ['5'],
        "fifth"     : ['5'],
        "six"       : ["6"],
        "sics"      : ["6"],
        "sixth"     : ["6"],
        "seven"     : ["7"],
        "seventh"   : ["7"],
        "ait"       : ["8"],
        "eighth"     : ["8"],
        "ate"       : ["8"],
        "eight"     : ["8"],
        "nine"      : ["9"],
        "ninth"     : ["9"],
        "nein"      : ["9"],
        "zero"      : ["0"],
        "empty"     : ["0"],
        "none"      : ["0"],
        "nought"    : ["0"],
        "knot"      : ["0"],
        "said"      : ["\"", "'"],
        "quote"     : ["\"", "'"],
        "say"       : ["\"", "'"],
        "pound"     : ["#"],
        "hash"      : ["#"],
        "money"     : ["$"],
        "worth"     : ["$"],
        "no"        : ["!"],
        "not"       : ["!"],
        "cant"      : ["!"],
        "is"        : ["="],
        "equal"     : ["="],
        "greatest"  : [">"],
        "greater"   : [">"],
        "great"     : [">"],
        "better"    : [">"],
        "more"      : [">"],
        "less"      : ["<"],
        "lesser"    : ["<"],
        "least"     : ["<"],
        "worse"     : ["<"],
        #"are"       : ["r", 'R'],
        "art"       : ["r", "R"],
        "and"       : ["&"],
        "you"       : ["u", "U"],
        "question"  : ["?"],
        "who"       : ["?"],
        "what"      : ["?"],
        "when"      : ["?"],
        "where"     : ["?"],
        "why"       : ["?", "y", "Y"],
        "how"       : ["?"],
        "okay"      : ["k", "K"],
        "ok"        : ["k", "K"]
        #"seeing"    : ["c", "C"]
        #"eyes"      : ["i", "I", '!', '1', '|', 'l']
        #"owe"       : ["o", "O", "0"]
        #"window"    : ['#'],
        #"lattice"   : ['#']
        #"into"      : ["2"]
        #"in"        : ['n', 'N'],
        #"an"        : ['n', 'N']
        #"thee"      :"3"
        #"sign"      :"-"
        #"tzu"       :"Z"
        #"never"     :"!"
        #"january"   :"1",
        #"jan"       :"1",
        #"february"  :"2",
        #"feb"       :"2",
        #"march"     :"3",
        #"mar"       :"3",
        #"answer"    :"?"
    }
    char2char = {
            'a': ['a', 'A', '@', '4'],
            'b': ['b', 'B', '8', '6'],
            'c': ['c', 'C', '('],
            'd': ['d', 'D', ')'],
            'e': ['e', 'E', '3', '&'],
            'f': ['f', 'F'],
            'g': ['g', 'G', '6', '&', '(', '9'],
            'h': ['h', 'H', '4', '#'],
            'i': ['i', 'I', '!', '1', '|', 'l', '2'],  #1
            'j': ['j', 'J'],
            'k': ['k', 'K', 'c', 'n', 'N'],
            'l': ['l', 'L', '1', '#', '|', 'i', 'I', '2'],
            'm': ['m', 'M'],
            'n': ['n', 'N'],
            'o': ['o', 'O', '0'],
            'p': ['p', 'P', 'n', 'N'],
            'q': ['q', 'Q', '9', '0', '@'], #0
            'r': ['r', 'R'],
            's': ['s', 'S', '$', '5'], #5
            't': ['t', 'T', '7', '+'],
            'u': ['u', 'U'],
            'v': ['v', 'V'],
            'w': ['w', 'W'],
            'x': ['x', 'X', '%'],
            'y': ['y', 'Y', 'j'],
            'z': ['z', 'Z', '2'],
            '0': ['0', 'o', 'O'],
            '1': ['1', '2'],
            '2': ['2', '3'],
            '3': ['3'],
            '4': ['4', 'a', 'A'],
            '5': ['5'],
            '6': ['6'],
            '7': ['7'],
            '8': ['8'],
            '9': ['9'],
            '@': ['@', 'a']
    }
    # returns a list of letters transformed from orig
    transforms = []
    w2c = word2char.get(word.lower())
    if w2c:
        transforms.extend(w2c)
    transforms.extend(char2char.get(word[0].lower()))
    return set(transforms)

def genAndCrackPhrase(phrase, hashes):
    #print(phrase)
    cracked = []
    # all phr 8 wds
    c0 = makeTransforms(phrase[0])
    c1 = makeTransforms(phrase[1])
    c2 = makeTransforms(phrase[2])
    c3 = makeTransforms(phrase[3])
    c4 = makeTransforms(phrase[4])
    c5 = makeTransforms(phrase[5])
    c6 = makeTransforms(phrase[6])
    c7 = makeTransforms(phrase[7])
    #transforms = [makeTransforms(phrase[x]) for x in range(n)]
    for char0 in c0:
        for char1 in c1:
            for char2 in c2:
                for char3 in c3:
                    for char4 in c4:
                        for char5 in c5:
                            for char6 in c6:
                                for char7 in c7:
                                    candidate = char0 + char1 + char2 + char3 + char4 + char5 + char6 + char7
                                    #print(candidate)
                                    if checkHash(candidate, hashes) == 1:
                                        #print("Cracked pw: " + candidate)
                                        cracked.append(candidate)
    return cracked
def iterateFiles(src, hashFile):
    import string
    f = open(hashFile)
    hashes = []
    for line in f.readlines():
        hashes.append(line.strip())
    hashes = set(hashes)
    crackedHashes = []
    mnemonicSrc = open(src)
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    for line in mnemonicSrc.readlines():
        split = line.translate(str.maketrans(translator)).split()
        if len(split) >= 8:
            crackedHashes.extend(genAndCrackPhrase(split[0:8], hashes))
    return crackedHashes

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3 :
        print("Must supply input file: python3 kiddough.py [input file] [known hashes]")
    else:
        # t desc. gen lst 4 : wd => [wd 2 ltr, 1st to all trnsfrms]
        # pt : chld 2 sme lst
        # mk t || mk 8 lsts and 8 4lps
        out = iterateFiles(sys.argv[1], sys.argv[2])
        #for word in out:
        #    print(word)
        print("Total Cracked: " + str(len(out)) + " out of 134760")
