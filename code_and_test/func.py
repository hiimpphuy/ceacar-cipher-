from character_list import character_list
def encode(user_input,num_shift):
    output_word = [i for i in user_input]
    for i in range(0,len(output_word)):
        output_word[i] = character_list[character_list.index(output_word[i])+num_shift].lower()
    return "".join(output_word)

def decode(user_input,num_shift):
    output_word = [i for i in user_input]
    for i in range(0, len(output_word)):
        output_word[i] = character_list[character_list.index(output_word[i]) - num_shift].lower()
    return "".join(output_word)
