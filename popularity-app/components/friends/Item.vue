<template>
  <button class="friends-section-container">
    <div class="friends-user-container">
    <img class="friends-user-photo" :src="PhotoUrl">
    <div class="friends-data">
        <div class="friends-data-left">
          <div class="friends-data-left-username">
            {{ UserName }}
          </div>
          <div class="friends-data-left-bottom" :style="{color: totalPointsConfig[String(getLevelByTotalPoints(Popularity, totalPointsConfig))].color}">
            <nuxt-icon name="fire"/>{{ formatNumberShort(Popularity) }}
          </div>
        </div>
        <div class="friends-data-right">
          +{{ Profit }} <nuxt-icon name="telegramStar" style="color: var(--telegram-star-color); font-size: 15px;"/>
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
  Profit: Number,
})

const appStore = useAppStore()
const totalPointsConfig = appStore.totalPointsConfig

</script>

<style>
.friends-section-container:last-child .friends-data::after {
  display: none;
}
.friends-data::after {
  content: "";
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 0.6px;
  background-color: var(--tg-theme-section-separator-color);
}
.friends-section-container {
  width: 100%;
  padding: 0px 7px 0px 7px;
  position: relative;
  overflow: hidden;
}
.friends-data-left-bottom {
  font-size: 14px;
  font-weight: 500;
}
.friends-data-left-username {
  color: var(--tg-theme-text-color);
  font-size: 16px;
  font-weight: 600;
}
.friends-data-right {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  font-weight: 600;
  color: green;
  font-size: 16px;
  gap: 4px;
}
.friends-data-left {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
  height: 50px;
}
.friends-data {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.friends-user-photo {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
.friends-user-container {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 10px;
  height: 64px;
}
</style>