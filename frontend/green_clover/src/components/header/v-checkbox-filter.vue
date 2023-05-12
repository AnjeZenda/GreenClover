<template>
    <div class="header-filters_item-checkbox">
        <input type="checkbox" id="free" v-model="$parent.params.isFree">
        <label for="free">Бесплатное событие</label>
    </div>
</template>

<script>
export default {
    name: 'v-checkbox-filter',
}
</script>
