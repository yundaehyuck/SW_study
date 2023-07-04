words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}


antonym_list = []

for word in words_dict:

    if word[0] == 'l':

        antonym_list.append('il'+word)
    
    elif word[0] == 'r':

        antonym_list.append('ir'+word)

    else:
        antonym_list.append('im'+word)

    #더 정확한 답?

    """elif word[0] == 'b' or word[0] == 'm' or word[0] == 'p':

        antonym_list.append('im'+word)
    
    else:
        antonym_list.append('in'+word)"""

antonym_list.sort()

print(antonym_list)
