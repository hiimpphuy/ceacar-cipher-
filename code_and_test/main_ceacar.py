from func import encode,decode
import os
while True:
    os.system("clear")
    print("1 for encrypt\n2 for decrypt")
    a = int(input())
    if a == 1:
        os.system("clear")
        user_input = input("Type the message you want to encode\n")
        num_shift = int(input("Type a number to encode\n"))
        print(encode(user_input=user_input,num_shift=num_shift))
    if a == 2:
        os.system("clear")
        user_input = input("Type the message you want to decode")
        num_shift = int(input("Type a number to decode"))
        print(decode(user_input=user_input,num_shift=num_shift))
    ask_user = input("Do you want to encode or decode again ?? Yes or No\n").lower()
    if ask_user == "yes" :
        pass
    elif ask_user == "no":
        break