// 1번
const nums = [1,2,3,4,5,6,7,8]

// const는 재할당이 불가능한데, i++로 인해 i의 값을 재할당해서, 에러남
// 재할당이 가능한 let으로 고친다
//for (const i = 0; i < nums.length; i++) {
for (let i = 0; i < nums.length; i++){
  console.log()
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

// 2번

//in은 속성의 이름으로 순회하므로
//속성의 실제 값으로 순회하는 of를 사용하는게 적절하다.
//for (num in nums) {
for (num of nums){
  console.log(num, typeof num)
}

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string

/*
1 number
2 number
3 number
4 number
5 number
6 number
7 number
8 number
*/
