import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.

    #movie에서 value 추출

    id_value = movie['id']
    title = movie['title']
    poster_path = movie['poster_path']
    vote_average = movie['vote_average']
    overview = movie['overview']
    genre_ids = movie['genre_ids']

    #genres를 id:name dict로 변환

    genre_id_name_dict = {}

    for genre in genres:

        genre_id_name_dict[genre['id']] = genre['name']

    #genre_ids의 ind번째 원소를 genre_id_name_dict를 이용해서 대응하는 name으로 교체 
    
    for ind,value in enumerate(genre_ids):

        genre_ids[ind] = genre_id_name_dict[value]
    
    return {'id':id_value, 'title':title, 'poster_path':poster_path,'overview':overview,'genre_names':genre_ids,'vote_average':vote_average}


        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))

    #print(movie)#movie가 어떻게 생겼는지 확인함
    #print(genres_list)#genres_list가 어떻게 생겼는지 확인함