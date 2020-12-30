# This project is poorly implemented and deprecated, keeping it here for archiving reasons

# pynesgame
NES-like sprite interface for pygame

## Classes

### pynes.Palette(palette: tuple)
Class representing an NES palette<br>
The 'palette' argument must contain 3 values among the ones contained in the [Color Reference](#Colorreference)<br>
Example:<br>
Super Mario's palette from Super Mario Bros can be:<br>
('0x16', '0x18', '0x28')<br>
The hex value is case sensitive, the 'x' must be lowercase, the digits must be uppercase<br>
Instances of 'Palette' are iterables, elements can be edited but not added or deleted<br>



### pynes.NESSprite(data: str, size: tuple, palette: Palette)
Class representing an NES sprite<br>
The 'data' argument must be an hex value, the exact value can be obtained by using the [pixeltohex.py](#pixeltohex.py) script<br>
The 'size' argument must be a tuple containing two elements: (number of horizontal tiles, number of vertical tiles)<br>
The 'palette' argument must be a pynes.Palette instance<br>
#### Class variables
##### pynes.NESSprite.pixel_size
Size of a single "pixel" of the sprite, measured in pixels

#### Attributes
##### pynes.NESSprite.palette
Palette currently used by the sprite
##### pynes.NESSprite.size
Number of orizontal and vertical tiles
##### pynes.NESSprite.data
Colors used in each pixel
##### pynes.NESSprite.image
Image composed using the hex value recived
#### Methods
##### pynes.NESSprite.update()
Updates the sprite<br>
If the sprite is part of a [pygame.sprite.Group](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group) you can also use [pygame.sprite.Group.update()](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.update)
##### pynes.NESSprite.save(name: str)
Saves the generated sprite in name.png<br>
##### pynes.NESSprite.change_data(data: str)
Changes the current hex value for the sprite

### pynes.NESTile(data: str, palette: Palette)
Class representing an NES tile<br>
The 'data' argument must be an hex value, the exact value can be obtained by using the [pixeltohex.py](#pixeltohex.py) script<br>
The 'palette' argument must be a pynes.Palette instance<br>
#### Class variables
##### pynes.NESTile.pixel_size
Size of a single "pixel" of the tile, measured in pixels
#### Attributes
##### pynes.NESSprite.palette
Palette currently used by the tile
##### pynes.NESTile.data
Colors used in each pixel
#### Methods
##### pynes.NESTile.update()
Updates the tile<br>
##### pynes.NESTile.save(name: str)
Saves the generated tile in name.png
##### pynes.NESTile.change_data(data: str)
Changes the current hex value for the tile

## Functions

### pynes.update()
Updates every pynes.NESSprite instance

### pynes.spritify(image_data: str, palette: Palette, size: tuple, pixel_size: int)
Creates a static image from an hex value, useful for creating animated sprites without having to re-parse data every frame
The 'image_data' argument must be an hex value, the exact value can be obtained by using the [pixeltohex.py](#pixeltohex.py) script<br>
The 'palette' argument must be a pynes.Palette instance<br>
The 'size' argument must be a tuple containing two elements: (number of horizontal tiles, number of vertical tiles)<br>
The 'pixel_size' argument represents how many pixels is a single square in the sprite


## pixeltohex.py
A script that generates a readable hex value for the NESSprite <br>
The input must be written in a file named 'convert.dat', every character must correspond to a pixel in the image, lines can be wrapped<br>
Accepted characters: 0, 1, 2, 3<br>
Every character must be the index of the color used in that pixel in the palette, 0 is transparent<br>
The result will be written in 'result.dat'<br>
Example:<br>
0000001111100000<br>
0000113222311000<br>
0001322222223100<br>
0013222222222100<br>
0012222222222310<br>
0122222221212310<br>
1322222221212221<br>
1222222221212221<br>
1222223322223321<br>
1322322222222321<br>
0132122222122131<br>
0011322222223110<br>
0001133222231100<br>
0013311111113310<br>
0133333111133331<br>
0011111000111110<br>
will return<br>
0x0300E0000E0338E0180F0CF8301F04F8201F06FC403F56ACC07F51AE807F51AE837F0DFEC87F05FE683727DA380F0EF81E071CF03F18FE0C7F3EFF1E3E003E0<br>
And when converted it will become Kirby's sprite

## test.py
Script that can be used to test if a sprite displays correctly<br>
The input must be in a file called 'test.dat', and it must be formatted in this way:<br>
__hex value (without 0x)__<br>
__number of horizontal tiles__<br>
__number of vertical tiles__<br>
__element [1] in the palette__<br>
__element [2] in the palette__<br>
__element [3] in the palette__<br>
The result will be saved in 'test.png'


## Color reference
![#007880](https://placehold.it/15/007880/000000?text=+) 0x00<br>
![#010100](https://placehold.it/15/010100/000000?text=+) 0x01<br>
![#020000](https://placehold.it/15/020000/000000?text=+) 0x02<br>
![#033e28](https://placehold.it/15/033e28/000000?text=+) 0x03<br>
![#048f02](https://placehold.it/15/048f02/000000?text=+) 0x04<br>
![#05ae00](https://placehold.it/15/05ae00/000000?text=+) 0x05<br>
![#06ab11](https://placehold.it/15/06ab11/000000?text=+) 0x06<br>
![#078f16](https://placehold.it/15/078f16/000000?text=+) 0x07<br>
![#085030](https://placehold.it/15/085030/000000?text=+) 0x08<br>
![#09007b](https://placehold.it/15/09007b/000000?text=+) 0x09<br>
![#0A0069](https://placehold.it/15/0A0069/000000?text=+) 0x0A<br>
![#0B0059](https://placehold.it/15/0B0059/000000?text=+) 0x0B<br>
![#0C0045](https://placehold.it/15/0C0045/000000?text=+) 0x0C<br>
![#0D0000](https://placehold.it/15/0D0000/000000?text=+) 0x0D<br>
![#0E0000](https://placehold.it/15/0E0000/000000?text=+) 0x0E<br>
![#0F0000](https://placehold.it/15/0F0000/000000?text=+) 0x0F<br>
![#10bcbf](https://placehold.it/15/10bcbf/000000?text=+) 0x10<br>
![#110178](https://placehold.it/15/110178/000000?text=+) 0x11<br>
![#120686](https://placehold.it/15/120686/000000?text=+) 0x12<br>
![#136648](https://placehold.it/15/136648/000000?text=+) 0x13<br>
![#14dd00](https://placehold.it/15/14dd00/000000?text=+) 0x14<br>
![#15e200](https://placehold.it/15/15e200/000000?text=+) 0x15<br>
![#16ff33](https://placehold.it/15/16ff33/000000?text=+) 0x16<br>
![#17e55f](https://placehold.it/15/17e55f/000000?text=+) 0x17<br>
![#18ab81](https://placehold.it/15/18ab81/000000?text=+) 0x18<br>
![#1900b8](https://placehold.it/15/1900b8/000000?text=+) 0x19<br>
![#1A00aa](https://placehold.it/15/1A00aa/000000?text=+) 0x1A<br>
![#1B07a5](https://placehold.it/15/1B07a5/000000?text=+) 0x1B<br>
![#1C0188](https://placehold.it/15/1C0188/000000?text=+) 0x1C<br>
![#1D2c2c](https://placehold.it/15/1D2c2c/000000?text=+) 0x1D<br>
![#1E0000](https://placehold.it/15/1E0000/000000?text=+) 0x1E<br>
![#1F0000](https://placehold.it/15/1F0000/000000?text=+) 0x1F<br>
![#20fdf8](https://placehold.it/15/20fdf8/000000?text=+) 0x20<br>
![#2138c0](https://placehold.it/15/2138c0/000000?text=+) 0x21<br>
![#226889](https://placehold.it/15/226889/000000?text=+) 0x22<br>
![#239e78](https://placehold.it/15/239e78/000000?text=+) 0x23<br>
![#24fe77](https://placehold.it/15/24fe77/000000?text=+) 0x24<br>
![#25fd58](https://placehold.it/15/25fd58/000000?text=+) 0x25<br>
![#26fd78](https://placehold.it/15/26fd78/000000?text=+) 0x26<br>
![#27fd9e](https://placehold.it/15/27fd9e/000000?text=+) 0x27<br>
![#28feb4](https://placehold.it/15/28feb4/000000?text=+) 0x28<br>
![#29bcf9](https://placehold.it/15/29bcf9/000000?text=+) 0x29<br>
![#2A5ed5](https://placehold.it/15/2A5ed5/000000?text=+) 0x2A<br>
![#2B59f8](https://placehold.it/15/2B59f8/000000?text=+) 0x2B<br>
![#2C00e9](https://placehold.it/15/2C00e9/000000?text=+) 0x2C<br>
![#2D5c5f](https://placehold.it/15/2D5c5f/000000?text=+) 0x2D<br>
![#2E0000](https://placehold.it/15/2E0000/000000?text=+) 0x2E<br>
![#2F0000](https://placehold.it/15/2F0000/000000?text=+) 0x2F<br>
![#30fdf8](https://placehold.it/15/30fdf8/000000?text=+) 0x30<br>
![#31a1e9](https://placehold.it/15/31a1e9/000000?text=+) 0x31<br>
![#32c5b8](https://placehold.it/15/32c5b8/000000?text=+) 0x32<br>
![#33dcb9](https://placehold.it/15/33dcb9/000000?text=+) 0x33<br>
![#34fbb8](https://placehold.it/15/34fbb8/000000?text=+) 0x34<br>
![#35f0c2](https://placehold.it/15/35f0c2/000000?text=+) 0x35<br>
![#36f4d1](https://placehold.it/15/36f4d1/000000?text=+) 0x36<br>
![#37fcdf](https://placehold.it/15/37fcdf/000000?text=+) 0x37<br>
![#38fcd8](https://placehold.it/15/38fcd8/000000?text=+) 0x38<br>
![#39dbf8](https://placehold.it/15/39dbf8/000000?text=+) 0x39<br>
![#3Ab6f9](https://placehold.it/15/3Ab6f9/000000?text=+) 0x3A<br>
![#3Baeef](https://placehold.it/15/3Baeef/000000?text=+) 0x3B<br>
![#3C00f7](https://placehold.it/15/3C00f7/000000?text=+) 0x3C<br>
![#3Dc9bf](https://placehold.it/15/3Dc9bf/000000?text=+) 0x3D<br>
![#3E0000](https://placehold.it/15/3E0000/000000?text=+) 0x3E<br>
![#3F0000](https://placehold.it/15/3F0000/000000?text=+) 0x3F<br>
