<template>
    <section class="main-baner">
        <div class="row d-flex align-items-center">
            <div class="col-8">
                <div class="main-baner_text">
                    <h1>
                        Green Clover
                    </h1>
                    <p>
                        Мы предоставляем актуальный список мест и мероприятий, которые будет приятно посетить
                        каждому
                        туристу
                    </p>
                </div>
                <div class="main-baner_btn">
                    <router-link to="/events/1">Просмотреть</router-link>
                </div>
            </div>
            <div class="col-4">
                <div class="main-baner_img">
                    <img src="../../assets/img/clover.jpg" alt="">
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: "v-main-baner"
}
</script>