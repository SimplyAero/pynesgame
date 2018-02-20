import pynes


def main():
    pynes.NESSprite.pixel_size = 20
    with open('test.dat', 'r') as test:
        character = test.readlines()
    size = (int(character[1].rstrip()), int(character[2].rstrip()))
    palette = pynes.Palette((False,
                             character[3].rstrip(),
                             character[4].rstrip(),
                             character[5].rstrip()
                            )
    )
    sprite = pynes.NESSprite("0x" + character[0].rstrip(), 
                             size, 
                             palette
    )
    sprite.save('test')


if __name__ == '__main__':
    main()