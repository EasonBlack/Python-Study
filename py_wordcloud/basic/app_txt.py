from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
from os import path
import json

d = path.dirname(__file__)
text = open(path.join(d, '../alice.txt')).read()

wc = WordCloud().generate(text)

# plt.figure(figsize=(12,4))
# plt.subplot(1,2,1)
# plt.imshow(wc)
# plt.show()

image=wc.to_image()
image.show()