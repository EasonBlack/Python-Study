from os import path
from PIL import Image
import numpy as np

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

text = open(path.join(d, '../alice.txt')).read()

alice_mask = np.array(Image.open(path.join(d, "../alice_mask.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords)

wc.generate(text)

image=wc.to_image()
image.show()

