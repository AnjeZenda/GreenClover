<template>
  <main>
    <div class="event-list">
      <div class="row">
        <vHomeItem></vHomeItem>
        <vHomeItem></vHomeItem>
        <vHomeItem></vHomeItem>
        <vHomeItem></vHomeItem>
        <vHomeItem></vHomeItem>
        <vHomeItem></vHomeItem>
        <vHomeItem></vHomeItem>
        <vHomeItem></vHomeItem>
        <vHomeItem></vHomeItem>
      </div>
    </div>
  </main>
</template>

<script>
import vHomeItem from '../components/home/v-home-item.vue';

export default {
  name: 'Home',
  components: {
    vHomeItem
  }
}
</script>