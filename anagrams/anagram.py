# Given a word, return all the anagrams of that word in the English language i.e: cinema - iceman or silent - listen

# Load my word list

f= open('words.txt', 'r')
words = f.read().split("\n")
words = [w.lower() for w in words]
f.close()

#Preprocess my word list into an anagram list with the signature as key

w = list(word)
w.sort()
signature = "".join(w)

anagrams = {}

# GENERATE ALL SETS OF ANAGRAMS
for word in words:
    # convert list to string
    signature = "".join(sorted(word.lower()))
    if signature not in anagrams:
        anagrams[signature] = []
    anagrams[signature].append(word)


def anagrams(word):
    signature = "".join(sorted(word.lower()))
    if signature not in anagrams:
      return []
    else:
      return anagrams[signature]