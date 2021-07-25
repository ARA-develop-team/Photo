import pygame
from PIL import Image


def create_pix_list(pix):
    pix_list = []
    for y in range(height):
        pix_list.append([])
        for x in range(width):
            pix_list[y].append(pix[x, y])
    return pix_list


def decrease_extension_photo(pix_list, size_x):
    remainder = len(pix_list[0]) % size_x
    for list_y in range(len(pix_list)):
        for _ in range(remainder):
            pix_list[list_y].pop()

    a = int(len(pix_list[0]) / size_x)
    b = int(a * 1.6)
    remainder = len(pix_list) % b
    print(remainder)
    for _ in range(remainder):
        pix_list.pop()

    new_pix_list = []
    number_y = 0
    for y in range(0, len(pix_list), b):
        new_pix_list.append([])
        for x in range(0, len(pix_list[0]), a):
            sum = 0
            for x1 in range(a):
                for y1 in range(b):
                    sum += pix_list[y + y1][x + x1][0]
            sum = sum / (a * b)

            new_pix_list[number_y].append((sum, sum, sum))
        number_y += 1
    return new_pix_list


def black_and_white_photo(pix_list, ):
    for y in range(height):
        for x in range(width):

            r = pix_list[y][x][0]  # узнаём значение красного цвета пикселя
            g = pix_list[y][x][1]  # зелёного
            b = pix_list[y][x][2]  # синего

            sr = (r + g + b) // 3  # среднее значение
            sr = int(sr * 1)
            if sr < 190:
                sr = 0
            else:
                sr = 255

            if sr > 255:
                sr = 255
            pix_list[y][x] = (sr, sr, sr)
    return pix_list


image = Image.open('samolet.jpg')
width = image.size[0]
height = image.size[1]

pix = image.load()

screen_size = [width, height]
screen_color = (0, 0, 0)
window = pygame.display.set_mode(screen_size)

pix_list = create_pix_list(pix)
pix_list_bw = black_and_white_photo(pix_list)
pix_list_pg = pix_list_bw
pix_list2 = decrease_extension_photo(pix_list_bw, 22)

window.fill(screen_color)
for y in range(len(pix_list2)):
    for x in range(len(pix_list2[0])):
        pygame.draw.circle(window, pix_list2[y][x], (x, y), 1, 1)

print(len(pix_list2))
print(len(pix_list2[0]))
for y in range(len(pix_list2)):
    print('')
    for x in range(len(pix_list2[0])):
        col = (pix_list2[y][x][0] + pix_list2[y][x][1] + pix_list2[y][x][2]) / 3
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
