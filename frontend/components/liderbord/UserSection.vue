<template>
  <div class="section-container">
    <div class="liderbord-top-section">
      <img class="liderbord-top-section-top-data-profile-user-photo" :src="userData.photo_url"/>
      <div class="liderbord-top-section-top-data">
        <div class="liderbord-top-section-top-data-left" >
          <div class="liderbord-top-section-top-data-left-username" >
            {{ userData.username }}
          </div>
          <div class="liderbord-top-section-top-data-left-bottom" :style="{color: totalPointsConfig[String(getLevelByTotalPoints(appStore.totalPoints, totalPointsConfig))].color}">
            <nuxt-icon name="fire"/>{{ formatNumberShort(appStore.totalPoints) }}
          </div>
        </div>
        <div class="liderbord-top-section-top-data-right">
          #{{ appStore.userPossition }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

const userStore = useUserStore()
const appStore = useAppStore()

const totalPointsConfig = appStore.totalPointsConfig
const userData = userStore.dataUnsafe.user

onMounted(() => {
  //
})

</script>

<style>
.section-container {
  background-color: var(--tg-theme-section-bg-color);
  border-radius: 10px;
  padding: 7px;
  box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
}
.liderbord-top-section-top-data-left-bottom {
  font-size: 14px;
  font-weight: 500;
}
.liderbord-top-section-top-data-right {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  font-weight: 500;
  color: var(--tg-theme-subtitle-text-color);
  font-size: 14px;
}
.liderbord-top-section-top-data {
  width: 100%;
  display: flex;
  justify-content: space-between;
}
.liderbord-top-section-top-data-left {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.liderbord-top-section-top-data-profile-user-photo {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
.liderbord-top-section-top-data-left-username {
  font-size: 16px;
  font-weight: 600;
}
.liderbord-top-section {
  display: flex;
  align-items: center;
  width: 100%;
  gap: 10px;
}
</style>