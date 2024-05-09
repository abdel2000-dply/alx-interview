#!/usr/bin/python3
'''UTF-8 Validation
'''


def validUTF8(data):
    '''Determines if a given data set represents a valid UTF-8 encoding
    '''
    count = 0
    for byte in data:
        byte = byte & 255
        if count == 0:
            if byte >> 5 == 0b110:
                count = 1
            elif byte >> 4 == 0b1110:
                count = 2
            elif byte >> 3 == 0b11110:
                count = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            count -= 1
    return count == 0
