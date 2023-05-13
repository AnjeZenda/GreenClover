<template>
    <input type="text" placeholder="Введите свой адрес" class="filter-adress" v-model="$parent.params.address"
        @keyup="onPress($parent.params.address)">
    <div class="header-filters_item-address" v-if="addressList.length != 0 && $parent.params.address != ''">
        <div class="header-filters_item-address__item" v-for="item in addressList" :key="item.value">
            <div @click="setAddress(item.value)">
                {{ item.value }}
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'v-address-filter',
    data() {
        return {
            addressList: []
        }
    },
    methods: {
        setAddress(data) {
            this.addressList = []
            this.$parent.params.address = data
        },
        onPress(e) {
            let addess = 'Санкт-Петербург ' + e;
            axios.post('https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address', {
                query: addess
            },
                {
                    headers: {
                        "Content-Type": "application/json",
                        "Accept": "application/json",
                        "Authorization": "Token 353a3d637266d50552f4534af4a839d507e6f5e5"
                    }
                },)
                .then((res) => {
                    this.addressList = res.data.suggestions
                });
        }
    }
}
</script>