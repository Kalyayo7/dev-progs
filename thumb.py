from PIL import Image



image = Image.open("monro.jpg")

red, green, blue = image.split()


red_left = red.crop((50, 0, red.width, red.height))

red_mid = red.crop((25, 0, red.width - 25, red.height))

red_spin = Image.blend(red_left, red_mid, 0.5)


blue_right = blue.crop((0, 0, blue.width - 50, blue.height))

blue_mid = blue.crop((25, 0, blue.width - 25, blue.height))

blue_spin = Image.blend(blue_right, blue_mid, 0.5)


green_spin = green.crop((25, 0, green.width - 25, green.height))


new_image = Image.merge("RGB", (red_spin, green_spin, blue_spin))


new_image.thumbnail((80, 80))
new_image.save('ava_mon.jpg')