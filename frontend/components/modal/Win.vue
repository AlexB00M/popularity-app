<template>
    <transition name="slide-up">
        <div v-if="Visible" class="modal-win-container">
          <div class="modal-win">
            <StoreItemWin v-if="CardName !== ''" :Name="CardName"/>
            <div class="modal-win-text">
              You've won a gift!
            </div>
          </div>
          <DotLottieVue class="congrats" autoplay loop :src="'https://lottie.host/db91afd4-43ef-4e8b-b29b-717b05889e1e/lp26500WBR.lottie'"/> 
        </div>
    </transition>
    <MainButton v-if="Visible" :text="`Clime`" :hasShineEffect="true" @click="close"/>
</template>

<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue' 
import { MainButton } from 'vue-tg'

const props = defineProps({
  Visible: Boolean,
  CardName: String,
})

const winModalVisible = useState('winModalVisible', () => false)

watch(
  () => props.Visible,
  (newVal) => {
    winModalVisible.value = newVal
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
.congrats {
  position: absolute;
  height: 100vh;
  width: 100vh;
}
.modal-win-text {
  font-weight: 600;
  font-size: 24px;
}
.modal-win {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.modal-win-container{
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  backdrop-filter: blur(5px); 
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  z-index: 2000;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;

}

.slide-up-enter-active, .slide-up-leave-active {
  transition: transform 0.3s ease, opacity 0.3s ease;
}
.slide-up-enter-from, .slide-up-leave-to {
  transform: translateY(100%);
  opacity: 0;
}
</style>