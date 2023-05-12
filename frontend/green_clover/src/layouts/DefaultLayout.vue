<template>
    <header>
        <div class="container">
            <h2>
                Список мероприятий в Санкт-Петербурге
            </h2>
            <div class="header-filters">
                <div class="header-filters_item">
                    <vRangeFilter></vRangeFilter>
                </div>
                <div class="header-filters_item">
                    <vDateFilter></vDateFilter>
                </div>
                <div class="header-filters_item">
                    <vCheckboxFilter></vCheckboxFilter>
                </div>
            </div>
        </div>
    </header>
    <div class="container">
        <slot />
    </div>
</template>

<script>
import vRangeFilter from '../components/layouts/v-range-filter.vue';
import vDateFilter from '../components/layouts/v-date-filter.vue';
import vCheckboxFilter from '../components/layouts/v-checkbox-filter.vue'

export default {
    name: 'DefaultLayout',
    components: {
        vRangeFilter,
        vDateFilter,
        vCheckboxFilter
    }
}
</script>