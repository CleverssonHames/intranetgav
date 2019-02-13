from PIL import Image

img  = Image.open('lojas/logix.png')

new_width = 80
new_height= 60

img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('logix.png') 
