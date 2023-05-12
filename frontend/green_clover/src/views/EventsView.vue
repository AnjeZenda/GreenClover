<template>
  <header>
    <div class="container">
      <h2>
        Список мест в Санкт-Петербурге
      </h2>
      <div class="header-filters" :class="isOpen ? 'act' : ''">
        <vFilterTitle></vFilterTitle>
        <div class="header-filters_item">
          <vRangeFilter></vRangeFilter>
        </div>
        <div class="header-filters_item">
          <vDateFilter></vDateFilter>
        </div>
        <div class="header-filters_item">
          <vCheckboxFilter></vCheckboxFilter>
        </div>
        <div class="header-filters_item">
          <div class="header-filters_item-btn" @click="send()">
            Применить фильтры
          </div>
        </div>
      </div>
      <div class="filters-open" @click="isOpen = true">
        Фильтры <img src="../assets/icons/options.svg" alt="">
      </div>
    </div>
  </header>
  <main>
    <div class="container">
      <div class="event-list">
        <div class="row">
          <vEventItem></vEventItem>
          <vEventItem></vEventItem>
          <vEventItem></vEventItem>
          <vEventItem></vEventItem>
          <vEventItem></vEventItem>
          <vEventItem></vEventItem>
          <vEventItem></vEventItem>
          <vEventItem></vEventItem>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import axios from 'axios';
import vEventItem from '../components/event/v-event-item.vue';
import vRangeFilter from '../components/header/v-range-filter.vue';
import vDateFilter from '../components/header/v-date-filter.vue';
import vCheckboxFilter from '../components/header/v-checkbox-filter.vue'
import vFilterTitle from '../components/header/v-filter-title.vue';

export default {
  name: 'Home',
  components: {
    vEventItem,
    vRangeFilter,
    vDateFilter,
    vCheckboxFilter,
    vFilterTitle
  },
  data() {
    return {
      params: {
        km: 5,
        dates: { start: new Date(), end: new Date(Date.now() + 1000 * 60 * 60 * 24) },
        isFree: false
      },
      isOpen: false,
    }
  },
  methods: {
    send() {
      this.isOpen = false
      console.log(this.params)
    },
    test() {
      axios.post('http://127.0.0.1:8000/info/', {
        test1: 123
      })
        .then((res) => {
          console.log(res)
        });
    }
  },
  mounted() {
    this.$nextTick(function () {
      this.test();
    })
  }
}
</script>