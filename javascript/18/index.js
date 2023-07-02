// 코드를 작성해 주세요


//가위바위보 알고리즘
const playGame = (p1_choice, p2_choice) => {

	if (p1_choice === 'rock'){

		if (p2_choice === 'paper') {

			return 2

		} else if (p2_choice == 'rock') {

			return 0
		} else {

			return 1
		}
	} else if (p1_choice == 'paper') {

		if (p2_choice == 'paper') {

			return 0
		} else if (p2_choice == 'rock') {

			return 1
		} else {

			return 2
		}
	} else {

		if (p2_choice == 'paper') {

			return 1
		} else if (p2_choice == 'rock') {

			return 2
		} else {

			return 0
		}
	}
}

//가위바위보 이미지 경로를 담은 배열

const rock_paper_scissors = ["./img/scissors.png","./img/rock.png","./img/paper.png"]

//버튼 3개의 위치

const scissors_button = document.querySelector('#scissors-button')
const rock_button = document.querySelector('#rock-button')
const paper_button = document.querySelector('#paper-button')

//player1,2의 이미지 위치

const player1_choice = document.querySelector('#player1-img')
const player2_choice = document.querySelector('#player2-img')

//게임 점수판의 위치

const count_player1 = document.querySelector('body > div.container > div > span.countA.m-1')
const count_player2 = document.querySelector('body > div.container > div > span.countB.m-1')

//모달창 위치
//class name을 select할때 반드시 앞에 .을 붙여줘야함
const modal = document.querySelector('.modal')
const modal_text = document.querySelector('.modal-content')

//가위 버튼을 눌렀을때,

scissors_button.addEventListener('click',function(){
    
    //player1의 이미지를 가위로 변경
    player1_choice.setAttribute('src',rock_paper_scissors[0])

    //버튼을 클릭하면, 나머지 버튼을 비활성화 시킵니다.

    scissors_button.setAttribute('disabled','')
    rock_button.setAttribute('disabled','')
    paper_button.setAttribute('disabled','')

    //player2의 이미지를 3초간, 0.1초 간격으로 변경하고자 함
    
    //인덱스 변수 선언
    var i = 0
    
    //0.1초마다 image를 가위,바위,보 순서로 바꿔주는 함수
    const changeImg = setInterval(function(){

        player2_choice.setAttribute('src',rock_paper_scissors[i])
        
        //현재 이미지 보여주고 인덱스 증가
        i++
        
        //인덱스가 3이상이 된다면.. 처음부터 다시 시작하기 위해 0으로 바꿔줌
        /*if (i>=3){
            i = 0
        }*/

        //i=0,1,2중 하나가 되어야하므로 3으로 나눠줍니다.
        i = i%3

    },100)

    //3초 후에 clearInterval을 호출하여 변경시키는 함수를 중지하도록 만들어준다.

    //3초 후에 게임 결과가 나와야한다.

    setTimeout(function(){

        clearInterval(changeImg)
    
        //컴퓨터가 랜덤하게 배열에서 가위,바위,보 중 하나를 선택합니다.

        const computer_choice = rock_paper_scissors[Math.floor(Math.random()*rock_paper_scissors.length)]

        //컴퓨터가 랜덤하게 선택한 이미지를 표시해줍니다.
    
        player2_choice.setAttribute('src',computer_choice)

        //게임 결과 구하기

        const player1 = 'scissors'

        //경로 문자열 앞이 ./img/이고 뒤가 .png임을 이용해서 가위,바위,보 추출
        const player2 = computer_choice.slice(6,-4)

        const result = playGame(player1,player2)

        //score를 가져옵니다.
        //변경시켜야하므로 let으로 선언

        let player1_score = Number(count_player1.innerText)
        let player2_score = Number(count_player2.innerText)

        //결과에 따라 점수판 변경

        if (result == 1) {

            player1_score += 1

            //변경시킨 값을 다시 삽입
        //string으로 안바꿔도 알아서 되는데?

            count_player1.innerText = player1_score
            count_player2.innerText = player2_score
           
           //모달 내용 삽입
            modal_text.innerText = 'player1 의 승리입니다!'
          
           //모달 창의 display를 변경한다
           //css를 변경하거나 추가할때는.. (요소이름).style.(속성명) = value

           //flex로 하면 가운데에 뜨고, block으로 하면 맨 위로 뜬다
            modal.style.display = 'flex'
            //modal.style.transition = 'all 1s';
           
            //모달창을 클릭하면 사라지도록 합니다.
            modal.addEventListener('click',function(){
                modal.style.display = 'none'
            })



        } else if (result == 2){

            player2_score += 1

            //변경시킨 값을 다시 삽입

            count_player1.innerText = player1_score
            count_player2.innerText = player2_score

            //모달 내용 삽입
            modal_text.innerText ='player2의 승리입니다!'

            //모달 창의 display를 변경
            modal.style.display = 'flex'

            //모달창을 클릭하면 사라지도록 만든다.
            modal.addEventListener('click',function(){
                modal.style.display = 'none'
            })

        } else {

            //무승부이므로, 값을 변경하지않고 모달창만 변경

            modal_text.innerText = '무승부입니다!'

            //모달 창의 display를 변경

            modal.style.display = 'flex'

            //모달 창을 클릭하면 사라지도록 만든다

            modal.addEventListener('click',function(){
                modal.style.display = 'none'
            })

        }

        //버튼 disabled 속성을 제거하고, 게임을 다시 할 수있도록 만든다

        scissors_button.removeAttribute('disabled')
        rock_button.removeAttribute('disabled')
        paper_button.removeAttribute('disabled')
    
    
    
    },3000)


})

