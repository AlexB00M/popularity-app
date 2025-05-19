<template>
    <div class="tasks-container">
        <div class="tasks-top-section">
            <DotLottieVue class="tasks-image" autoplay loop :src="'https://lottie.host/62d79c4e-a4f0-42b1-a20f-8a5d2b1881fb/G3MYM2qdHv.lottie'"/>
            <span class="tasks-top-section-text">Tasks</span>
            <span class="tasks-top-section-text-sub">Complite tasks and get gifts.</span>
        </div>
        <div v-if="tasks.length === 0" class="tasks-main-section">
            <div class="tasks-main-section-data">
                <DotLottieVue class="tasks-image" autoplay :src="'https://lottie.host/b2e5418e-42fc-4fe8-89de-b1658e340799/QYDAtddDXB.lottie'"/>
                <div class="tasks-main-section-data-text">
                    Tasks will be available soon.
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'

const tasks = ref([])

</script>

<style> 
.tasks-container {
    display: flex;
    flex-direction: column;
    gap: 15px
}
.tasks-main-section {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 350px;
    background-color: var(--tg-theme-secondary-bg-color);
    border-radius: 10px;
    margin: 10px;
}
.tasks-main-section-data {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.tasks-main-section-data-text {
    color: var(--tg-theme-subtitle-text-color)
}
.tasks-top-section-text-sub {
  text-align: center;
  font-size: 14px;
  font-weight: 500;
  color: var(--tg-theme-subtitle-text-color);
}
.tasks-top-section-text {
  font-size: 20px;
  font-weight: bold;
}
.tasks-top-section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 7px;
}
.tasks-image {
  width: 100px;
  height: 100px;
}
</style>