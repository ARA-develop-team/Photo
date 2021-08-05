
class Image(object):

    def __init__(self, image_in_pix_list=None):
        self.image_in_pix_list = image_in_pix_list
        self.save = []
        self.black_white = False

    def black_white(self):
        for y in range(len(self.image_in_pix_list)):
            for x in range(len(self.image_in_pix_list[0])):

                r = self.image_in_pix_list[y][x][0]  # узнаём значение красного цвета пикселя
                g = self.image_in_pix_list[y][x][1]  # зелёного
                b = self.image_in_pix_list[y][x][2]  # синего

                sr = (r + g + b) // 3  # среднее значение
                self.image_in_pix_list[y][x] = (sr, sr, sr)

    def high_contrast(self):
        sr = 0
        for y in range(len(self.image_in_pix_list)):
            for x in range(len(self.image_in_pix_list[0])):
                if sr < 190:
                    sr = 0
                else:
                    sr = 255
                self.image_in_pix_list[y][x] = (sr, sr, sr)

    def average_brightness(self):



def save(self):
        self.save.append(self.image_in_pix_list)

    def load(self, save_number):
        self.image_in_pix_list = self.save[save_number]
