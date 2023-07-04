
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

group_word = {}

for word in words:

    group_key = list(word) #'aeet' 같은 경우도 있을 수 있으므로 list로 변환

    group_key.sort() #오름차순으로 정렬해서 애너그램은 같은 리스트를 가지도록

    group_key = tuple(group_key) #dict key로 사용하기 위해 tuple로 변환

    #gropu_key = ''.join(sorted(word)) #정렬한 문자열을 key로 사용

    try:
        
        group_word[group_key].append(word)
    
    except:

        group_word[group_key] = []

        group_word[group_key].append(word)
    
    """if group_word.get(group_key):
           
           group_word[group_key].append(word)
        
       else:

           group_word[gropu_key] = [word]"""


for ind,(key,value) in enumerate(group_word.items(),start=1):

    print(f"group{ind} : {value}")
