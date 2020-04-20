import random

sample = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 `-=~!@#$%^&*()_{}[]\|:;\'\"<>?,./'

#generating hash randomly based on sample

hash_list = list(sample)
random.shuffle(hash_list)
hash = ''.join(hash_list)

print(len(sample))
print(len(hash))
message = input('Enter your message : ')

#value of key can be random
key = 10
encrypt = ''

#seed = length of sample or hash, to avoid 'string index out of range' error.
seed = 94

#message encryption
for i in message:
    encrypt_position = hash.find(i)
    new_encrypt_postion = (encrypt_position+key) % seed
    encrypt += hash[new_encrypt_postion]
print(encrypt)

decrypt = ''

#encrypted message decryption
for i in encrypt:
    decrypt_position = hash.find(i)
    new_decrypt_postion = (decrypt_position-key) % seed
    decrypt += hash[new_decrypt_postion]
print(decrypt)
