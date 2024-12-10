#!/usr/bin/python3
""" UTF-8 validation """

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
        data: List of integers where each integer represents 1 byte of data

    Returns:
        bool: True if data is valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit is set or not
    mask1 = 1 << 7

    # Mask to check if the secong most significant bit is set or not
    mask2 = 1 << 6

    for num in data:
        # Get only the 8 least significant bits
        num = num & 255

        # If this is the start of a new UTF-8 caracter
        if n_bytes == 0:
            # Count number of 1s in the beginning of the byte
            mask = 1 << 7
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False

            # If we are processing continuation bytes
        else:
            # Check if the byte starts with 10
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    # All bytes should be accounted for
    return n_bytes == 0
