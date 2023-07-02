<template>
    <div class="sidebar">
    <router-link to="/"><h3 class="mt-4 mx-5">모든</h3></router-link>
    <router-link to="/today"><h3>오늘</h3></router-link>
    <router-link to="/important"><h3>중요</h3></router-link>
    </div>
    
</template>

<style>
.sidebar {
  border:1px solid black;
  border-radius:10px;
}

a {
    text-decoration: none;
}
</style>