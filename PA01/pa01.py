"""
============================================================================
| Assignment: pa01 - Encrypting a plaintext file using the Hill cipher
|
| Author: Giovanni Acireale
| Language: python
|
| To Compile: python3 pa01.py
|
| To Execute: python3 pa01.py kX.txt pX.txt
| where kX.txt is the keytext file
| and pX.txt is plaintext file
| Note:
| All input files are simple 8 bit ASCII input
| All execute commands above have been tested on Eustis
|
| Class: CIS3360 - Security in Computing - Spring 2023
| Instructor: McAlpin
| Due Date: per assignment
+===========================================================================
"""

import sys

def read_key(filename):
    with open(filename, 'r') as file:
        file.readline()
        key = []
        for line in file:
            row = list(map(int, line.strip().split()))
            key.append(row)
    return key

def extract_letters(filename):
    letters = []
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    letters.append(char.lower())
    return ''.join(letters)

def matrix_multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            value = 0
            for k in range(len(matrix2)):
                value += matrix1[i][k] * matrix2[k][j]
            row.append(value)
        result.append(row)
    return result

def hill_cipher_encrypt(key, plaintext):
    key_size = len(key)
    ciphertext = ''
    for i in range(0, len(plaintext), key_size):
        chunk = plaintext[i:i+key_size]
        chunk_vector = [ord(char) - ord('a') for char in chunk]
        encrypted_chunk = matrix_multiply(key, [chunk_vector])[0]
        encrypted_chunk = [value % 26 for value in encrypted_chunk]
        ciphertext += ''.join([chr(num + ord('a')) for num in encrypted_chunk])
    return ciphertext

def output_ciphertext(ciphertext):
    print("\nCiphertext:")
    for i in range(0, len(ciphertext), 80):
        print(ciphertext[i:i+80])
    print()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pa01.py <key_file> <plaintext_file>")
        sys.exit(1)

    key_file = sys.argv[1]
    plaintext_file = sys.argv[2]

    key = read_key(key_file)
    plaintext = extract_letters(plaintext_file)

    print("Key matrix:")
    for row in key:
        print(' '.join(map(str, row)))

    print("\nPlaintext:")
    for i in range(0, len(plaintext), 80):
        print(plaintext[i:i+80])
    print()

    ciphertext = hill_cipher_encrypt(key, plaintext)

    output_ciphertext(ciphertext)

"""
=============================================================================
| I Giovanni Acireale 5582169 affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+=============================================================================
"""