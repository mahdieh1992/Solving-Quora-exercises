#واحد حفاظت و امنیت
import re 
class Security:
    pattern = r'([A-Z][a-z]+):www\.([a-z0-9]+\.[a-z0-9]+)/(\w+)'  
     
    def secure(self, info: str) -> str:
        def rep(match):
            username = match.group(3)
            encrypt = self.encrypt(username)
            return f"{match.group(1)}:www.{match.group(2)}/{encrypt}"
        return re.sub(Security.pattern,rep,info)       
    
    def is_social_account_info(self, param: str) -> bool:
        return bool(re.fullmatch(Security.pattern,param)) 
    
    def encrypt(self, s: str) -> int:
        set_char = set(s)
        code_char = {char: ord(char) - 96 for char in set_char}
        char_dict = {}
        result = ""

        for chr in s:
            char_dict[chr] = char_dict.get(chr,0) + 1
        list_char = [chr * char_dict[chr] for chr in char_dict]    

        for string in list_char:
            for indx,sub_str in enumerate(string):
                result += str((indx + 1) * code_char[sub_str])
        return result

string = "abcccdd"
s = Security()
# print(s.encrypt(string))
# print(s.is_social_account_info("Instagram:www.instagram.com/aalavi"))
print(s.secure("FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02 Gender:male Instagram:www.instagram.com/aalavi Degree:Master Twitter:www.twiter.com/alaviii imdb:www.imdb.com/alavi"))