#!/usr/bin/env python
#filename: encrypt_data.py
#

import base64


def encrypt(key, clear):
    '''enciphered data'''
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = (ord(clear[i]) + ord(key_c)) % 256
        enc.append(enc_c)
    print(enc)
    return base64.urlsafe_b64encode(bytes(enc))


def decrypt2(key, enc):
    '''decipher data'''
   dec = []
   enc = base64.urlsafe_b64decode(enc)
   for i in range(len(enc)):
       key_c = key[i % len(key)]
       dec_c = chr((256 + enc[i] - ord(key_c)) % 256)
       dec.append(dec_c)
   return "".join(dec)


if __name__ == '__main__':
    #Specify the encryption key
    keyC = '123456012'
    #Specify the encrypted data
    clearT = 'This is a magical world!'

    print(encrypt(keyC, clearT).decode())

    enc =  encrypt(keyC, clearT)
    print(decrypt2(keyC, enc))
