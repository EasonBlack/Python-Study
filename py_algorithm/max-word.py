import operator

a = ['aa', 'b', 'aa','c','d', 'e', 'f','f', 'd', 'e', 'f']
dictWords = {}
for i in range(len(a)):
  dictWords[a[i]] = (dictWords.get(a[i]) or 0) + 1

maxWord = max(dictWords.items(), key=lambda value: value[1])
print maxWord