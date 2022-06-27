import sys
from PIL import Image

# creates a new empty image
big_img = Image.new('RGB', (33*24,33*24))

for i in range(1, 24*24):
    small_img = "output/" + str(i) + ".png"
    data = Image.open(small_img)
    big_img.paste(data, (33*(i%24), 33*(i//24)))

big_img.save('sol.png')

# 404CTF{M4n1PuL4T10N_d'1M4g3S_F4c1L3_n0N?}
