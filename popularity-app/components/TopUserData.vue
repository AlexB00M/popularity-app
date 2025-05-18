<template>
    <div class="top-user-data-container">
        <div class="top-user-data-left" @click="clicked">
            <img class="top-user-data-left-user-photo" :src="userStore.dataUnsafe.user.photo_url"/>
            <div class="top-user-data-left-text">
                {{ userStore.dataUnsafe.user.username }}
            </div>
        </div>
        <div class="top-user-data-right" @click="upBalanceClicked">
            <div class="top-user-data-right-text">
                {{ storeStore.userStarsBalance }}
            </div>
            <nuxt-icon class="top-user-data-right-star-icon" name="telegramStar" style="color: #ffc400;"/>
        </div>
    </div>
</template>

<script setup>

const router = useRouter()

const userStore = useUserStore()
const storeStore = useStoreStore()

const buyStarsModalVisible = useState('buyStarsModalVisible')
const isSpining = useState('isSpining')

const upBalanceClicked = () => {
    if (isSpining.value) return
    buyStarsModalVisible.value = true
}

const clicked = () => {
    if (isSpining.value) return
    if (buyStarsModalVisible.value) return
    
    router.push('/profile')
}
</script>

<style>
.top-user-data-right-text {
    font-weight: 700;
    font-size: 15px;
}
.top-user-data-right {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 5px;
}
.top-user-data-left-text {
    font-size: 15px;
    font-weight: bold;
    color: var(--tg-theme-text-color);
}
.top-user-data-container{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: var(--tg-theme-section-bg-color);
    border-radius: 10px;
    padding: 7px;
    box-shadow: 0 0px 12px rgba(0, 0, 0, 0.1);
    position: sticky;
    top: 5px;
    z-index: 1000;
}
.top-user-data-left {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    text-decoration: none;
}
.top-user-data-left-user-photo {
    width: 35px;
    height: 35px;
    border-radius: 50%;
    border: 1px solid white;
}
</style>