from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import os
import json

f = open('../word.json','r')
content = json.loads(f.read())

wc = WordCloud().generate_from_frequencies(content)

# plt.figure(figsize=(12,4))
# plt.subplot(1,2,1)
# plt.imshow(wc)
# plt.show()

image=wc.to_image()
image.show()