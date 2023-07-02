# 1. 느낀 점

django 이론만 듣고 실습이 부족했는데 직접해보면서 url - view - templates의 기본 흐름을 다시 한번 익힐 수 있어서 좋았습니다

오타에 조심해야겠습니다. 찾기가 너무 힘드네요.. 문법보다 오타에 대부분 시간을 썼습니다

form을 from이라고 써서 한참 찾았습니다

장고가 파이썬 문법 안에서는 변수처럼 써도 text로 인식하는것 같은데.. html 태그 안에서는 text로 인식 못해서 "" 붙여주는건지 헷갈린다.. 적당히 감각으로 해야하나

```
    <select name="genre">
    {% for genre in genres %}
        {% if genre == movie.genre %}
    <option label="{{movie.genre}}" value="{{movie.genre}}" selected>
        {%else%}
    <option label="{{genre}}" value="{{genre}}">
        {%endif%}
    {%endfor%}
```

# 2. 배운 점

처음에는 오류 봐도 뭐가 틀린지 모르겠던데 오류메시지 보면서 어디가 틀렸을지 어느정도 예상을 할 수 있을것 같다

select 박스가 option에서 value 속성을 쓰지 않으면 데이터 값이 안들어온다

근데 input 요소는 value속성에 값을 남기고, select는 selected라고 해야 값을 남겨준다

textarea는 태그 밖에다가 값을 남겨야한다

# 3.참조

필드 참고
https://arotein.tistory.com/10

input 타입
https://axce.tistory.com/31
https://cocoon1787.tistory.com/257