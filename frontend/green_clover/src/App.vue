<template>
  <default-layout>
    <RouterView />
  </default-layout>
</template>

<script>
import DefaultLayout from './layouts/DefaultLayout.vue';
import { RouterView } from 'vue-router'

export default {
  name: 'App',
  components: {
    DefaultLayout,
  },
}

</script>

