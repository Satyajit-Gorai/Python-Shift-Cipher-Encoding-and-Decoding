Dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

raw_input = input("enter the message: ")
# Breaking the array into list of charecters
char_array = list(raw_input)
encrypt_msg = []
#print(char_array)
for i in range(len(char_array)):
    if char_array[i] != ' ':
        #extracting the key from Dictionary for the charecter array
        dict_key_from_value = [number for number, name in Dict.items() if name == char_array[i]]
#        print(dict_key_from_value,Dict[dict_key_from_value[0]])
        key_in_int = dict_key_from_value[0]
        encrypt_key = (key_in_int + 12) % 26
#        print(encrypt_key)
#        print(Dict[encrypt_key])
        if (encrypt_key==0):
            encrypt_msg.append(Dict[26])
        else:
            encrypt_msg.append(Dict[encrypt_key])

    else:
        encrypt_msg.append(' ')

final_encrypt_msg = ' '.join(encrypt_msg)
print("Original Message: ", raw_input,"\n")
print("Encrypted Message: ", final_encrypt_msg,"\n")
