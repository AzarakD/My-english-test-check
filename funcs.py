def answers_to_dict(lst):
    dct = {}
    
    for i in range(1, 51):
        dct[i] = lst[i-1].ent.get()
        
    return dct

def check(kdct, adct):
    k_set = set(kdct.items())
    a_set = set(adct.items())
    wrong_answers = a_set - k_set          # находим неправильные ответы
    right_answers = a_set - wrong_answers  # находим правильные ответы
    
    wrong_answers = dict(wrong_answers)
    right_answers = dict(right_answers)
    wrong_answers = dict(sorted(wrong_answers.items()))
    right_answers = dict(sorted(right_answers.items()))
    
    return wrong_answers, right_answers

def show_res(check_set, field):
    points = 0
    mistakes = 0
    
    for x in check_set[0].items():
        mistakes += 1
    
    for x in check_set[1].items():
        points += 1
    
    if 0 <= points <= 18:       score_text = 'A1'
    elif 19 <= points <= 25:    score_text = 'A2'
    elif 26 <= points <= 32:    score_text = 'B1'
    elif 33 <= points <= 39:    score_text = 'B2'
    elif 40 <= points <= 46:    score_text = 'C1'
    elif 47 <= points <= 50:    score_text = 'C2'
    
    total_text = f'Баллов: {points} из {points + mistakes}. Ошибок: {mistakes}\n'
    field['text'] = total_text + f'Ваш уровень - {score_text}'

def more_info(check_set, field):
    if 'ответы' in field['text']:
        return
    else:
        tab_counter = 0
        field['text'] += '\nНеправильные ответы: '
        for x in check_set[0].items():
            if x[1] == '':
                field['text'] += f'{str(x[0])}: x, '
            else:
                field['text'] += f'{str(x[0])}: {str(x[1])}, '
            tab_counter += 1
            if tab_counter > 14:
                field['text'] += '\n'
                tab_counter = 0
        
        tab_counter = 0
        field['text'] += '\nПравильные ответы: '
        for x in check_set[1].items():
            field['text'] += f'{str(x[0])}: {str(x[1])}, '
            tab_counter += 1
            if tab_counter > 14:
                field['text'] += '\n'
                tab_counter = 0
