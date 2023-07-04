"""첨부파일
words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
print(wordrelay(words)) # 5번째 참가자가 탈락하였습니다."""


def wordrelay(word_list):

    before_word = []

    for ind,word in enumerate(word_list,start = 1):

        try:

            if word not in before_word:

                if before_word[-1][-1] == word[0]:

                    before_word.append(word)
                
                else:

                    return f"{ind}번째 참가자가 탈락하였습니다."
            
            else:

                return f"{ind}번째 참가자가 탈락하였습니다."
        
        except:

            before_word.append(word)

        s = input('done을 입력하면 끝말잇기를 그만합니다.')

        if s == 'done':

            break
    
    return f"탈락자가 없습니다."

words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]

print(wordrelay(words))

        






