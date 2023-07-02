import json
import os
from datetime import datetime


def dec_movies(movies):
    # 여기에 코드를 작성합니다.

    #movies.json에서 존재하는 영화 데이터의 id들을 추출합니다.

    all_id_list = []

    for movie in movies_list:  

        all_id_list.append(movie['id'])
    
    cwd = os.getcwd()

    meta_dir = cwd+'\\'+'data\\movies' #movies 폴더 경로를 구하고

    metadata_list = os.listdir(meta_dir) #movies 폴더 내부의 데이터 목록을 얻습니다

    release_12_list = []

    for metadata in metadata_list:

        target_dir = meta_dir+'\\'+metadata #열고자 하는 파일 경로를 지정하고

        metajson = open(target_dir,encoding='UTF8')
        meta_dict = json.load(metajson)

        #print(meta_dict.keys()) #키를 확인

        #print(meta_dict['release_date']) #'1988-11-17'

        #print(type(meta_dict['release_date'])) #'str'

        #movies 폴더 내에 id가 movies.json 데이터 id로 존재하는경우에

        if meta_dict['id'] in all_id_list:

            #개봉일이 12월인 경우

            if datetime.strptime(meta_dict['release_date'],'%Y-%m-%d').month == 12:

                release_12_list.append(meta_dict['title']) #제목을 리스트에 넣습니다.
    
    return release_12_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))

    #print(movies_list)