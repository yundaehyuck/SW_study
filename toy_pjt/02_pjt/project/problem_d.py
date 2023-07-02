import requests
from pprint import pprint


def recommendation(title):
    # 여기에 코드를 작성합니다.  

    # 제목을 받아 조건에 맞는 해당하는 영화의 id를 찾는다

    url_title = f"https://api.themoviedb.org/3/search/movie?api_key=ad80b4bf15ab04539de8939a1d069689&language=ko-KR&region=KR&query='{title}'"

    title_response = requests.get(url_title).json()

    try: #검색한 영화정보가 있다면 첫번째 영화의 id를 구한다

        target_id = title_response['results'][0]['id']
    
    except: #검색한 영화정보가 없다면 None

        return None

    #영화의 id로 추천영화 목록의 타이틀을 찾는다

    url_recommend = f"https://api.themoviedb.org/3/movie/{target_id}/recommendations?api_key=ad80b4bf15ab04539de8939a1d069689&language=ko-KR"

    recommend_response = requests.get(url_recommend).json()

    title_list = []

    for movie in recommend_response['results']:

        title_list.append(movie['title'])
    
    return title_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
