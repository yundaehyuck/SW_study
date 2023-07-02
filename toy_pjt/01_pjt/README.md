# 1) 배운 점?

### 1. os 모듈 사용

- os.getcwd()로 현재 작업환경 받아오기

- os.listdir(path)로 path에 존재하는 파일 목록 받아오기

- os.chdir(path)하면 현재 작업경로를 path로 바꾸기

### 2. 날짜 다루기

- from datetime import datetime

- datetime.strptime(str,format) : str을 format에 맞는 날짜 타입으로 바꾸기

- 예를 들어 datetime.strptime('1988-12-03','%Y-%m-%d) 하면 1988년 12월 3일을 날짜 형식으로 가지고  .year, .month, .day 등으로 원하는 부분만 가져온다

### 3. json 파일 열기

- json = open(파일경로, encoding='UTF8')
- json_dict = json.load(json)


# 2) 어려운 점?

### 데이터를 보고 어떤 인사이트를 얻고 싶은지 생각하는게 쉽지 않다..


# 3) 느낀 점?

### 내가 만들기를 원하는 기능을 생각하고 천천히 논리적으로 생각하면서 코딩할 수 있어서 좋았습니다  

### 어떤 부분이 틀렸는지, 어떻게 진행되고 있는지 중간중간 print()하면서 확인해보면서 코딩할 수 있어서 좋았습니다.