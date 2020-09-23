import numpy as np
from PIL import Image, ImageDraw, ImageFont

def ascii_art(file):
    im=Image.open(file)
    im=im.convert("L")

    sample_rate=0.15
    # new_im_size=[int(x*sample_rate) for x in im.size]
    font = ImageFont.load_default()
    aspect_ratio = font.getsize("x")[0] / font.getsize("x")[1]
    new_im_size = np.array(
        [im.size[0] * sample_rate, im.size[1] * sample_rate * aspect_ratio]
    ).astype(int)

    im=im.resize(new_im_size)

    im=np.array(im)

    symbols=np.array(list(" .-vM"))

    im=(im-im.min())/(im.max()-im.min())*(symbols.size-1)

    ascii=symbols[im.astype(int)]
    lines="\n".join(("".join(r) for r in ascii))
    print(lines)

    fh = open('ascii.txt', 'w', encoding='utf-8')
    fh.write(lines)
    fh.close()

if __name__=="__main__":
    ascii_art("D:\Pic_for_this\juren.png")
