// App.vue

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  created: function () {
		// 이곳에 들어갈 코드를 작성하시오.
    const token = localStorage.getItem("jwt")
    if (token) {
      this.isLogin=true;
    } else {
      this.isLogin=false;
    }
  },
}
