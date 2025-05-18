<template>
    <div class="rulette-card-container" :style="themeStore.colorTheme === 'dark' ? { backgroundColor: 'var(--tg-theme-secondary-bg-color)' } : {}">
        <div class="rulette-card-data">
            <div class="rulette-card-data-params" :style="{ color: appStore.colorTotal }">
                <!-- +{{ appStore.cardsConfig[Name].pointsPerOne }}<nuxt-icon name="fire"/> -->
                 <!-- {{ Index }} -->
            </div>
            <DotLottieVue class="rulette-card-image" autoplay loop :src="appStore.cardsConfig[Name].url"/> 
        </div> 
        <div class="rulette-card-cost-container"> 
            <div class="rulette-card-cost">
                <nuxt-icon class="rulette-card-star-icon" name="telegramStar"/>
                <div class="rulette-card-text">
                    {{ appStore.cardsConfig[Name].cost }}
                </div>
            </div>  
        </div>
    </div>
</template>

<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue' 

const appStore = useAppStore()
const themeStore = useThemeStore()

const props = defineProps({
    Name: String,
    Index: Number
})

</script>

<style>
.rulette-card-cost {
    display: flex;
    align-items: center;
    gap: 4px;
    background-color: #f0b40029;
    border-radius: 20px;
    padding: 2px 6px 2px 6px;
}
.rulette-card-text {
    font-size: 10px;
    font-weight: bold;
    color: #ad8603;
}
.rulette-card-star-icon {
    font-size: 16px;
    color: var(--telegram-star-color);
}
.rulette-card-cost-container {
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    height: 25px;
}
.rulette-card-data {
    border-radius: 10px;
    margin-bottom: 5px;
}
.rulette-card-data-params {
    padding-top: 5px;
    font-size: 13px;
    font-weight: bold;
    text-align: center;
}
.rulette-card-image {
    height: 100px;
    top: 0;
}
.rulette-card-container {
    width: 100px;
    padding: 5px;
    border-radius: 10px;
    box-shadow: 0 0px 12px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: center;
    flex-direction: column;
}
</style>