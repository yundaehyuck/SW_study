words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

bef_word_list = []

for ind,word in enumerate(words):

    end = input("Done을 입력하면 끝말잇기를 종료합니다. : ")

    if end == 'Done': #Done을 입력할때까지 끝말잇기를 수행

        break
    
    else:

        print(ind,word) #ind번째 사람이 말한 단어 출력

        try:

            if word in bef_word_list: #이전 단어를 말한건지 검사

                print(f"{ind}번째 사람이 탈락")
                break
            
            else: #이전 단어를 말하지 않았으니 첫번째는 통과

                if bef_word_list[-1][-1] == word[0]:

                    bef_word_list.append(word)
                
                else:

                    print(f"{ind}번째 사람이 탈락")
                    break

        
        except:

            bef_word_list.append(word)

print("끝말잇기가 끝났습니다.")
