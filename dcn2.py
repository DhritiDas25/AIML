import numpy as np

def vrc(data):
    ones = data.count('1')

    if ones % 2 == 0:
        parity = '0'
    else:
        parity = '1'

    return parity + data

data = "1000001"

print("VRC")
print("Data:", data)
print("VRC:", vrc(data))

def lrc(data):
    rows = []
    for row in data:
        ones = row.count('1')

        if ones % 2 == 0:
            parity = '0'
        else:
            parity = '1'

        rows.append(row + parity)

    lrc_bits = ""

    for col in range(len(rows[0])):
        ones = 0

        for row in rows:
            if row[col] == '1':
                ones += 1

        if ones % 2 == 0:
            lrc_bits += '0'
        else:
            lrc_bits += '1'

    return rows, lrc_bits

data = [
    "1101",
    "1011",
    "0010",
    "1110"
]
rows, lrc_result = lrc(data)
print("LRC")

print("Rows with VRC:")
for row in rows:
    print(row)

print("LRC:", lrc_result)

def checksum(words):
    total = 0

    for word in words:
        total += int(word, 2)

        while total > 255:
            carry = total >> 8
            total = (total & 255) + carry
    check = total ^ 255

    return format(check, '08b')


words = [
    "11110000",
    "00100010"
]

print("CHECKSUM")

print("Word 1:", words[0])
print("Word 2:", words[1])

print("Checksum:", checksum(words))

def crc(data, generator):

    r = len(generator) - 1

    appended_data = data + '0' * r

    data_list = list(appended_data)

    # Modulo-2 division using XOR
    for i in range(len(data)):

        if data_list[i] == '1':

            for j in range(len(generator)):
                data_list[i + j] = str(
                    int(data_list[i + j]) ^
                    int(generator[j])
                )

    # Remainder = CRC
    remainder = ''.join(data_list[-r:])

    # Data + CRC
    codeword = data + remainder

    return remainder, codeword

def check_crc(codeword, generator):
    data_list = list(codeword)
    # Modulo-2 division
    for i in range(len(codeword) - len(generator) + 1):
        if data_list[i] == '1':
            for j in range(len(generator)):
                data_list[i + j] = str(
                    int(data_list[i + j]) ^
                    int(generator[j])
                )

    remainder = ''.join(
        data_list[-(len(generator) - 1):]
    )

    if int(remainder, 2) == 0:
        return "No error detected"
    else:
        return "Error detected"

data = "1101"
generator = "1011"
crc_result, codeword = crc(data, generator)
print("Data:", data)
print("Generator:", generator)
print("CRC:", crc_result)
print("Transmitted codeword:", codeword)
print("Receiver:", check_crc(codeword, generator))