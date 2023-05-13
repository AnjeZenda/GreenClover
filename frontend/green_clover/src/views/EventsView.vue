<template>
  <header>
    <div class="container">
      <h2>
        Список мест в Санкт-Петербурге
      </h2>
      <div class="header-filters" :class="isOpen ? 'act' : ''">
        <vFilterTitle></vFilterTitle>
        <div class="header-filters_item">
          <vAddressFilter></vAddressFilter>
        </div>
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
          <div class="header-filters_item-btn" @click="getList()">
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
          <vEventItem v-for="item in eventList" :key="item.place.id" :item="item"></vEventItem>
        </div>
        <div class="event-list_pagination" v-if="!isLoad">
          <div class="event-list_pagination-prev"
            @click="this.$router.push(`/events/${Number(this.$route.params.page) - 1}`), getList(Number(this.$route.params.page) - 1)"
            v-if="Number(this.$route.params.page) - 1 > 0">
            <img src="../assets/icons/arrow-prev.svg" alt="">
          </div>
          <div class="event-list_pagination-number__prev"
            @click="this.$router.push(`/events/${Number(this.$route.params.page) - 1}`), getList(Number(this.$route.params.page) - 1)"
            v-if="Number(this.$route.params.page) - 1 > 0">
            {{ Number(this.$route.params.page) - 1 }}
          </div>
          <div class="event-list_pagination-number__current">
            {{ this.$route.params.page }}
          </div>

          <div class="event-list_pagination-number__next"
            @click="this.$router.push(`/events/${Number(this.$route.params.page) + 1}`), getList(Number(this.$route.params.page) + 1)"
            v-if="Number($route.params.page) + 1 < totalPages">
            {{ Number($route.params.page) + 1 }}
          </div>

          <div class="event-list_pagination-number__dots" v-if="totalPages != $route.params.page">
            ...
          </div>

          <div class="event-list_pagination-number__last" v-if="totalPages != $route.params.page"
            @click="this.$router.push(`/events/${totalPages}`), getList(totalPages)">
            {{ totalPages }}
          </div>
          <div class="event-list_pagination-next"
            @click="this.$router.push(`/events/${Number(this.$route.params.page) + 1}`), getList(Number(this.$route.params.page) + 1)"
            v-if="Number($route.params.page) + 1 < totalPages">
            <img src="../assets/icons/arrow-next.svg" alt="">
          </div>
        </div>
      </div>
    </div>
  </main>
  <div class="loader" v-if="isLoad">loading</div>
</template>

<script>
import axios from 'axios';
import moment from 'moment'

import vEventItem from '../components/event/v-event-item.vue';
import vRangeFilter from '../components/header/v-range-filter.vue';
import vDateFilter from '../components/header/v-date-filter.vue';
import vCheckboxFilter from '../components/header/v-checkbox-filter.vue'
import vFilterTitle from '../components/header/v-filter-title.vue';
import vAddressFilter from '../components/header/v-address-filter.vue';

export default {
  name: 'Home',
  components: {
    vEventItem,
    vRangeFilter,
    vDateFilter,
    vCheckboxFilter,
    vFilterTitle,
    vAddressFilter
  },
  data() {
    return {
      params: {
        km: 5,
        dates: moment().format('YYYY-MM-DD'),
        isFree: false,
        address: '',
        page: this.$route.params.page
      },
      isOpen: false,
      eventList: [],
      isLoad: true,
      totalPages: 0
    }
  },
  methods: {
    getList(page = 0) {
      this.isOpen = false
      this.isLoad = true
      this.eventList = []
      this.params.dates = moment(this.params.dates).format('YYYY-MM-DD')
      if(page != 0) this.params.page = page
      axios.post('http://127.0.0.1:8000/events/', this.params)
        .then((res) => {
          this.isLoad = false
          this.eventList = res.data.data.data
          this.totalPages = Math.ceil(res.data.data.count / 12)
        });
    }
  },
  mounted() {
    this.$nextTick(function () {
      this.getList();
    })
  }
}
</script>