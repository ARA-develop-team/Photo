
class Image(object):

    def __init__(self, image_in_pix_list=None):
        self.image_in_pix_list = image_in_pix_list
        self.save = []
        self.black_white = False
        self.average_brightness = 0

    def make_black_white(self):
        for y in range(len(self.image_in_pix_list)):
            for x in range(len(self.image_in_pix_list[0])):

                r = self.image_in_pix_list[y][x][0]  # узнаём значение красного цвета пикселя
                g = self.image_in_pix_list[y][x][1]  # зелёного
                b = self.image_in_pix_list[y][x][2]  # синего

                sr = (r + g + b) // 3  # среднее значение
                self.image_in_pix_list[y][x] = (sr, sr, sr)

    def high_contrast(self):
        self.average_brightness = self.get_average_brightness()
        sr = 0
        for y in range(len(self.image_in_pix_list)):
            for x in range(len(self.image_in_pix_list[0])):
                if sr < self.average_brightness:
                    sr = 0
                else:
                    sr = 255
                self.image_in_pix_list[y][x] = (sr, sr, sr)

    def get_average_brightness(self):
        brightness = 0
        for y in range(len(self.image_in_pix_list)):
            for x in range(len(self.image_in_pix_list[0])):

                r = self.image_in_pix_list[y][x][0]
                g = self.image_in_pix_list[y][x][1]
                b = self.image_in_pix_list[y][x][2]

                sr = (r + g + b) // 3
                brightness += sr

        return brightness / len(self.image_in_pix_list) + len(self.image_in_pix_list[0])

    def decrease_extension_photo(self, size_x, compression):
        # compression: 1 - без сжатия; >1 - с сжатием по y; <1 - с разширением по y

        remainder = len(self.image_in_pix_list[0]) % size_x  # остаток
        for list_y in range(len(self.image_in_pix_list)):
            for _ in range(remainder):
                self.image_in_pix_list[list_y].pop()  # удаление лишних рядов пикселей для подальшого деления справа

        a = int(len(self.image_in_pix_list[0]) / size_x)  # шаг с которым будут обэдинятся пиксели по x
        b = int(a * compression)  # шаг с которым будут обэдинятся пиксели по y

        remainder = len(self.image_in_pix_list) % b  # остаток
        print(remainder)
        for _ in range(remainder):
            self.image_in_pix_list.pop()  # удаление лишних рядов пикселей для подальшого деления снизу

        new_pix_list = []
        number_y = 0

        # объединение пикселей
        for y in range(0, len(self.image_in_pix_list), b):
            new_pix_list.append([])
            for x in range(0, len(self.image_in_pix_list[0]), a):
                sum_r = 0  # сума r в rgb всех объединение пикселей
                sum_g = 0  # сума g в rgb всех объединение пикселей
                sum_b = 0  # сума b в rgb всех объединение пикселей
                for x1 in range(a):
                    for y1 in range(b):
                        sum_r += self.image_in_pix_list[y + y1][x + x1][0]
                        sum_g += self.image_in_pix_list[y + y1][x + x1][1]
                        sum_b += self.image_in_pix_list[y + y1][x + x1][2]
                # среднее значение
                sum_r = sum_r / (a * b)
                sum_g = sum_g / (a * b)
                sum_b = sum_b / (a * b)

                new_pix_list[number_y].append((sum_r, sum_g, sum_b))  # добавление сжатого пикселя
            number_y += 1

        self.image_in_pix_list = new_pix_list

    def save(self):
        self.save.append(self.image_in_pix_list)

    def load(self, save_number):
        self.image_in_pix_list = self.save[save_number]
