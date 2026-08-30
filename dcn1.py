def bit_stuffing(data):
    """Insert a '0' after every five consecutive '1' bits."""
    stuffed = ""
    count = 0
    for bit in data:
        stuffed += bit
        if bit == '1':
            count += 1
            if count == 5:
                stuffed += '0'  # stuff an extra 0
                count = 0
        else:
            count = 0
    return stuffed


def bit_destuffing(data):
    """Remove the stuffed '0' that follows every five consecutive '1' bits."""
    destuffed = ""
    count = 0
    i = 0
    n = len(data)
    while i < n:
        bit = data[i]
        destuffed += bit
        if bit == '1':
            count += 1
            if count == 5:
                i += 1  # skip the stuffed 0
                count = 0
        else:
            count = 0
        i += 1
    return destuffed


if __name__ == "__main__":
    original = "110111110"
    print("Original Bit Stream  : ", original)

    stuffed = bit_stuffing(original)
    print("Stuffed Bit Stream   : ", stuffed)

    destuffed = bit_destuffing(stuffed)
    print("De-stuffed Bit Stream: ", destuffed)

    print("\nMatch with original?", destuffed == original)