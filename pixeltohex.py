def main():
    with open('convert.dat', 'r') as to_convert:
        grid = ''.join(to_convert.readlines())
    grid = ''.join(grid.split('\n'))
    part_1 = str()
    part_2 = str()
    for pixel in grid:
        if (int(pixel) % 2) == 0:
            part_1 += '0'
        else:
            part_1 += '1'
        if int(pixel) > 1:
            part_2 += '1'
        else:
            part_2 += '0'
    binary = str()
    while len(part_1):
        binary += part_1[:8] + part_2[:8]
        part_1 = part_1[8:]
        part_2 = part_2[8:]
    with open('result.dat', 'w') as result:
        converted = str()
        while len(binary) > 4:
            converted += hex(int('0b' + binary[:4], 2))[2:]
            binary = binary[4:]
        result.write('0x' + converted.upper())


if __name__ == '__main__':
    main()