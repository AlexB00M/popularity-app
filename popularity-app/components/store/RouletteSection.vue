<template>
    <div class="section-container bg">
        <div class="section-lable"></div>
        <div class="roulette-wrapper-container" style="position: relative;">
            <div class="rulette-line-container">
                <div class="rulette-line"></div>
            </div>
            <nuxt-icon class="rulette-poiner-bottom" name="triangle-bottom"/>
            <nuxt-icon class="rulette-poiner-top" name="triangle-top"/>
            <div class="roulette-wrapper">
                <div class="roulette-inner" @transitionend="onSpinEnd">
                    <StoreItemRoulette style="width: 100px; flex-shrink: 0;"
                        v-for="(item, index) in items"
                        :key="item + '-' + index"
                        :Name="item"
                        :Index="index"
                    />
                </div>
            </div>
        </div>
        <div class="rulette-bottom-container">
            <button class="rulette-spin-button" @click="spin" :style="!isAvailibleSpin ? { background: '#3d5b7a', color: 'rgb(150, 150, 150)' } : {background: `var(--tg-theme-button-color)`}">
                <div class="rulette-spin-button-text">
                    Spin
                </div>
                <div class="rulette-spin-button-cost-container">
                    <div class="rulette-spin-button-cost">
                        100
                    </div>
                    <nuxt-icon class="store-item-card-star-icon" name="telegramStar" :style="!isAvailibleSpin ? {color: '#977400'} : {color: '#ffc400'}"/>
                </div>
            </button>
        </div>
    </div>
    <ModalWin :Visible="winVisible" :CardName="itemWin" @close="closeWin"/>
</template>

<script setup>

const isSpining = useState('isSpining')
const winVisible = useState("winVisible")
const isBuying = useState('isBuying')
const isBuyingStars = useState('isBuyingStars')

const cells = 31
const isAvailibleSpin = ref(true)
const items = ref([])
const itemWin = ref('')

const appStore = useAppStore()
const themeStore = useThemeStore()

const cardsConfig = appStore.cardsConfig
const cardConfigSorted = appStore.sortConfigAsc(cardsConfig)

const closeWin = () => {
    winVisible.value = false 
}

const spin = () => {
    if (isBuyingStars.value) return
    if (isBuying.value) return
    if (!isAvailibleSpin.value) return

    items.value = generateItems()
    console.log(items.value)
    const randomNonce = Math.floor(Math.random() * 81) - 10; //[-10px, +70px]

    const rulette = document.querySelector('.roulette-inner')
    rulette.style.transition = 'none'
    rulette.style.transform = 'translate3d(0, 0, 0)'
    rulette.offsetHeight 

    rulette.style.transition = 'transform 5s cubic-bezier(.21, .53, .29, .99)'
    setTimeout(() => {
        rulette.style.left = '50%'
        rulette.style.transform = `translate3d(calc(-80% + ${randomNonce}px), 0, 0)`
    }, 0)
    
    itemWin.value = items.value[24]

    console.log("spin", itemWin)

    isAvailibleSpin.value = false
    isSpining.value = true
}

const onSpinEnd = () => {
  isAvailibleSpin.value = true
  isSpining.value = false
  winVisible.value = true
}

const getItem = () => {
    const chance = Math.floor(Math.random() * 100000)
    let item;
    
    while (!item) {
        for(let name in cardConfigSorted){
            if (chance < Number(cardConfigSorted[name].chance*1000)) {
                item = name
                break
            }
        }
    }
    return item
}

const generateItems = () => {
    let generatedList = []

    for (let i = 0; i < cells; i++){
        generatedList.push(getItem())
    }
    return generatedList
}

onMounted(() => {
    items.value = generateItems()
    console.log("Смонтирван")
})
</script>

<style scoped>
.section-container.bg{
    background-image: linear-gradient(-45deg, yellow 0%, yellow 25%, yellow 51%, #ff357f 100%);
  -webkit-animation: AnimateBG 20s ease infinite;
    animation: AnimateBG 20s ease infinite;
}
.roulette-wrapper-container {
    margin: 10px 0px 20px 0px;
}
.rulette-line-container {
    position: absolute;
    width: 100%;
    height: 100%;
}
.rulette-line {
    position: absolute;
    height: calc(100% - 10px);
    width: 1px;
    background-color: var(--tg-theme-button-color);
    z-index: 100;
    top: 5px;
    left: calc(50% - 2.5px);
}
.rulette-poiner-bottom {
    position: absolute;
    width: 100%;
    transform: translate3d(calc(50% - 10px), -8px, 0);
    z-index: 100;
    color: var(--tg-theme-button-color);
}
.rulette-poiner-top {
    position: absolute;
    left: calc(50% - 10px);
    top: calc(100% - 13px);
    z-index: 100;
    color: var(--tg-theme-button-color);
}
.rulette-spin-button-cost-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 3px;
}
.rulette-spin-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 5px;
    width: 100%;
    color: var(--tg-theme-button-text-color);
    font-weight: 600;
    font-size: 20px;
    border-radius: 40px;
    cursor: pointer;
    padding: 10px;
}
.highlight-bg {
  background-color: #ffcc00; /* или любой другой стиль */
}
.roulette-wrapper {
    position: relative;
    overflow: hidden;
    padding: 10px 0px 10px 0px;
    border-radius: 10px;
    background-color: var(--tg-theme-bg-color);
}
.roulette-inner {
    position: relative;
    box-sizing: border-box;
    transform: translate3d(0, 0, 0);
    display: inline-flex;
    gap: 6px;
    transition: 5s cubic-bezier(.21, .53, .29, .99);
}
</style>
