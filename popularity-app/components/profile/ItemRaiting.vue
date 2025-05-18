<template>
  <button class="liderbord-section-container">
    <div class="liderbord-user-container">
    <img class="liderbord-user-photo" :src="PhotoUrl">
    <div class="liderbord-data">
        <div class="liderbord-data-left">
          <div class="liderbord-data-left-username">
            {{ UserName }}
          </div>
          <div class="liderbord-data-left-bottom" style="color: var(--tg-theme-subtitle-text-color)">
            <nuxt-icon name="fire"/>{{ formatNumberShort(DonatedPopularity) }}
          </div>
        </div>
        <div class="liderbord-data-right">
          #{{ Position }}
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
  DonatedPopularity: Number,
  Position: Number,
})
</script>

<style>
.liderbord-data::after {
  content: "";
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 1px;
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