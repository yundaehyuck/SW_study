import requests
import seaborn as sns
import matplotlib.pyplot as plt

#한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'


#7월 첫째주부터 주말 박스오피스 영화의 매출변화와 어느 나라 영화가 대세인지 살펴보기

weeklist = ['20220703','20220710','20220717','20220724'] #각 주마다 주말 날짜 리스트를 만든다

week_dict = {}

#각 주마다 url을 반복적으로 request하여 해당하는 영화제목, 누적매출액, 누적관객수를 가져옵니다

for ind,week in enumerate(weeklist,start=1):
    
    boxoffice_url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=01d6af266369c5a5a496ef0f24fcff46&targetDt={week}'

    movie_list = []

    boxoffice_response = requests.get(boxoffice_url).json()

    boxoffice_list = boxoffice_response['boxOfficeResult']['weeklyBoxOfficeList']
    showrange = boxoffice_response['boxOfficeResult']['showRange']

    for movie in boxoffice_list:

        #movie 데이터로부터 cd 코드를 받아서 해당 movie의 자세한 정보를 파악해 개봉국가를 구해옵니다.

        movie_url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=01d6af266369c5a5a496ef0f24fcff46&movieCd={movie['movieCd']}"

        movie_response = requests.get(movie_url).json()

        movie_nation = movie_response['movieInfoResult']['movieInfo']['nations'][0]['nationNm']

        movie_list.append((movie['movieNm'],movie['salesAmt'],movie['audiAcc'],movie_nation))
    
    week_dict[ind] = (showrange,movie_list)

#가져온 데이터를 출력합니다.

for key,value in week_dict.items():
    print('====================================================================================================')

    print(f'2022년 7월 {key}주차 ({value[0]}) boxoffice top10'.center(100))
    print('====================================================================================================')
    print()

    for ind,(name,sale,audi,nation) in enumerate(value[1],start=1):
        print(f'{ind}위 : {name}({nation}), 누적매출액 : {sale}, 누적관객수 : {audi}')
        print()

    print('====================================================================================================')
    print()

"""
#########데이터 시각화##############

i = 1 #week

title = []
sale = []
audi = []
nation = []

for ind,column in enumerate(zip(*week_dict[i][1])):
    
    if ind == 0:
        
        title = list(column)
    
    elif ind == 1:
        
        sale = list(map(int,column))
    
    elif ind == 2:
        
        audi = list(map(int,column))
    
    else:

        nation = list(column)

title_nation = [title+'('+nation+')' for title,nation in zip(title,nation)]



plt.suptitle(f'2022년 7월 {i}주차 ({week_dict[i][0]}) boxoffice top10')

plt.subplot(1,2,1)

ax1 = sns.barplot(sale,title_nation)
plt.xlabel('누적매출액',fontsize=20)


plt.subplot(1,2,2)
ax2 = sns.barplot(audi,title_nation)
plt.xlabel('누적관객수',fontsize=20)

plt.show()



####################################################################################################
"""