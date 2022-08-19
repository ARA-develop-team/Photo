import pygame
from PIL import Image
import class_text_image


def create_pix_list(pix):
    pix_list = []
    for y in range(height):
        pix_list.append([])
        for x in range(width):
            pix_list[y].append(pix[x, y])
    return pix_list


def print_image(img):
    for y in range(len(img.image_in_pix_list)):
        print('')
        for x in range(len(img.image_in_pix_list[0])):
            col = (img.image_in_pix_list[y][x][0] + img.image_in_pix_list[y][x][1] + img.image_in_pix_list[y][x][2]) / 3
            step = 256 / len(symbol_list)
            for i in range(len(symbol_list)):
                if col < (i + 1) * step:
                    print(symbol_list[i], end='')
                    break


image = Image.open('kot.jpg')
width = image.size[0]
height = image.size[1]
pix = image.load()

pix_list = create_pix_list(pix)
image = class_text_image.Image(pix_list)

symbol_list = ['─', '░', '▒', '▓', '█']  # from darker to lighter

screen_size = [700, 700]
screen_color = (0, 0, 0)
window = pygame.display.set_mode(screen_size)

window.fill(screen_color)

image.make_black_white()
image.high_contrast()

image.draw(window)

# image2 = image
# image2.decrease_extension_photo(40, 2)
#
# image2.print(symbol_list)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(screen_color)
    image.draw(window)
    pygame.display.flip()

pygame.quit()
