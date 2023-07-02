/* 
  아래에 코드를 작성해주세요.
*/

//1.검색창 만들기

//검색창을 가져온다
const search_box = document.querySelector('body > main > div.search-box > input')

//a.검색창의 value를 입력하면 keyword라는 변수에 저장

let keyword = ''

search_box.addEventListener('input',function() {

  keyword = search_box.value

})

//검색버튼을 가져오고 searchBtn에 저장

const searchBtn = document.querySelector('body > main > div.search-box > button')

//c. 클릭시 발생할 콜백함수

//앨범 정보를 저장할 변수
let albums = []


//검색 결과안에 들어간 모든 결과를 삭제하는 함수
function removeAllchild(div) {
  while (div.hasChildNodes()) {
      div.removeChild(div.firstChild);
  }
}

//page와 limit의 기본값은 각각 1과 10
function fetchAlbums (page=1,limit=10) {
  //메시지가 정상 출력되는지 확인
  //alert('확인!')
  //2.api요청하기
  const musicUrl = `https://ws.audioscrobbler.com/2.0/?method=album.search&album=${keyword}&api_key=d4019612ab5b136e995409ae1e13368a&format=json`

  //search한 결과를 넣을 위치를 찾아온다
  const result = document.querySelector('body > main > div.search-result')

  //새로운 검색결과를 표시하기 위해, 검색 결과를 먼저 모두 제거합니다.
  removeAllchild(result)

  axios.get(musicUrl)
  .then((response) => {
    //요청 응답에 성공했을 경우
    //검색 결과를 albums에 저장
    console.log(musicUrl)
    albums = response.data.results.albummatches.album
    
    //검색 결과를 순회합니다.

    //순회하기 전에, result에 담긴 모든 자식 요소를 제거합니다

    for (let album of albums) {
      
      //앨범명, 앨범 아티스트명, 앨범 이미지 정보를 가져옵니다.  
      let albumName = album.name
      let albumArtist = album.artist
      let albumImg = album.image[1]['#text']

      //이미지를 넣을 태그를 생성

      const cardImg = document.createElement('img')
      cardImg.setAttribute('src',albumImg)

      //첫번째 div태그를 생성

      const card = document.createElement('div')
      card.classList.add('search-result__card')

      //두번째 div태그를 생성

      const text = document.createElement('div')
      text.classList.add('search-result__text')

      //아티스트의 이름

      const artistTag = document.createElement('h2')
      artistTag.innerText = albumArtist

      //앨범 영

      const albumTag = document.createElement('p')
      albumTag.innerText = albumName

      // 이미지 태그를 먼저 card에 넣는다
      card.appendChild(cardImg)

      // 아티스트와 앨범 이름을 추가

      text.appendChild(artistTag)
      text.appendChild(albumTag)

      //text 태그를 card태그에 추가

      card.appendChild(text)

      //검색결과를 표시

      result.appendChild(card)
    }
    //3.검색 결과
  })
  .catch((error) => {
    //요청에 실패할 경우
    alert('잠시 후 다시 시도해주세요.')
  })
}
//b. 클릭시 발생할 이벤트

searchBtn.addEventListener('click',fetchAlbums)

/*
비동기식으로 albums에 저장이 되고 있는데
albums에 저장이 되는게 끝나기 전에
얘를 수행하니까, albums에 빈상태로 보이는거
for (let album of albums) {
  console.log(album.name)
  console.log(album.artist)
  console.log(album.url)
}*/