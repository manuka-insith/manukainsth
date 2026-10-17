import random
def changing_text(text):
    new_text=text.split()
def encode (text):
    key =  random.randint(1,50)
    normal_text='abcdefghijklmnopqrstuvwxyz '
    numbers='1234567890'
    signs='''!@#$%^&*()_-+={}[];:'",<.>/?~`'''
    clear_text = str(normal_text+numbers+signs)
    mixed_text= str(clear_text[key:]+clear_text[:key])
    encode_text= str.maketrans(clear_text,mixed_text)
    encode_text_with_key = text.translate(encode_text)
    if len(str(key))==1:
        return encode_text_with_key + '0'+str(key)
    elif len(str(key)) == 2 :
        return encode_text_with_key+str(key)
def decode (text):
    if isinstance(int(text[-2]),int):
        str_key = text[-2:]
        key_index = text.find(str_key)
        key = int(text[-2:])
        text = text[:key_index]
    elif not isinstance(int(text[-2]),int):
        return f'is this your text:{text}'
    else:
        return 'plsease  try again'
    normal_text='abcdefghijklmnopqrstuvwxyz '
    numbers='1234567890'
    signs='''!@#$%^&*()_-+={}[];:'",<.>/?~`'''
    clear_text = str(normal_text+numbers+signs)
    mixed_text= str(clear_text[key:]+clear_text[:key])
    decoding_text= str.maketrans(mixed_text,clear_text)
    decoded_text_with_key = text.translate(decoding_text)
    return decoded_text_with_key
    
def use_encrypter ():
    input_text = input('type your text:')
    try:
        how_many_times = int(input('how many times should it encrypt: ')) 
    except ValueError:
        print('Please use a number')
    text = ''
    for i in range(how_many_times):
        
        text = encode(input_text)
    print(text)
def use_decrypter():
    encrypted_text = input('type your encrypted text:')
    while True:
        decrypted_text=decode(encrypted_text)
        
        if decrypted_text[-2:].isdigit():
            encrypted_text = decrypted_text
            continue
        
        elif  isinstance(decrypted_text[-2:],str):
            print(decrypted_text)
            break
        else:
            print('something went wrong please try again')
        break


while True:
    print('''
    choose the number as your wants
    1. encryption
    2. decryption
    3. exit
    ''')
    try:
        choice = int(input('choose a number: '))
    except :
        print('enter a valid number')
        continue
    if choice == 1:
        use_encrypter()
    elif choice == 2:
        use_decrypter()
    elif choice == 3:
        exit()
    else:
        print('please enter a valid number')
        continue