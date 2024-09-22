from rembg import remove
from PIL import Image
image_input = Image.open("C:\\Users\\HP\\Desktop\\BUREAU\\mes donnes\\Pictures\\BezzCover\\amzo.png")
output = remove(image_input)
output.save("C:\\Users\\HP\\Desktop\\BUREAU\\mes projets\\python fill")
#print(image_input.format)  