import numpy as np
from PIL import Image

def RGB_img_show(i1, i2, i3):
    if min(i1,i2,i3)<20:
        i1+=50
        i2+=50
        i3+=50
    color = (int(np.clip(i1, 0, 255)),
             int(np.clip(i2, 0, 255)),
             int(np.clip(i3, 0, 255)))
    img = Image.new("RGB", (400, 200), color)
    img.show()
    print(f"🖼️ Displayed color patch for RGB {color}")
