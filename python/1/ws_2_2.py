
s = input()

s_list = []


#앞쪽 특수문자 제거하기 위해 앞에서 처음으로 알파벳 나오는 인덱스 찾기

for ind,char in enumerate(s):

    if not char.isalpha():

        pass
    
    else:
        
        break

start_ind = ind

#뒤쪽 특수문자 제거하기 위해 뒤에서 처음으로 알파벳 나오는 인덱스 찾기

for ind,char in enumerate(s[::-1]):

    if not char.isalpha():

        pass
    
    else:

        break

end_ind = -1*ind-1


#특수문자 제거

#맨 뒤에 올 수 있는 문장 부호이면 포함시키기

if s[end_ind+1] in ['.','!','?']:

    end_ind += 1

s = s[start_ind:end_ind+1]

#s를 순회하면서 최초 나오는 대문자가 I이면 소문자로 바꾸지 않고
#나머지는 모두 소문자로 바꿔서 넣기

f_upper = False

for char in s:

    if not f_upper:

        if char.isupper():

            f_upper = True

            if char == 'I':

                s_list.append(char)
            
            else:
                
                s_list.append(char.lower())
        
        else:

            s_list.append(char)
    

    else:

        s_list.append(char.lower())




print(''.join(s_list))