//바위 버튼을 눌렀을때,

rock_button.addEventListener('click',function(){
    
    //player1의 이미지를 바위로 변경
    player1_choice.setAttribute('src',rock_paper_scissors[1])

    //버튼을 클릭하면, 나머지 버튼을 비활성화 시킵니다.

    scissors_button.setAttribute('disabled','')
    rock_button.setAttribute('disabled','')
    paper_button.setAttribute('disabled','')

    //player2의 이미지를 3초간, 0.1초 간격으로 변경하고자 함
    
    //인덱스 변수 선언
    var i = 0
    
    //0.1초마다 image를 가위,바위,보 순서로 바꿔주는 함수
    const changeImg = setInterval(function(){

        player2_choice.setAttribute('src',rock_paper_scissors[i])
        
        //현재 이미지 보여주고 인덱스 증가
        i++
        
        //인덱스가 3이상이 된다면.. 처음부터 다시 시작하기 위해 0으로 바꿔줌
        /*if (i>=3){
            i = 0
        }*/

        //i=0,1,2중 하나가 되어야하므로 3으로 나눠줍니다.
        i = i%3

    },100)

    //3초 후에 clearInterval을 호출하여 변경시키는 함수를 중지하도록 만들어준다.

    //3초 후에 게임 결과가 나와야한다.

    setTimeout(function(){

        clearInterval(changeImg)
    
        //컴퓨터가 랜덤하게 배열에서 가위,바위,보 중 하나를 선택합니다.

        const computer_choice = rock_paper_scissors[Math.floor(Math.random()*rock_paper_scissors.length)]

        //컴퓨터가 랜덤하게 선택한 이미지를 표시해줍니다.
    
        player2_choice.setAttribute('src',computer_choice)

        //게임 결과 구하기

        const player1 = 'rock'

        //경로 문자열 앞이 ./img/이고 뒤가 .png임을 이용해서 가위,바위,보 추출
        const player2 = computer_choice.slice(6,-4)

        const result = playGame(player1,player2)

        //score를 가져옵니다.
        //변경시켜야하므로 let으로 선언

        let player1_score = Number(count_player1.innerText)
        let player2_score = Number(count_player2.innerText)

        //결과에 따라 점수판 변경

        if (result == 1) {

            player1_score += 1

            //변경시킨 값을 다시 삽입
        //string으로 안바꿔도 알아서 되는데?

            count_player1.innerText = player1_score
            count_player2.innerText = player2_score
           
           //모달 내용 삽입
            modal_text.innerText = 'player1 의 승리입니다!'
          
           //모달 창의 display를 변경한다
           //css를 변경하거나 추가할때는.. (요소이름).style.(속성명) = value

           //flex로 하면 가운데에 뜨고, block으로 하면 맨 위로 뜬다
            modal.style.display = 'flex'
            //modal.style.transition = 'all 1s';
           
            //모달창을 클릭하면 사라지도록 합니다.
            modal.addEventListener('click',function(){
                modal.style.display = 'none'
            })



        } else if (result == 2){

            player2_score += 1

            //변경시킨 값을 다시 삽입

            count_player1.innerText = player1_score
            count_player2.innerText = player2_score

            //모달 내용 삽입
            modal_text.innerText ='player2의 승리입니다!'

            //모달 창의 display를 변경
            modal.style.display = 'flex'

            //모달창을 클릭하면 사라지도록 만든다.
            modal.addEventListener('click',function(){
                modal.style.display = 'none'
            })

        } else {

            //무승부이므로, 값을 변경하지않고 모달창만 변경

            modal_text.innerText = '무승부입니다!'

            //모달 창의 display를 변경

            modal.style.display = 'flex'

            //모달 창을 클릭하면 사라지도록 만든다

            modal.addEventListener('click',function(){
                modal.style.display = 'none'
            })

        }

        //버튼 disabled 속성을 제거하고, 게임을 다시 할 수있도록 만든다

        scissors_button.removeAttribute('disabled')
        rock_button.removeAttribute('disabled')
        paper_button.removeAttribute('disabled')
    
    
    
    },3000)


})

