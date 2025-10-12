import re
def words_check(text: str) -> dict[str, int]:
    pattern = r'[a-zA-Z]'
    words = text.split()
    dict_str = {}
    for word in words:
        length = len(word)
        bad_char = sum(1 for char in word if not char.isalpha())
        if  bad_char * 2 >= length:
            continue
        word =''.join(re.findall(pattern,word))
        good_word = word.capitalize()
        dict_str[good_word] = dict_str.get(good_word,0) + 1
    result = dict(sorted(dict_str.items()))      
    return result

char = """HeLLLO_O My________________FRIEND\nHOW ARE YOUUUUU?___?\nI Don'T KNow Y_O_U_R_N_A_M_E yet !!!!!!!!"""
print(words_check(char))
