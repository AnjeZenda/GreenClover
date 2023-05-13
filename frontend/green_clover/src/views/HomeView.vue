<template>
    <header>
        <div class="container d-flex justify-content-between">
            <div class="header-logo">
                <img src="../assets/img/logo.svg" alt="">
            </div>
            <nav class="header-menu">
                <ul>
                    <li><router-link to="/">Главная</router-link></li>
                    <li><router-link to="/events/1">Список мест</router-link></li>
                </ul>
            </nav>
        </div>
    </header>
    <main class="home">
        <div class="container">
            <vMainBaner></vMainBaner>
            <vMainUsage></vMainUsage>
        </div>
    </main>
</template>

<script>
import vMainBaner from '../components/home/v-main-baner.vue';
import vMainUsage from '../components/home/v-main-usage.vue';

export default {
    name: 'Home',
    components: {
        vMainBaner,
        vMainUsage
    }
}
</script>