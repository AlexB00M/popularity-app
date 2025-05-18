<template>
    <div class="item-win-container">
        <div class="item-win-data">
            <div class="item-win-data-params" :style="{ color: appStore.colorTotal }">
                <!-- +{{ appStore.cardsConfig[Name].pointsPerOne }}<nuxt-icon name="fire"/> -->
            </div>
            <DotLottieVue class="item-win-image" autoplay loop :src="appStore.cardsConfig[Name].url"/> 
        </div> 
    </div>
</template>

<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue' 

const appStore = useAppStore()

const props = defineProps({
  Name: String,
})

</script>

<style>
.item-win-buy-button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.item-win-data {
  border-radius: 10px;
  margin-bottom: 5px;
}
.item-win-data-params {
  padding-top: 5px;
  font-size: 13px;
  font-weight: bold;
  text-align: center;
}
.item-win-image {
  width: 250px;
  height: 250px;
}
.item-win-container {
  width: 250px;
  height: 250px;
  padding: 5px;
  border-radius: 10px;

}
</style>