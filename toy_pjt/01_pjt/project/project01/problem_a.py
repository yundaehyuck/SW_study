import json
from pprint import pprint
import os


def movie_info(movie):
    # 여기에 코드를 작성합니다.
    
    return {'id':movie['id'],'title':movie['title'],'poster_path':movie['poster_path'],'vote_average':movie['vote_average'],
    'overview':movie['overview'],'genre_ids':movie['genre_ids']}


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
    #print(movie_dict)#movie_dict가 어떻게 생겼는지 확인함