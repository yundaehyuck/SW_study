import json
import os #파일 목록을 확인하기 위한 모듈


def max_revenue(movies):

    #제공된 영화데이터의 모든 id리스트를 만든다

    all_id_list = []

    for movie in movies:

        all_id_list.append(movie['id'])

    cwd = os.getcwd()

    target_dir = cwd+'\\data\\movies'

    #movies 내부에 존재하는 파일 목록의 리스트를 받아옴

    metadata_list = os.listdir(target_dir) #['11216.json', '122.json', '129.json', '13.json', '155.json', '238.json', '278.json'...]

    #movies 파일목록을 순회합니다

    revenue_list = []

    for metadata in metadata_list:

        #target_num = int(metadata[:-5]) #movies 파일 목록은 (id).json형태이므로 .json을 뺀 숫자만 추출합니다

        targetjson = target_dir+'\\'+metadata #파일을 열기위한 경로를 구합니다.

        target_file = open(targetjson,encoding='UTF8')
        target_dict = json.load(target_file) #파일을 열고 dict로 만듭니다.

        #print(target_dict.keys()) #dict의  key가 무엇이 있는지 확인해봄

        if target_dict['id'] in all_id_list: #movies 폴더 내에 있는 파일의 id가 movies.json 데이터의 id목록에 존재한다면

            revenue_list.append((target_dict['title'],target_dict['revenue'])) #찾고자하는 데이터이므로 그것의 제목과 수익을 넣습니다.
    
    
    sort_revenue_list = sorted(revenue_list,key=lambda item: [-item[1]])

    return sort_revenue_list[0][0]





# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

    #print(movies_list)
