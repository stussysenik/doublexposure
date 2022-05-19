from PIL import Image, ImageChops
import os
import random
import pprint
import time
pp = pprint.PrettyPrinter(indent=4)

def random_order(folder):
  return random.shuffle(folder)

def check_image(string):
  return True if string.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')) else False

def check_difference(pathA, pathB):
  img = ImageChops.difference(Image.open(pathA),Image.open(pathB))
  return img.show()

#return smaller value out of the tuples
def compare_tuples(tup1, tup2):
  return tup1 if tup1 < tup2 else tup2

folderA = [f for f in os.listdir('./A')]
folderB = [f for f in os.listdir('./B')]
random_order(folderA)
random_order(folderB)

start = time.time()
print("hello")

for i in range(len(folderA)):
  pathA = './A/' + folderA[i]
  pathB = './B/' + folderB[i]
  if check_image(pathA) and check_image(pathB):
    imgA = Image.open(pathA)
    imgB = Image.open(pathB)
    smaller = compare_tuples(imgA.size, imgB.size)
    # print(f"sizeA: {imgA.size} vs sizeB: {imgB.size} = {compare_tuples(imgA.size, imgB.size)}")
    while True:
      try:
        final = Image.blend(imgA,imgB,alpha=0.5)
        output_path = './Output5/' + str(i) + '.jpg'
        final.save(output_path, "JPEG")
        # print(f"Correct Combination: {pathA} | {pathB}.")
      except ValueError:
        # print(f"Bad Combination: {pathA} | {pathB}.")
        if imgA.size == smaller:
          # print(f"run: {i}")
          # print(f"Resized: imgA {imgA.size} < imgB {imgB.size}")
          imgB = imgB.resize(smaller)
          # print()
        else:
          # print(f"run: {i}")
          # print(f"Resized: imgA {imgA.size} > imgB {imgB.size}")
          imgA = imgA.resize(smaller)
          # print()
        continue
      break
  else:
      print(f"Incorrect Filename: {pathA} | {pathB}.")

end = time.time()
print(end - start)


# load images:
# 1)has to be the same count
# 2)same width
# 3)iterate through folder
# check image size
# time estimate
