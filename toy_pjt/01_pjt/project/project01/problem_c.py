import json
from pprint import pprint


def movie_info(movies, genres):
    # 여기에 코드를 작성합니다.

    pop_movie_list = []

    genre_id_name_dict = {}

    #genres_list에 존재하는 dict를 순회하여 id:name 형태의 dict 구성

    for genre in genres:

        genre_id_name_dict[genre['id']] = genre['name']

    #movies에 존재하는 각 movie dict들을 가지고와서 정보를 추출

    for movie in movies:

        id_value = movie['id']
        title = movie['title']
        poster_path = movie['poster_path']
        vote_average = movie['vote_average']
        overview = movie['overview']
        genre_ids= movie['genre_ids']

        #genre_ids의 id를 genre_id_name_dict를 활용해서 name으로 대체

        for ind,value in enumerate(genre_ids):

            genre_ids[ind] = genre_id_name_dict[value]
        
        #새로만든 dict를 pop_movie_list에 넣기

        pop_movie_list.append({'id':id_value,'title':title,'poster_path':poster_path,'vote_average':vote_average,'overview':overview,'genre_names':genre_ids})
    
    return pop_movie_list
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))

    #각 리스트 내용을 확인

    #print(movies_list)
    #print(genres_list) 