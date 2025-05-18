<template>
    <transition name="slide-up">
        <div v-if="Visible" class="modal-item-card">
            <div class="modal-item-card-top-container">
                <div class="modal-item-card-top-container">
                    <div class="modal-item-card-top-text">
                        {{ CardName }}
                    </div>
                    <button @click="close" class="modal-item-card-close-button">
                        <nuxt-icon name="closeModal"/>
                    </button>
                </div>
            </div>
            <div class="modal-item-card-main-container">
                <ProfileCardHistory v-for="(card, index) in cardHistory"
                :key="index"
                :UserNameFrom="card.userNameFrom"
                :UserFromPhotoUrl="card.photoUrl"
                :Data="card.data"
                :Count="Number(card.count)"
                :PointsPerOne="Number(appStore.cardsConfig[CardName].pointsPerOne)"
                />
            </div>
        </div>
    </transition>
</template>

<script setup>
import cardHistory from '~/assets/dataTest/cardCarHistory.json'
//Вместо этого запрос к БД по https://api/userId/ и парметры cardName или id

defineProps({
    Visible: Boolean,
    CardName: String,
})

const storeStore = useStoreStore()
const appStore = useAppStore()
const emit = defineEmits(['close'])

const close = () => {
    emit('close')
}

</script>

<style>
.modal-item-card-main-container {
    display: flex;
    flex-direction: column;
    gap: 10px
}
.modal-item-card-top-text {
    font-weight: bold;
    font-size: 30px;
}
.modal-item-card-close-button {
    font-size: 17px;
    color: var(--tg-theme-text-color);
}
.modal-item-card-top-container {
    display: flex;
    justify-content: space-between;
    width: 100%;
    padding-bottom: 5px;
}
.modal-item-card {
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
  height: 50vh;
}


.slide-up-enter-active, .slide-up-leave-active {
  transition: transform 0.3s ease, opacity 0.3s ease;
}
.slide-up-enter-from, .slide-up-leave-to {
  transform: translateY(100%);
  opacity: 0;
}
</style>