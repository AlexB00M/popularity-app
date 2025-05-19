<template>
    <div class="item-card-container" :style="{ backgroundColor: info.color, boxShadow: '1px 1px 5px 0px ' + info.color }">
        <button class="item-card-data" @click="modalItemCardOpen" :style="themeStore.colorTheme === 'dark' ? { backgroundColor: 'var(--tg-theme-secondary-bg-color)' } : {}">
            <div class="item-card-data-params" :style="{ color: appStore.cardsConfig[Name].levels[String(info.level)].color }">
                {{ formatNumberShort(info.totalCardPoints) }}<nuxt-icon name="fire"/>
            </div>
            <DotLottieVue class="item-card-image" autoplay loop :src="info.url"/>
          </button>
        <div class="item-card-progress-bar-container">
            <div class="item-card-progress-bar" :style="{ width: info.progressPercent + '%' }"></div>
            <div class="item-card-progress-bar-text">
                {{ info.currentLevelThreshold }}<nav v-if="info.level < 5">/{{ info.nextLevelThreshold }}</nav>
            </div>
        </div> 
        <div class="item-card-bottom">
          <div class="item-card-level">
            {{ info.level }} Lvl
          </div>
          <div class="item-card-data-volume">
                {{ info.totalCards }}х
          </div>
        </div>
    </div>
    <ModalItemInventory :Visible="modalItemCardVisible" :CardName="Name" @close="modalItemCardClose"/>
</template>

<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue' 

const props = defineProps({
    Name: String,
})

const appStore = useAppStore()
const themeStore = useThemeStore()

const modalItemCardVisible = ref(false)
const oneOpened = useState('oneOpened')
oneOpened.value = false

const modalItemCardOpen = () => {
    if (oneOpened.value) return

    modalItemCardVisible.value = true
    oneOpened.value = true
}
const modalItemCardClose = () => {
    modalItemCardVisible.value = false
    oneOpened.value = false
} 

const getTotalCardsBeforeLevel = (level, levelsConfig) => {
  const levels = Object.keys(levelsConfig)
    .map(Number)
    .sort((a, b) => a - b);

  return levels
    .filter(lvl => lvl < level)
    .reduce((sum, lvl) => sum + Number(levelsConfig[lvl].cardsCountUpLevel || 0), 0);
}

const getLevelProgressInfo = (count, cardConfig) => {
  const pointsPerOne = cardConfig.pointsPerOne;
  const points = count * pointsPerOne;
  const levelsConfig = cardConfig.levels;
  const url = cardConfig.url;

  const level = getLevelByCards(count, levelsConfig)
  const currentLevelThreshold = count - getTotalCardsBeforeLevel(level, levelsConfig)
  const nextLevelThreshold = Number(levelsConfig[level].cardsCountUpLevel)

  const progressPercent = currentLevelThreshold/nextLevelThreshold * 100

  const color = levelsConfig[level].color;

  return {
    level,
    progressPercent,
    currentLevelThreshold,
    nextLevelThreshold,
    totalCardPoints: points,
    totalCards: count,
    url,
    color
  };
};

const info = computed(() => {
    const index = appStore.userCards.findIndex(item => item.name ===  props.Name)
    // console.log(index)
    console.log(getLevelProgressInfo(appStore.userCards[index].count, appStore.cardsConfig[props.Name]))
    return getLevelProgressInfo(appStore.userCards[index].count, appStore.cardsConfig[props.Name])
})

</script>

<style>
.item-card-bottom {
  display: flex;
  font-size: 12px;
  font-weight: bold;
  justify-content: space-between;
}
.item-card-progress-bar-text {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgb(0, 0, 0);
  font-size: 7px;
  font-weight: bold;
}
.item-card-progress-bar-container {
  position: relative;
  margin: 5px 0px 5px 0px;
  width: 100%;
  background-color: #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  height: 10px;
}
.item-card-progress-bar {
  height: 100%;
  background-color: rgb(251, 255, 0);
  transition: width 0.3s ease;
}
.item-card-data {
  background-color: var(--tg-theme-bg-color);
  /* background-color: aliceblue; */
  border-radius: 10px;
}
.item-card-data-params {
  padding-top: 5px;
  font-size: 13px;
  font-weight: bold;
  text-align: center;
}
.item-card-data-volume {
  color: var(--tg-theme-subtitle-text-color);
  text-align: right;
  font-weight: bold;
}
.item-card-image {
  height: 100px;
  top: 0;
}
.item-card-container {
  padding: 5px;
  display: inline-block;
  /* background-color: var(--tg-theme-section-bg-color); */
  /* background-color: var(--tg-theme-bg-color); */
  border-radius: 10px;
}
</style>
