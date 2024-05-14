"""
=============================================================================
| Assignment: pa02 - Calculating an 8, 16, or 32 bit
| checksum on an ASCII input file
|
| Author: Giovanni Acireale
| Language: Python
|
| To Compile: 
| python pa02.py //Caution - expecting input parameters
|
| To Execute: python3 pa02.py inputFile.txt 8
| where inputFile.txt is an ASCII input file
| and the number 8 could also be 16 or 32
| which are the valid checksum sizes, all
| other values are rejected with an error message
| and program termination
|
| Note: All input files are simple 8 bit ASCII input
|
| Class: CIS3360 - Security in Computing - Spring 2024
| Instructor: McAlpin
| Due Date: 3/31/2024
|
+=============================================================================
"""

import sys

def calculate_checksum(data, checksum_size):
    checksum = 0
    for byte in data:
        checksum += byte

    if checksum_size == 16:
        checksum_low = checksum & 0xFFFF  # Mask to 16 bits
        checksum_high = checksum >> 16  # Get high 16 bits
        checksum = checksum_low + checksum_high

        # Handle carry if checksum is greater than 0xFFFF
        if checksum > 0xFFFF:
            checksum = (checksum & 0xFFFF) + 1

        checksum = checksum & 0xFFFF  # Mask to 16 bits

    elif checksum_size == 32:
        while checksum > 0xFFFFFFFF:
            carry = checksum >> 32
            checksum = (checksum & 0xFFFFFFFF) + carry
        checksum = checksum & 0xFFFFFFFF  # Mask to 32 bits

    elif checksum_size == 8:
        while checksum > 0xFF:
            carry = checksum >> 8
            checksum = (checksum & 0xFF) + carry
        checksum = checksum & 0xFF  # Mask to 8 bits

    else:
        sys.stderr.write("Error: Invalid checksum size. Valid sizes are 8, 16, or 32 bits.\n")
        sys.exit(1)

    return checksum

def main():
    # Step 1: Collect command line arguments
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python pa02.py <input_file> <checksum_size>\n")
        sys.exit(1)

    input_file = sys.argv[1]
    checksum_size = int(sys.argv[2])

    # Print collected arguments for verification (comment out in final version)
    print(f"Input File: {input_file}")
    print(f"Checksum Size: {checksum_size} bits")

    # Step 2: Read and print file content
    try:
        with open(input_file, 'rb') as file:
            data = file.read()
            file.close()

            # Step 3: Adjust output to 80 characters per line
            print("Input text:")
            for i in range(0, len(data), 80):
                print(data[i:i+80].decode('utf-8'))

            # Step 4: Calculate checksum based on the specified size
            checksum = calculate_checksum(data, checksum_size)
            
            # Pad the checksum with 'X' if needed for 32-bit size
            if checksum_size == 32:
                checksum_str = f"{checksum:X}"
                checksum_length = checksum_size // 4  # Number of characters for checksum based on size
                padded_checksum = 'X' * max(0, checksum_length - len(checksum_str)) + checksum_str
            else:
                padded_checksum = f"{checksum:X}"

            print(f"{checksum_size} bit checksum is {padded_checksum} for all {len(data)} chars")

    except FileNotFoundError:
        sys.stderr.write("Error: Input file not found.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()

"""
=============================================================================
| I Giovanni Acireale (5582169) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================
"""