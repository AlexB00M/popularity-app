<template>
    <transition name="slide-up">
        <div v-if="Visible" class="modal-item-card-store">
            <div class="modal-item-card-store-container">
                <div class="modal-item-card-store-content-top">
                    <div class="modal-item-card-store-content-top-text">{{ CardName }}</div> 
                    <button @click="close" class="modal-item-card-store-close-button">
                        <nuxt-icon name="closeModal"/>
                    </button>
                </div>
                <div class="modal-item-card-store-content-main">
                    <DotLottieVue class="modal-item-card-store-image" autoplay loop :src="CardImageUrl"/>
                    <div class="modal-item-card-store-content-main-data">
                        <ul class="modal-item-card-store-content-ul">
                            <li class="modal-item-card-store-content-li" :style="{ color: appStore.cardsConfig[CardName].levels['1'].color }">1 Lvl -> {{ appStore.cardsConfig[CardName].levels["1"].cardsCountUpLevel }}x</li>
                            <li class="modal-item-card-store-content-li" :style="{ color: appStore.cardsConfig[CardName].levels['2'].color }">2 Lvl -> {{ appStore.cardsConfig[CardName].levels["2"].cardsCountUpLevel }}x</li>
                            <li class="modal-item-card-store-content-li" :style="{ color: appStore.cardsConfig[CardName].levels['3'].color }">3 Lvl -> {{ appStore.cardsConfig[CardName].levels["3"].cardsCountUpLevel }}x</li>
                            <li class="modal-item-card-store-content-li" :style="{ color: appStore.cardsConfig[CardName].levels['4'].color }">4 Lvl -> {{ appStore.cardsConfig[CardName].levels["4"].cardsCountUpLevel }}x</li>
                            <li class="modal-item-card-store-content-li" :style="{ color: appStore.cardsConfig[CardName].levels['5'].color }">5 Lvl -> {{ appStore.cardsConfig[CardName].levels["5"].cardsCountUpLevel }}x</li>
                        </ul>
                    </div>
                </div>
                <div class="modal-item-card-store-content-bottom">
                </div>
            </div>
        </div>
    </transition>
</template>

<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue' 

const props = defineProps({
    Visible: Boolean,
    CardName: String,
    CardImageUrl: String
})

const itemStoreModalVisible = useState('itemStoreModalVisible', () => false)

watch(
  () => props.Visible,
  (newVal) => {
    itemStoreModalVisible.value = newVal
  }
)

const storeStore = useStoreStore()
const appStore = useAppStore()
const emit = defineEmits(['close'])

const close = () => {
    emit('close')
}

</script>

<style>

.modal-item-card-store-content-bottom-left {
    display: flex;
    gap: 10px;
    align-items: center;
}
.modal-item-card-store-content-ul {
  list-style-type: disc;
  padding-left: 20px;
}
.modal-item-card-store-content-li {
  margin-bottom: 8px;
}
.modal-item-card-store-image {
    width: 170px;
    height: 170px;
}
.modal-item-card-store-content-main {
    display: flex;
    gap: 20px;
}
.modal-item-card-store-content-top-text {
    font-weight: bold;
    font-size: 30px;
}
.modal-item-card-store-content-top {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-bottom: 10px;
}
.modal-item-card-store-close-button {
    font-size: 17px;
    color: var(--tg-theme-text-color);
}
.modal-item-card-store-container {
    padding-bottom: 10px;
}
.modal-item-card-store {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--tg-theme-bg-color);
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  padding: 13px 18px 13px 18px;
  box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.2);
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