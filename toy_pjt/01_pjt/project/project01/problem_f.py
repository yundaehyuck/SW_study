import json
import os

#제공된 영화데이터에서 runtime이 가장 긴 순서대로 top5 제목을 출력하기

#영화제목과 해당하는 runtime을 튜플로 가지는 리스트 만들기

def movies_runtime(movies):

    all_id_list = []

    for movie in movies:

        all_id_list.append(movie['id']) #제공된 영화데이터에 존재하는 id 목록을 만들기

    cwd = os.getcwd()

    meta_dir = cwd+'\\'+'data\\movies' #movies 폴더 경로를 구하고

    metadata_list = os.listdir(meta_dir) #movies에 존재하는 파일목록을 구합니다.

    runtime_datalist = []

    for metadata in metadata_list:

        target_dir = meta_dir+'\\'+metadata #파일 경로를 지정하고

        metajson = open(target_dir,encoding='UTF8')
        meta_dict = json.load(metajson)

        if meta_dict['id'] in all_id_list:

            runtime_datalist.append((meta_dict['title'],meta_dict['runtime'],meta_dict['production_countries'][0]['iso_3166_1'],meta_dict['popularity']))
        
    
    sort_runtime_data = sorted(runtime_datalist,key=lambda item:[-item[1]]) #runtime이 큰 순서대로 내림차순 정렬하고

    return sort_runtime_data





if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    
    movies_list = json.load(movies_json)
    
    runtime_list = movies_runtime(movies_list)

    #런타임이 가장 긴 top5 출력

    print("런타임 긴 top5")

    for ind,(title,run,country,pop) in enumerate(runtime_list,start=1):

        print(f'top{ind}: {title}, runtime:{run}, country:{country}, popularity:{pop}')

        if ind == 5:

            break
    
    print("=================================================================")

    print("런타임 짧은 top5")
    
    #런타임이 가장 짧은 top5 출력

    for ind,(title,run,country,pop) in enumerate(runtime_list[::-1],start=1):

        print(f'top{ind}: {title}, runtime:{run}, country:{country}, popularity:{pop}')

        if ind == 5:

            break