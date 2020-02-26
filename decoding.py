Dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

raw_input = input("enter the encrypted message: ")
# Breaking the array into list of charecters
char_array = list(raw_input)
decrypt_msg = []
#print(char_array)
for i in range(len(char_array)):
    if char_array[i] != ' ':
        #extracting the key from Dictionary for the charecter array
        dict_key_from_value = [number for number, name in Dict.items() if name == char_array[i]]
#        print(dict_key_from_value,Dict[dict_key_from_value[0]])
        key_in_int = dict_key_from_value[0]

        skey = (key_in_int - 12)
        if skey > 0 :
            decrypt_key = skey
        else:
            decrypt_key = skey + 26
#        print(encrypt_key)
#        print(Dict[encrypt_key])
        if (decrypt_key==0):
            decrypt_msg.append(Dict[26])
        else:
            decrypt_msg.append(Dict[decrypt_key])

    else:
        decrypt_msg.append(' ')

final_decrypt_msg = ' '.join(decrypt_msg)
print("Decrypted Message: ", raw_input,"\n")
print("Original Message: ", final_decrypt_msg,"\n")
