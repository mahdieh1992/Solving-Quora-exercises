esm_famil = []
dict_replys = {}
scores_participant = {}
def ready_up() -> None:
    with open('esm_famil_data.csv','r',encoding='utf-8') as file:
        count = 0
        global title_list
        title_list =  [title.strip() for title in file.readline().strip().split(',')]
        for line in file:
            current_dict = dict()
            count += 1
            if count == 1 :
                continue
            get_info = line.strip().split(',')
            for i in range(len(title_list)):
                title = title_list[i]
                val  = get_info[i].strip().replace(' ','')
                current_dict[title] = val
            esm_famil.append(current_dict)
    return esm_famil

def add_participant(participant: str, answers: dict[str, str]):
    for key,val in answers.items():
        answers[key] = val.strip().replace(' ','')
    dict_replys[participant] = answers
    scores_participant[participant] = 0

def calculate(title,participant):
    invalid_reply = 0
    valid_reply_uniq = 0
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
            if title_current != dict_replys[participant_][title]:
                valid_reply_uniq += 1
    return invalid_reply,valid_reply_equal,valid_reply_uniq
    
def calculate_all() -> dict[str, int]:
    for title in title_list:
        if any(dict_replys[participant][title] == '' for participant in dict_replys):
            for participant in dict_replys: 
                invalid_reply,valid_reply_equal,valid_reply_uniq = calculate(title,participant)
                if valid_reply_equal > 0:
                         scores_participant[participant] = scores_participant.get(participant) + 10
                elif valid_reply_uniq >= 1 and valid_reply_equal == 0: 
                        scores_participant[participant] = scores_participant.get(participant) + 15
                elif invalid_reply == 1:
                        scores_participant[participant] = scores_participant.get(participant) + 0
        else:
            for participant in dict_replys: 
                invalid_reply,valid_reply_equal,valid_reply_uniq = calculate(title,participant) 
                if valid_reply_equal > 0:
                         scores_participant[participant] = scores_participant.get(participant) + 5
                elif valid_reply_uniq >= 1 and valid_reply_equal == 0: 
                        scores_participant[participant] = scores_participant.get(participant) + 10
                elif invalid_reply == 1:
                        scores_participant[participant] = scores_participant.get(participant) + 0
    return scores_participant 
                                        
ready_up()
add_participant(participant = 'salib', answers = {'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
add_participant(participant = 'kianoush', answers = {'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
add_participant(participant = 'sajjad', answers = {'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
add_participant(participant = 'farhad', answers = {'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})
print(calculate_all())
