# Aim : to build a caesar decipher by using ascii
# The letters will be shifted by 3
answer = input("do you want to encode or decode (type your answer(encode/decode) after the question mark) ?")
message = input("please enter a message :")
def Encode(messages):
    new_message = ''
    for letter in messages:
        # For letters from A to W (both upper case and lower case)
        if ord(letter) in range(65,88) or ord(letter) in range(97,120):
            new_letters = chr(ord(letter) + 3)
        # For letters from x to z
        elif ord(letter) in range(120,123):
            num = 3 - 122 + ord(letter)
            new_letters = chr(num+96)
        # For letters from X to Z
        elif ord(letter) in range(88,91):
            num = 3 - 90 + ord(letter)
            new_letters = chr(num+64)
        # For any values other than letters
        else:
            new_letters = letter
        new_message += new_letters
    print(new_message)
def Decode(messages):
    new_message = ""
    for letter in messages:
         # For letters from D to Z (both upper case and lower case)
        if ord(letter) in range(68,91) or ord(letter) in range(100,123):
            new_letter = chr(ord(letter) - 3)
        # For letters from A to C
        elif ord(letter) in range(65,68):
            num = 65 - (ord(letter) - 3)
            new_letter = chr(91 - num)
        # For letters from a to c
        elif ord(letter) in range(97,100):
            num = 97 - (ord(letter) - 3)
            new_letter = chr(123 - num)
        # For any values other than letters
        else:
            new_letter = letter
        new_message += new_letter
    print(new_message)
# To decide whether to encode or decode the given message
if answer.lower() == "decode":
    Decode(message)
elif answer.lower() == "encode":
    Encode(message)

    


        
