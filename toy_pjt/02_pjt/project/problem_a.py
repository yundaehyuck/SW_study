import requests


def popular_count():
    # 여기에 코드를 작성합니다.
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=ad80b4bf15ab04539de8939a1d069689&language=ko-KR&region=KR'

    response = requests.get(url).json()

    return len(response['results'])





# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