//보 버튼을 눌렀을때,

paper_button.addEventListener('click',function(){
    
    //player1의 이미지를 보로 변경
    player1_choice.setAttribute('src',rock_paper_scissors[2])

    //버튼을 클릭하면, 나머지 버튼을 비활성화 시킵니다.

    scissors_button.setAttribute('disabled','')
    rock_button.setAttribute('disabled','')
    paper_button.setAttribute('disabled','')

    //player2의 이미지를 3초간, 0.1초 간격으로 변경하고자 함
    
    //인덱스 변수 선언
    var i = 0
    
    //0.1초마다 image를 가위,바위,보 순서로 바꿔주는 함수
    const changeImg = setInterval(function(){

        player2_choice.setAttribute('src',rock_paper_scissors[i])
        
        //현재 이미지 보여주고 인덱스 증가
        i++
        
        //인덱스가 3이상이 된다면.. 처음부터 다시 시작하기 위해 0으로 바꿔줌
        /*if (i>=3){
            i = 0
        }*/

        //i=0,1,2중 하나가 되어야하므로 3으로 나눠줍니다.
        i = i%3

    },100)

    //3초 후에 clearInterval을 호출하여 변경시키는 함수를 중지하도록 만들어준다.

    //3초 후에 게임 결과가 나와야한다.

    setTimeout(function(){

        clearInterval(changeImg)
    
        //컴퓨터가 랜덤하게 배열에서 가위,바위,보 중 하나를 선택합니다.

        const computer_choice = rock_paper_scissors[Math.floor(Math.random()*rock_paper_scissors.length)]

        //컴퓨터가 랜덤하게 선택한 이미지를 표시해줍니다.
    
        console.log(computer_choice)
    
        player2_choice.setAttribute('src',computer_choice)

        //게임 결과 구하기

        const player1 = 'paper'

        //경로 문자열 앞이 ./img/이고 뒤가 .png임을 이용해서 가위,바위,보 추출
        const player2 = computer_choice.slice(6,-4)

        const result = playGame(player1,player2)

        //score를 가져옵니다.
        //변경시켜야하므로 let으로 선언

        let player1_score = Number(count_player1.innerText)
        let player2_score = Number(count_player2.innerText)

        //결과에 따라 점수판 변경

        if (result == 1) {

            player1_score += 1

            //변경시킨 값을 다시 삽입
        //string으로 안바꿔도 알아서 되는데?

            count_player1.innerText = player1_score
            count_player2.innerText = player2_score
           
           //모달 내용 삽입
            modal_text.innerText = 'player1 의 승리입니다!'
          
           //모달 창의 display를 변경한다
           //css를 변경하거나 추가할때는.. (요소이름).style.(속성명) = value

           //flex로 하면 가운데에 뜨고, block으로 하면 맨 위로 뜬다
            modal.style.display = 'flex'
            //modal.style.transition = 'all 1s';
           
            //모달창을 클릭하면 사라지도록 합니다.
            modal.addEventListener('click',function(){
                modal.style.display = 'none'
            })



        } else if (result == 2){

            player2_score += 1

            //변경시킨 값을 다시 삽입

            count_player1.innerText = player1_score
            count_player2.innerText = player2_score

            //모달 내용 삽입
            modal_text.innerText ='player2의 승리입니다!'

            //모달 창의 display를 변경
            modal.style.display = 'flex'

            //모달창을 클릭하면 사라지도록 만든다.
            modal.addEventListener('click',function(){
                modal.style.display = 'none'
            })

        } else {

            //무승부이므로, 값을 변경하지않고 모달창만 변경

            modal_text.innerText = '무승부입니다!'

            //모달 창의 display를 변경

            modal.style.display = 'flex'

            //모달 창을 클릭하면 사라지도록 만든다

            modal.addEventListener('click',function(){
                modal.style.display = 'none'
            })

        }

        //버튼 disabled 속성을 제거하고, 게임을 다시 할 수있도록 만든다

        scissors_button.removeAttribute('disabled')
        rock_button.removeAttribute('disabled')
        paper_button.removeAttribute('disabled')
    
    
    
    },3000)


})