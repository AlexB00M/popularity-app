<template>
    <div class="main">
        <div class="header">
            <div class="headertop"></div>
            <div class="headerbottom"> 
                <span v-if="!userStore.desktop" class="header-text">
                    <!-- <div v-if="route.fullPath === '/'" class="user-stars-balance-container">
                        <div class="user-stars-balance-text">
                            {{ storeStore.userStarsBalance }}
                        </div>
                        <nuxt-icon :style="{ color: appStore.colorTotal }" name="fire"/>
                    </div>
                    <div v-else>{{ label }}</div> -->
                    {{ header_lable }}
                </span> 
            </div>
        </div>
        <div class="safe-area" :class="{ winVisible: winModalVisible}">
            <div class="container" :class="{ 'no-main-button': !isAnyCard, 'main-button': isAnyCard }"> 
                <nuxt keep-alive />
                <slot></slot>
            </div>
        </div>
        <BottomMenu v-if="!isAnyCard && !winVisible" class="bottom-menu"/>
    </div>
    <ModalBuyStars />
</template>
  
<script setup>

const header_lable = ref('Default')
const route = useRoute()

watch(
  () => route.fullPath,
  (newPath) => {
  },
  { immediate: true }
)

const userStore = useUserStore()
const storeStore = useStoreStore()
const appStore = useAppStore()

const winVisible = useState('winVisible')
const winModalVisible = useState('winModalVisible')
const itemStoreModalVisible = useState('itemStoreModalVisible')
const buyStarsModalVisible = useState('buyStarsModalVisible')
buyStarsModalVisible.value = true

const isAnyCard = useState('isAnyCard', () => 
  computed(() => {
    return Object.values(storeStore.storeBuyCards).some(card => card.count > 0)
  })
)

watchEffect(() => {
    header_lable.value = getRouteName()
})
onMounted(() => {
    header_lable.value = getRouteName()
})
</script>

<style>
.safe-area.winVisible {
    overflow-y: hidden;
}
.main-button {
    padding-bottom: 25px;
}
.no-main-button::after {
    content: "";
    height: var(--bottom-menu-height);
    display: block;
}
.user-stars-balance-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 4px;
}
.headerbottom{
    display: flex;
    align-items: center;
    justify-content: center;
}
.header-text {
    font-weight: bold;
    font-size: 18px;
}


</style>
  