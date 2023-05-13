<template>
    <div class="col-lg-3">
        <div class="event-list_item">
            <div class="event-list_item-img">
                <img src="../../assets/img/event_image.jpg" alt="">
            </div>
            <div class="event-list_item-title">
                {{ item.title }}
            </div>
            <div class="event-list_item-description">
                {{ item.description }}
            </div>
            <div class="event-list_item-number">
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
                ст.м. {{ item.place.subway }} (5 минут)
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'v-home-item',
    props: ['item']
}
</script>