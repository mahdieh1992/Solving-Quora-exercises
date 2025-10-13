esm_famil = []
dict_replys = {}
scores_participant = {}

# this function delete all space
def clear_space (word: str) -> str:
    word = ''.join(word.split())
    return word

# reading inforamtion from esm_famil file and into dict
def ready_up() -> None:
    global title_list
    with open('esm_famil_data.csv','r',encoding='utf-8') as file:
        title_list =  [title.strip() for title in file.readline().strip().split(',')]
        for line in file:
            current_dict = dict()
            get_info = line.strip().split(',')
            if len(get_info) != len(title_list):
                continue
            for i in range(len(title_list)):
                title = title_list[i]
                val  = clear_space(get_info[i])
                current_dict[title] = val
            esm_famil.append(current_dict)
    return esm_famil

# read replys and into dict_replys 
def add_participant(participant: str, answers: dict[str, str]):
    for key,val in answers.items():
        answers[key] = clear_space(val)
    dict_replys[participant] = answers
    scores_participant[participant] = 0

def calculate(title,participant):
    invalid_reply = 0
    valid_reply_equal = 0
    title_current = dict_replys[participant][title]
    check_exists = any(title_current == esm[title] for esm in esm_famil)
    if not check_exists or title_current == '':
        invalid_reply = 1
    else:
        for participant_ in dict_replys:
            if participant == participant_:
                continue
            if title_current == dict_replys[participant_][title]:
                valid_reply_equal += 1
    return invalid_reply,valid_reply_equal

# calculate replyes a participant with other participant    
def calculate_all() -> dict[str, int]:
    global dict_replys, scores_participant, esm_famil, title_list
    # I config replys equal 0 after calculate
    scores_participant = {p: 0 for p in dict_replys}
    for title in title_list:
        has_Empty = any(dict_replys[participant][title] == '' for participant in dict_replys)
        for participant in dict_replys: 
            invalid_reply,valid_reply_equal = calculate(title,participant)   
            if has_Empty:
                if valid_reply_equal > 0:
                    scores_participant[participant] += 10
                elif invalid_reply == 1: 
                    scores_participant[participant] += 0
                else:
                    scores_participant[participant] += 15
            else:
                if valid_reply_equal > 0:
                    scores_participant[participant] += 5
                elif invalid_reply == 1: 
                    scores_participant[participant] += 0
                else:
                    scores_participant[participant] += 10
    return scores_participant 
if __name__ == '__main__' :                           
    ready_up()
    add_participant(participant = 'salib', answers = {'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
    add_participant(participant = 'kianoush', answers = {'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
    add_participant(participant = 'sajjad', answers = {'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
    add_participant(participant = 'farhad', answers = {'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})
    print(calculate_all())
