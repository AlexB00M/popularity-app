<template>
    <transition name="slide-up">
        <div v-if="buyStarsModalVisible" class="modal-buy-stars" :style="themeStore.colorTheme === 'dark' ? { backgroundColor: 'var(--tg-theme-secondary-bg-color)' } : {}">
            <div class="modal-stars-items-container">
                <div class="modal-stars-item" :class="{ active: activeItem === '100' }" @click="itemClick('100')">
                    <div class="modal-stars-item-image-container">
                        <DotLottieVue class="modal-stars-item-image" style="width: 50px; height: 50px;" autoplay loop speed="1" :src="'https://lottie.host/2684cdee-17c3-4833-b3b0-2c0418fbcb80/kWsD4Xalzr.lottie'"/>
                    </div>
                    <div class="modal-stars-item-text-container">
                        <nuxt-icon name="telegramStar" style="color: var(--telegram-star-color);"/>
                        <div class="modal-stars-item-text" style="color: #ad8603;">
                            100 
                        </div>
                    </div>
                </div>
                <div class="modal-stars-item" :class="{ active: activeItem === '200' }" @click="itemClick('200')">
                    <div class="modal-stars-item-image-container">
                        <DotLottieVue class="modal-stars-item-image" style="width: 65px; height: 65px;" autoplay loop speed="1" :src="'https://lottie.host/2684cdee-17c3-4833-b3b0-2c0418fbcb80/kWsD4Xalzr.lottie'"/>
                    </div>
                    <div class="modal-stars-item-text-container">
                        <nuxt-icon name="telegramStar" style="color: var(--telegram-star-color);"/>
                        <div class="modal-stars-item-text" style="color: #ad8603;">
                            200 
                        </div>
                    </div>
                </div>
                <div class="modal-stars-item" :class="{ active: activeItem === '500' }" @click="itemClick('500')">
                    <div class="modal-stars-item-image-container">
                        <DotLottieVue class="modal-stars-item-image" style="width: 80px; height: 80px;" autoplay loop speed="1" :src="'https://lottie.host/2684cdee-17c3-4833-b3b0-2c0418fbcb80/kWsD4Xalzr.lottie'"/>
                    </div>
                    <div class="modal-stars-item-text-container">
                        <nuxt-icon name="telegramStar" style="color: var(--telegram-star-color);"/>
                        <div class="modal-stars-item-text" style="color: #ad8603;">
                            500
                        </div>
                    </div>
                </div>
                <div class="modal-stars-item" :class="{ active: activeItem === '1000' }" @click="itemClick('1000')">
                    <div class="modal-stars-item-image-container">
                        <DotLottieVue class="modal-stars-item-image" style="width: 105px; height: 105px;" autoplay loop speed="1" :src="'https://lottie.host/2684cdee-17c3-4833-b3b0-2c0418fbcb80/kWsD4Xalzr.lottie'"/>
                    </div>
                    <div class="modal-stars-item-text-container">
                        <nuxt-icon name="telegramStar" style="color: var(--telegram-star-color);"/>
                        <div class="modal-stars-item-text" style="color: #ad8603;">
                            1000 
                        </div>
                    </div>
                </div>
                <div class="modal-stars-item" :class="{ active: activeItem === '4000' }" @click="itemClick('4000')">
                    <div class="modal-stars-item-image-container">
                        <DotLottieVue class="modal-stars-item-image" style="width: 120px; height: 120px;" autoplay loop speed="1" :src="'https://lottie.host/2684cdee-17c3-4833-b3b0-2c0418fbcb80/kWsD4Xalzr.lottie'"/>
                    </div>
                    <div class="modal-stars-item-text-container">
                        <nuxt-icon name="telegramStar" style="color: var(--telegram-star-color);"/>
                        <div class="modal-stars-item-text" style="color: #ad8603;">
                            4000 
                        </div>
                    </div>
                </div>
                <div class="modal-stars-item" :class="{ active: activeItem === '10000' }" @click="itemClick('10000')">
                    <div class="modal-stars-item-image-container">
                        <DotLottieVue class="modal-stars-item-image" style="width: 135px; height: 135px;" autoplay loop speed="1" :src="'https://lottie.host/2684cdee-17c3-4833-b3b0-2c0418fbcb80/kWsD4Xalzr.lottie'"/>
                    </div>
                    <div class="modal-stars-item-text-container">
                        <nuxt-icon name="telegramStar" style="color: var(--telegram-star-color);"/>
                        <div class="modal-stars-item-text" style="color: #ad8603;">
                            10000 
                        </div>
                    </div>
                </div>
            </div>
            <MainButton v-if="mainButtonVisible" :text="`Buy ${activeItem} Stars`" :hasShineEffect="true"/>
        </div>
    </transition>
</template>

<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue' 
import { useSecondaryButton, MainButton } from 'vue-tg'

const secondaryButton = useSecondaryButton()
secondaryButton.hasShineEffect.value = true

const buyStarsModalVisible = useState('buyStarsModalVisible')
buyStarsModalVisible.value = false

const mainButtonVisible = ref(false)
const activeItem = ref('')
const itemCoutClicks = ref(0)

const themeStore = useThemeStore()

const isBuyingStars = useState('isBuyingStars')

const itemClick = (itemName) => {
    if (activeItem.value === itemName){
        itemCoutClicks.value += 1
    } else {
        itemCoutClicks.value = 1
    }
    activeItem.value = itemName
}

watchEffect(() => {
    if (activeItem.value != ''){
        mainButtonVisible.value = true
    }
    if (itemCoutClicks.value === 2) {
        itemCoutClicks.value = 0
        activeItem.value = ''
        mainButtonVisible.value = false
    }
})
watchEffect(() => {
    if (buyStarsModalVisible.value) {
        isBuyingStars.value = true
        secondaryButton.show();
    } else {
        isBuyingStars.value = false
        secondaryButton.hide();
    }
});

secondaryButton.onClick(() => {
    buyStarsModalVisible.value = false
    activeItem.value = ''
    itemCoutClicks.value = 0
    mainButtonVisible.value = false
})
</script>

<style>
.modal-stars-item.active {
    outline: 1px solid blue;
}
.modal-stars-item-text {
    font-size: 12px;
    font-weight: bold;
}
.modal-stars-item-text-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 3px;
    background-color: #f7b90085;
    width: 100%;
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 10px;
}
.modal-stars-item {
    box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    /* overflow: hidden; */
}
.modal-stars-item-image {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}
.modal-stars-item-image-container {
    width: 80px;
    height: 80px;
    position: relative;
    overflow: hidden;
    border-top-right-radius: 5px;
    border-top-left-radius: 5px;
    /* background-image: 
    linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)),
    url('~/assets/images/backGroundStars2.webp'); 

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat; */
    }
.modal-stars-items-container {
    display: flex;
    align-items: flex-start;
    gap: 15px;
    height: 100%;
    overflow-y: scroll;
    padding: 15px;
}
.modal-buy-stars {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--tg-theme-bg-color);
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  /* padding: 15px 0px 15px 0px; */
  box-shadow: 0 -4px 10px rgba(0, 0, 0, 0.1);
  z-index: 300;
}


.slide-up-enter-active, .slide-up-leave-active {
  transition: transform 0.3s ease, opacity 0.3s ease;
}
.slide-up-enter-from, .slide-up-leave-to {
  transform: translateY(100%);
  opacity: 0;
}
</style>