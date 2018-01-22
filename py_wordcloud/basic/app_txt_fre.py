from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
from os import path
import json
import re

d = path.dirname(__file__)
text = open(path.join(d, '../alice.txt')).read()
text1 = re.split(r'[\n.()!, ""/]', text)
# delete some empty string
text2 = [x for x in text1 if len(x) > 0]
wd = {}
stopwords = [
    u'and', u'the', u'she',u'said', u'it',u'was',u'of', u'to', u'a',u'you', 
    u'is', u'are', u'in', u'as', u'new', u'for', u'use', u'that', u'I', u'be', u'at', u'on']
for w in text2:
    if w in stopwords:
        continue
    else:
        str(w)
        if w not in wd:
            wd[w] = 1
        else:
            wd[w] += 1

wc = WordCloud().generate_from_frequencies(wd)

# plt.figure(figsize=(12,4))
# plt.subplot(1,2,1)
# plt.imshow(wc)
# plt.show()

image=wc.to_image()
image.show()