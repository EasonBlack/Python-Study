

import requests
from PIL import Image

branchList =  [3]

for b in branchList: 
  r = requests.get(f"xxxx")
  data = r.json()
  url = data["data"]
  img = Image.open(requests.get(url, stream = True).raw)
  img.save(f'{b}.jpg')
