import re
def check_words(text: str) -> dict[str, int]:
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
if __name__ == '__main__':
    print(check_words("""hEllO My FriEnDs!!! thIS is A tEsT For your #p#r#o#b#l#e#m a"""))
