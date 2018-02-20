# pynesgame
NES-like sprite interface for pygame

## Classes

### pynes.Palette(palette: tuple)
Class representing an NES palette<br>
The 'palette' argument must contain 4 values among _False_ and the ones contained in the [Color Reference](#Colorreference)<br>
_False_ represents transparent pixels, for sprites by standard it should be the element 0 in the palette<br>
Example:<br>
Super Mario's palette from Super Mario Bros can be:<br>
(False, '0x16', '0x18', '0x28')<br>
The hex value is case sensitive, the 'x' must be lowercase, the digits must be uppercase<br>
Instances of 'Palette' are iterables, elements can be edited but not added or deleted<br>

### Class variables
#### pynes.NESSprite.pixel_size
Size of a single "pixel" of the sprite, measured in pixels

### Attributes
#### pynes.NESSprite.palette
Palette currently used by the sprite
#### pynes.NESSprite.size
Number of orizontal and vertical tiles
#### pynes.NESSprite.data
Hex value of the sprite
#### pynes.NESSprite.image
Image composed using the hex value recived

### pynes.NESSprite(data: str, size: tuple, palette: Palette)
Class representing an NES sprite<br>
The 'data' argument must be an hex value, the exact value can be obtained by using the [pixeltohex.py](#pixeltohex.py) script<br>
The 'size' argument must be a tuple containing two elements: (number of horizontal tiles, number of vertical tiles)<br>
The 'palette' argument must be a pynes.Palette instance<br>
#### pynes.NESSprite.update()
Updates the sprite<br>
If the sprite is part of a [pygame.sprite.Group](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group) you can also use [pygame.sprite.Group.update()](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.update)
#### pynes.NESSprite.save(name: str)
Saves the generated sprite in name.png<br>

## Functions

## pynes.update()
Updates every pynes.NESSprite instance

## pixeltohex.py
A script that generates a readable hex value for the NESSprite <br>
The input must be written in a file named 'convert.dat', every character must correspond to a pixel in the image, lines can be wrapped<br>
Accepted characters: 0, 1, 2, 3<br>
Every character must be the index of the color used in that pixel in the palette<br>
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
![#788083](https://placehold.it/15/788083/000000?text=+) 0x00<br>
![#0100fc](https://placehold.it/15/0100fc/000000?text=+) 0x01<br>
![#0000bf](https://placehold.it/15/0000bf/000000?text=+) 0x02<br>
![#3e28c7](https://placehold.it/15/3e28c7/000000?text=+) 0x03<br>
![#8f028e](https://placehold.it/15/8f028e/000000?text=+) 0x04<br>
![#ae002c](https://placehold.it/15/ae002c/000000?text=+) 0x05<br>
![#ab1103](https://placehold.it/15/ab1103/000000?text=+) 0x06<br>
![#8fddff](https://placehold.it/15/8fddff/000000?text=+) 0x07<br>
![#503001](https://placehold.it/15/503001/000000?text=+) 0x08<br>
![#007b01](https://placehold.it/15/007b01/000000?text=+) 0x09<br>
![#006901](https://placehold.it/15/006901/000000?text=+) 0x0A<br>
![#005902](https://placehold.it/15/005902/000000?text=+) 0x0B<br>
![#004559](https://placehold.it/15/004559/000000?text=+) 0x0C<br>
![#000000](https://placehold.it/15/000000/000000?text=+) 0x0D<br>
![#000000](https://placehold.it/15/000000/000000?text=+) 0x0E<br>
![#000000](https://placehold.it/15/000000/000000?text=+) 0x0F<br>
![#bcbfc6](https://placehold.it/15/bcbfc6/000000?text=+) 0x10<br>
![#0178f8](https://placehold.it/15/0178f8/000000?text=+) 0x11<br>
![#0686fe](https://placehold.it/15/0686fe/000000?text=+) 0x12<br>
![#6648fe](https://placehold.it/15/6648fe/000000?text=+) 0x13<br>
![#dd00d3](https://placehold.it/15/dd00d3/000000?text=+) 0x14<br>
![#e2006b](https://placehold.it/15/e2006b/000000?text=+) 0x15<br>
![#ff3301](https://placehold.it/15/ff3301/000000?text=+) 0x16<br>
![#e55f15](https://placehold.it/15/e55f15/000000?text=+) 0x17<br>
![#ab8102](https://placehold.it/15/ab8102/000000?text=+) 0x18<br>
![#00b800](https://placehold.it/15/00b800/000000?text=+) 0x19<br>
![#00aa05](https://placehold.it/15/00aa05/000000?text=+) 0x1A<br>
![#07a548](https://placehold.it/15/07a548/000000?text=+) 0x1B<br>
![#018897](https://placehold.it/15/018897/000000?text=+) 0x1C<br>
![#2c2c2c](https://placehold.it/15/2c2c2c/000000?text=+) 0x1D<br>
![#000000](https://placehold.it/15/000000/000000?text=+) 0x1E<br>
![#000000](https://placehold.it/15/000000/000000?text=+) 0x1F<br>
![#fdf8fc](https://placehold.it/15/fdf8fc/000000?text=+) 0x20<br>
![#38c0fe](https://placehold.it/15/38c0fe/000000?text=+) 0x21<br>
![#6889fd](https://placehold.it/15/6889fd/000000?text=+) 0x22<br>
![#9e78fd](https://placehold.it/15/9e78fd/000000?text=+) 0x23<br>
![#fe77ff](https://placehold.it/15/fe77ff/000000?text=+) 0x24<br>
![#fd589c](https://placehold.it/15/fd589c/000000?text=+) 0x25<br>
![#fd7859](https://placehold.it/15/fd7859/000000?text=+) 0x26<br>
![#fd9e4c](https://placehold.it/15/fd9e4c/000000?text=+) 0x27<br>
![#feb401](https://placehold.it/15/feb401/000000?text=+) 0x28<br>
![#bcf918](https://placehold.it/15/bcf918/000000?text=+) 0x29<br>
![#5ed557](https://placehold.it/15/5ed557/000000?text=+) 0x2A<br>
![#59f89d](https://placehold.it/15/59f89d/000000?text=+) 0x2B<br>
![#00e9e6](https://placehold.it/15/00e9e6/000000?text=+) 0x2C<br>
![#5c5f5a](https://placehold.it/15/5c5f5a/000000?text=+) 0x2D<br>
![#000000](https://placehold.it/15/000000/000000?text=+) 0x2E<br>
![#000000](https://placehold.it/15/000000/000000?text=+) 0x2F<br>
![#fdf8fc](https://placehold.it/15/fdf8fc/000000?text=+) 0x30<br>
![#a1e9f6](https://placehold.it/15/a1e9f6/000000?text=+) 0x31<br>
![#c5b8fb](https://placehold.it/15/c5b8fb/000000?text=+) 0x32<br>
![#dcb9f9](https://placehold.it/15/dcb9f9/000000?text=+) 0x33<br>
![#fbb8fd](https://placehold.it/15/fbb8fd/000000?text=+) 0x34<br>
![#f0c2dc](https://placehold.it/15/f0c2dc/000000?text=+) 0x35<br>
![#f4d1b5](https://placehold.it/15/f4d1b5/000000?text=+) 0x36<br>
![#fcdfb4](https://placehold.it/15/fcdfb4/000000?text=+) 0x37<br>
![#fcd884](https://placehold.it/15/fcd884/000000?text=+) 0x38<br>
![#dbf87a](https://placehold.it/15/dbf87a/000000?text=+) 0x39<br>
![#b6f978](https://placehold.it/15/b6f978/000000?text=+) 0x3A<br>
![#aeefda](https://placehold.it/15/aeefda/000000?text=+) 0x3B<br>
![#00f7fc](https://placehold.it/15/00f7fc/000000?text=+) 0x3C<br>
![#c9bfc0](https://placehold.it/15/c9bfc0/000000?text=+) 0x3D<br>
![#000000](https://placehold.it/15/000000/000000?text=+) 0x3E<br>
![#000000](https://placehold.it/15/000000/000000?text=+) 0x3F<br>
