<template>
    <div class="col-lg-3">
        <div class="event-list_item">
            <div class="event-list_item-img" v-if="!item.images">
                <img src="../../assets/img/no-image.jpg" alt="">
            </div>
            <div class="event-list_item-img" v-else-if="item.images.length == 1">
                <img :src="item.images[0].image" alt="">
            </div>
            <div class="event-list_item-img" v-else>
                <carousel :items-to-show="1">
                    <slide v-for="img in item.images" :key="img">
                        <img :src="img.image" alt="">
                    </slide>

                    <template #addons>
                        <navigation />
                        <pagination />
                    </template>
                </carousel>
            </div>
            <div class="event-list_item-title">
                {{ item.title }}
            </div>
            <div class="event-list_item-description">
                {{ item.description }}
            </div>
            <div class="event-list_item-number" v-if="item.place.phone">
                <span>
                    Телефон:
                </span>
                <span>
                    {{ item.place.phone }}
                </span>
            </div>
            <div class="event-list_item-address">
                {{ item.place.address }}
            </div>
            <div class="event-list_item-metro" v-if="item.place.subway">
                <div :style="'background: #' + item.subway_info[0].data.color"></div>
                ст.м. {{ item.place.subway }} ({{ item.subway_time }} мин)
            </div>
            <div class="event-list_item-btn" @click="isOpen = true">
                Подробнее
            </div>
        </div>
    </div>
    <vEventMoreInfo v-if="isOpen" :item="item"></vEventMoreInfo>
</template>

<script>
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'

import vEventMoreInfo from './v-event-more-info.vue';

export default {
    name: 'v-home-item',
    props: ['item'],
    data() {
        return {
            isOpen: false
        }
    },
    components: {
        Carousel,
        Slide,
        Pagination,
        Navigation,
        vEventMoreInfo
    },
}
</script>