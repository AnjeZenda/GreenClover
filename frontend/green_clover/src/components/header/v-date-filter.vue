<template>
    <div class="header-filters_item-date">
        <div class="header-filters_item-date__title" @click="isOpen = !isOpen">
            Дата начала: <img src="../../assets/icons/calendar.svg" alt="">
        </div>
        <div class="header-filters_item-date__body" :class="(isOpen) ? 'act' : ''">
            <DatePicker v-model="$parent.params.dates" :color="selectedColor"></DatePicker>
        </div>
    </div>
</template>

<script>
import { DatePicker } from 'v-calendar';
import 'v-calendar/style.css';

export default {
    name: 'v-date-filter',
    data() {
        return {
            isOpen: false,
            selectedColor: 'green'
        }
    },
    components: {
        DatePicker
    }
}
</script>
