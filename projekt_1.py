"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Oupic Svoboda
email: tomas.svoboda@ideastatica.com
discord: Tomáš#7986
"""
# import ...

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
         red, purple, yellow and gray beds of the Wasatch
         Formation. Eroded portions of these horizontal
         beds slope gradually upward from the valley floor
         and steepen abruptly. Overlying them and extending
         to the top of the butte are the much steeper
         buff-to-white beds of the Green River Formation,
         which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
         a portion of the largest deposit of freshwater fish
         fossils in the world. The richest fossil fish deposits
         are found in multiple limestone layers, which lie some
         100 feet below the top of the butte. The fossils
         represent several varieties of perch, as well as
         other freshwater genera and herring similar to those
         in modern oceans. Other fish such as paddlefish,
         garpike and stingray are also present.'''
         ]
cara = '-' * 40
users = {'bob': '123', 'ann': 'pass123', 'mike': 'pasword123', 'liz': 'pass132'}
break1 = False
for ii in range(1):  # nevěděl jsem jak lépe vyskočit z programu
    print('$ python projekt1.py')
    user_name = input('username: ')
    #print('username: ', user_name)
    pasw = input('password: ')

    if not user_name in users.keys():
        print('unregistered user, terminating the program..')
        break

    while pasw != users[user_name]:
        pasw = input('wrong password, try again or press q: ')
        if pasw == 'q':
            print('terminating the program..')
            break1 = True
            break
    if break1:
        break

    #print('password: ', pasw)
    print(cara)
    print('Welcome to the app,', user_name)
    print('We have 3 texts to be analyzed.')
    print(cara)
    number = input('Enter a number btw. 1 and 3 to select: ')
    if not number.isdigit():
        print('A number is needed. terminating the program')
        break
    number = int(number)
    if not number in [1, 2, 3]:
        print('A wrong input. terminating the program')
        break
    #print('Enter a number btw. 1 and 3 to select: ', number)
    print(cara)

    txtsplt = TEXTS[number - 1].split(' ')
    splitted = []  # *****odstraní znaky\n
    for txtsplt_1 in txtsplt:
        if '\n' in txtsplt_1:
            inner = txtsplt_1.split('\n')
            inner_dl = len(inner)
            for i in range(inner_dl):
                splitted.append(inner[i])
        else:
            splitted.append(txtsplt_1)  # *****odstraní znaky\n

    while '' in splitted:
        splitted.remove('')

    words = len(splitted)

    t_words, u_words, l_words, n_words, sum_w, max_delka, counter = 0, 0, 0, 0, 0, 0, 0
    chart = []
    for A in splitted:
        t_words += 1 if A[0].isupper() else 0
        for B in A:
            if B.isnumeric():
                break
        else:
            u_words += 1 if A.isupper() else 0
        l_words += 1 if not A.isupper() and not A[0].isupper() and not A.isnumeric() else 0
        if A.isnumeric():
            n_words += 1
            sum_w += int(A)

        counter += 1
        if ',' in A or '.' in A:
            splitted[counter - 1] = splitted[counter - 1].replace(',', '')
            splitted[counter - 1] = splitted[counter - 1].replace('.', '')

    for A in splitted:
        if max_delka < len(A):
            max_delka = len(A)

    for i in range(max_delka):
        chart.append(0)
    for A in splitted:
        chart[len(A) - 1] += 1

    print('There are', words, 'words in the selected text.')
    print('There are', t_words, 'titlecase words.')
    print('There are', u_words, 'uppercase words.')
    print('There are', l_words, 'lowercase words')
    print('There are', n_words, 'lowercase words')
    print('The sum of all the numbers', sum_w)
    print(cara)
    np = 1 if (max(chart) - 9 % 2) > 0 else 0
    print('LEN|', ' ' * ((max(chart) - 9) // 2), 'OCCURENCE', ' ' * ((max(chart) - 9) // 2 - np), '|NR.')
    print(cara)

    for i in range(max_delka):
        if i > 8:
            print(i + 1, '|', '*' * chart[i], ' ' * (max(chart) - chart[i]), '|', chart[i])
        else:
            print('', i + 1, '|', '*' * chart[i], ' ' * (max(chart) - chart[i]), '|', chart[i])