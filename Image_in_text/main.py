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


image = Image.open('kot.jpg')
width = image.size[0]
height = image.size[1]
pix = image.load()

pix_list = create_pix_list(pix)
image = class_text_image.Image(pix_list)

screen_size = [700, 700]
screen_color = (0, 0, 0)
window = pygame.display.set_mode(screen_size)

window.fill(screen_color)

image.make_black_white()
image.high_contrast()

for y in range(len(image.image_in_pix_list)):
    for x in range(len(image.image_in_pix_list[0])):
        pygame.draw.circle(window, image.image_in_pix_list[y][x], (x, y), 1, 1)

image.decrease_extension_photo(40, 2)

for y in range(len(image.image_in_pix_list)):
    print('')
    for x in range(len(image.image_in_pix_list[0])):
        col = (image.image_in_pix_list[y][x][0] + image.image_in_pix_list[y][x][1] + image.image_in_pix_list[y][x][2]) / 3
        if col < 51:
            print('─', end='')
        elif col < 102:
            print('░', end='')
        elif col < 153:
            print('▒', end='')
        elif col < 204:
            print('▓', end='')
        else:
            print('█', end='')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
