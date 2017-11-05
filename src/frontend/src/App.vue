<template>
  <div>
    <Pnav></Pnav>
  </div>
    
</template>

<script>
import Pnav from './components/navigation/Pnav';


export default {
  name: 'app',
  components: {
    Pnav,
  },
};
</script>

<style>

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
