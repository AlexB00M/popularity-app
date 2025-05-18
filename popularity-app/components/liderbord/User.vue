<template>
  <button class="liderbord-section-container">
    <div class="liderbord-user-container">
    <img class="liderbord-user-photo" :src="PhotoUrl">
    <div class="liderbord-data">
        <div class="liderbord-data-left">
          <div class="liderbord-data-left-username">
            {{ UserName }}
          </div>
          <div v-if="activeTab === 'Top'" class="liderbord-data-left-bottom" :style="{color: totalPointsConfig[String(getLevelByTotalPoints(Popularity, totalPointsConfig))].color}">
            <nuxt-icon name="fire"/>{{ formatNumberShort(Popularity) }}
          </div>
          <div v-if="activeTab === 'Hot'" class="liderbord-data-left-bottom" :style="{color: 'rgb(21, 228, 3)'}">
            <nuxt-icon name="fire"/>+{{ formatNumberShort(Popularity) }}
          </div>
          <div v-if="activeTab === 'Friends'" class="liderbord-data-left-bottom" :style="{color: totalPointsConfig[String(getLevelByTotalPoints(Popularity, totalPointsConfig))].color}">
            <nuxt-icon name="fire"/>{{ formatNumberShort(Popularity) }}
          </div>
        </div>
        <div class="liderbord-data-right">
          #{{ Possition }}
        </div>
      </div>
    </div>
  </button>
</template>

<script setup>
defineProps({
  UserName: String,
  UserId: Number,
  PhotoUrl: String,
  Popularity: Number,
  Possition: Number,
})

const appStore = useAppStore()
const totalPointsConfig = appStore.totalPointsConfig

const activeTab = useState('activeTab')

</script>

<style>
.liderbord-section-container:last-child .liderbord-data::after {
  display: none;
}
.liderbord-data::after {
  content: "";
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 0.6px;
  background-color: var(--tg-theme-section-separator-color);
}
.liderbord-section-container {
  width: 100%;
  padding: 0px 7px 0px 7px;
  position: relative;
  overflow: hidden;
}
.liderbord-data-left-bottom {
  font-size: 14px;
  font-weight: 500;
}
.liderbord-data-left-username {
  color: var(--tg-theme-text-color);
  font-size: 16px;
  font-weight: 600;
}
.liderbord-data-right {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  font-weight: 500;
  color: var(--tg-theme-subtitle-text-color);
  font-size: 14px;
}
.liderbord-data-left {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
  height: 50px;
}
.liderbord-data {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.liderbord-user-photo {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
.liderbord-user-container {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 10px;
  height: 64px;
}
</style>