import os
import random

images =[]
for fname in os.listdir("image"):
    image = os.path.join("image",fname)
    if os.path.isfile(image):
        images.append(image)

print(random.choice(images))