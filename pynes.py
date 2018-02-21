import pygame


_colors = { '0x00': (120, 128, 131, 255),
            '0x01': (1, 0, 252, 255),
            '0x02': (0, 0, 191, 255),
            '0x03': (62, 40, 199, 255),
            '0x04': (143, 2, 142, 255),
            '0x05': (174, 0, 44, 255),
            '0x06': (171, 17, 3, 255),
            '0x07': (143, 22,1, 255),
            '0x08': (80, 48, 1, 255),
            '0x09': (0, 123, 1, 255),
            '0x0A': (0, 105, 1, 255),
            '0x0B': (0, 89, 2, 255),
            '0x0C': (0, 69, 89, 255),
            '0x0D': (0, 0, 0, 255),
            '0x0E': (0, 0, 0, 255),
            '0x0F': (0, 0, 0, 255),
            '0x10': (188, 191, 198, 255),
            '0x11': (1, 120, 248, 255),
            '0x12': (6, 134, 254, 255),
            '0x13': (102, 72, 254, 255),
            '0x14': (221, 0, 211, 255),
            '0x15': (226, 0, 107, 255),
            '0x16': (255, 51, 1, 255),
            '0x17': (229, 95, 21, 255),
            '0x18': (171, 129, 2, 255),
            '0x19': (0, 184, 0, 255),
            '0x1A': (0, 170, 5, 255),
            '0x1B': (7, 165, 72, 255),
            '0x1C': (1, 136, 151, 255),
            '0x1D': (44, 44, 44, 255),
            '0x1E': (0, 0, 0, 255),
            '0x1F': (0, 0, 0, 255),
            '0x20': (253, 248, 252, 255),
            '0x21': (56, 192, 254, 255),
            '0x22': (104, 137, 253, 255),
            '0x23': (158, 120, 253, 255),
            '0x24': (254, 119, 255, 255),
            '0x25': (253, 88, 156, 255),
            '0x26': (253, 120, 89, 255),
            '0x27': (253, 158, 76, 255),
            '0x28': (254, 180, 1, 255),
            '0x29': (188, 249, 24, 255),
            '0x2A': (94, 213, 87, 255),
            '0x2B': (89, 248, 157, 255),
            '0x2C': (0, 233, 230, 255),
            '0x2D': (92, 95, 90, 255),
            '0x2E': (0, 0, 0, 255),
            '0x2F': (0, 0, 0, 255),
            '0x30': (253, 248, 252, 255),
            '0x31': (161, 233, 246, 255),
            '0x32': (197, 184, 251, 255),
            '0x33': (220, 185, 249, 255),
            '0x34': (251, 184, 253, 255),
            '0x35': (240, 194, 220, 255),
            '0x36': (244, 209, 181, 255),
            '0x37': (252, 223, 180, 255),
            '0x38': (252, 216, 132, 255),
            '0x39': (219, 248, 122, 255),
            '0x3A': (182, 249, 120, 255),
            '0x3B': (174, 239, 218, 255),
            '0x3C': (0, 247, 252, 255),
            '0x3D': (201, 191, 192, 255),
            '0x3E': (0, 0, 0, 255),
            '0x3F': (0, 0, 0, 255)
}

_nes_sprites = pygame.sprite.Group()


class Palette:
    
    def __init__(self,palette: tuple):
        self[0] = _colors[palette[0]] if palette[0] else (0, 0, 0, 0)
        self[1] = _colors[palette[1]]
        self[2] = _colors[palette[2]]
        self[3] = _colors[palette[3]]
    
    def __setitem__(self, key, item):
        if key > 3:
            raise IndexError('Palette supports only 4 colors')
        elif key < 0:
            key = 4 - key
            if key < 0:
                raise IndexError('Palette supports only 4 colors')
        self.__setattr__('_element_' + str(key), item)
    
    def __getitem__(self, key):
        if key > 3:
            raise IndexError('Palette supports only 4 colors')
        elif key < 0:
            key = 4 - key
            if key < 0:
                raise IndexError('Palette supports only 4 colors')
        return self.__getattribute__('_element_' + str(key))


class NESSprite(pygame.sprite.Sprite):
    
    pixel_size = 0
    
    def __init__(self, data: str, size: tuple, palette: Palette):
        super(NESSprite, self).__init__()
        self.palette = palette
        self.size = size
        self.data = _format_data(data)
        _nes_sprites.add(self)
        self.update()
    
    def update(self):
        row_size = 8 * self.size[0]
        size = (row_size * self.pixel_size, self.size[1] * self.pixel_size * 8)
        image = pygame.Surface(size,
                               flags=(pygame.HWSURFACE |
                                      pygame.SRCALPHA |
                                      pygame.DOUBLEBUF
                                     )
        )
        for index in range(len(self.data) * 8):
            color = self.palette[int(self.data[index // 8][index % 8])]
            position_x = (index % row_size) * self.pixel_size
            position_y = (index // row_size) * self.pixel_size
            pixel = (position_x, position_y, self.pixel_size, self.pixel_size)
            image.fill(color, pixel)
        self.image = image
    
    def save(self, name: str):
        pygame.image.save(self.image, name + '.png')
    
    def change_data(self, data: str):
        self.data = _format_data(data)


class NESTile(pygame.Surface):
    
    pixel_size = 0
    
    def __init__(self, data: str, palette: Palette):
        size = (16 * self.pixel_size, 16 * self.pixel_size)
        super(NESTile, self).__init__(size, 
                                      flags=(pygame.HWSURFACE |
                                             pygame.SRCALPHA |
                                             pygame.DOUBLEBUF
                                      )
        )
        self.palette = palette
        self.data = _format_data(data)
        self.update()
    
    def update(self):
        for index in range(256):
            color = self.palette[int(self.data[index // 8][index % 8])]
            position_x = (index % 8) * self.pixel_size
            position_y = (index // 8) * self.pixel_size
            pixel = (position_x, position_y, self.pixel_size, self.pixel_size)
            self.fill(color, pixel)
    
    def save(self, name:str):
        pygame.image.save(self, name + '.png')
    
    def change_data(self, data: str):
        self.data = _format_data(data)


def _format_data(data: str) -> str:
    formatted_data = list()
    unsplit_data = data[2:]
    while len(unsplit_data) > 0:
        base_1 = bin(int('0x' + unsplit_data[:2], 16))[2:].zfill(8)
        base_2 = bin(int('0x' + unsplit_data[2:4], 16))[2:].zfill(8)
        unsplit_data = unsplit_data[4:]
        base = str()
        for index in range(8):
            if base_1[index] == '0':
                if base_2[index] == '0':
                    base += '0'
                else:
                    base += '2'
            else:
                if base_2[index] == '0':
                    base += '1'
                else:
                    base += '3'
        formatted_data.append((base))
    return formatted_data


def update():
    _nes_sprites.update()