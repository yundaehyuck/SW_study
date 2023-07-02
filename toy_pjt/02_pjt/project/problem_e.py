import requests
from pprint import pprint


def credits(title):
    # 여기에 코드를 작성합니다.

    #제공되는 타이틀로 영화를 검색

    url_title = f"https://api.themoviedb.org/3/search/movie?api_key=ad80b4bf15ab04539de8939a1d069689&language=ko-KR&region=KR&query='{title}'"

    title_response = requests.get(url_title).json()

    try: #검색되는 영화정보가 있다면 첫번째 id정보를 찾아옵니다

        target_id = title_response['results'][0]['id']
    
    except: #검색되는 영화정보가 없다면 None을 반환

        return None

    #검색한 id를 이용하여 cast&crew 데이터를 가져온다
    
    url_cast_crew = f'https://api.themoviedb.org/3/movie/{target_id}/credits?api_key=ad80b4bf15ab04539de8939a1d069689&language=ko-KR'

    cast_crew_response = requests.get(url_cast_crew).json()

    #cast_id가 10 미만인 cast를 찾는다

    cast_list = [cast['name'] for cast in cast_crew_response['cast'] if cast['cast_id'] < 10]

    #directing인 crew를 찾는다

    crew_list = [crew['name'] for crew in cast_crew_response['crew'] if crew['department'] == 'Directing']

    return {'cast':cast_list,'crew':crew_list}

        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
