<template>
    <div class="header-filters_item-range">
        <div class="header-filters_item-range__title" @click="isOpen = !isOpen">
            Растояние от центра <img src="../../assets/icons/arrow-up.svg" alt="">
        </div>
        <div class="header-filters_item-range__body" v-if="isOpen">
            <Slider v-model="filterKm" :format="{ suffix: ' км', decimals: 0 }" :max="10" :min="1" :step="1" />
            <div class="header-filters_item-range__body-diapason">
                <span>
                    1км
                </span>
                <span>
                    10км
                </span>
            </div>
            <!--   <div class="header-filters_item-range__body-text">
            <input type="text" placeholder="Не более 10 км" v-model="filterKm">
            </div> -->
        </div>
    </div>
</template>

<script>
import Slider from '@vueform/slider'

export default {
    name: 'v-range-filter',
    components: {
        Slider,
    },
    data() {
        return {
            isOpen: false,
            filterKm: 5,
        }
    },
}
</script>

<style src="@vueform/slider/themes/default.css"></style>