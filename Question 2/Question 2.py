import time
from PIL import Image
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
image_path = 'Chapter1.png'
img = Image.open(image_path)
pixels = img.load()
for i in range(img.width):
    for j in range(img.height):
        r, g, b = pixels[i, j]
        pixels[i, j] = (r + generated_number, g + generated_number, b + generated_number)
new_image_path = 'Chapter1out.png'
img.save(new_image_path)
red_sum = sum(pixels[i, j][0] for i in range(img.width) for j in range(img.height))
print("Sum of red values:", red_sum)
