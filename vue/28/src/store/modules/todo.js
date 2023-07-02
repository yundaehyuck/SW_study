const state = () => {
    return {
          // todo 리스트 Array
      list: [
              // 개별 todo Object
        {
          id: 1638771553377,                // nowDateObj.getTime()
          content: 'Vue',                   // Todo 내용
          dueDateTime: '2021-12-09T00:00',  // 마감일
          isCompleted: false,               // 완료된 할 일
          isImportant: true,				        // 중요 할 일
        },
        {
          id: 1638771553378,
          content: 'Vue Router',
          dueDateTime: '2021-12-10T00:00',
          isCompleted: false,
          isImportant: true,
        },
        {
          id: 16387715533779,
          content: 'Vuex',
          dueDateTime: '2021-12-11T00:00',
          isCompleted: true,
          isImportant: false,
        },
      ],
    }
  }

  const mutations = {
    ADD_TO_DO(state,text) {
    
    const createDay = Date.now()

    let today = new Date();

    let year = today.getFullYear()
    let month = today.getMonth() + 1
    let date = today.getDate() + 1

    let due = year + '-' + month + '-' + date + 'T00:00' 



    const newToDo = {}
    
    newToDo.id = createDay
    newToDo.content = text
    newToDo.dueDateTime = due
    newToDo.isCompleted = false
    newToDo.isImportant = false

    state.list.push(newToDo)

    }
  }
  const actions = {
    addTodo(context,text) {
        context.commit('ADD_TO_DO',text)
    }
  }
  const getters = {}

  export default {

    namespaced:true,

    state: state,
    mutations: mutations,
    actions: actions,
    getters: getters,
  }