<template>
  <button class="profile-social-container" @click="openLink">
    <DotLottieVue class="profile-social-image" autoplay :src="ImageUrl"/>
    <div class="profile-social-button">
      {{ SocialName }}
    </div>
  </button>
</template>

<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue' 
import { useMiniApp } from 'vue-tg'

const props = defineProps({
  ImageUrl: String,
  SocialName: String,
  SocialLink: String
})

const miniApp = useMiniApp()

const openLink = () => {
  if (props.SocialName === 'Telegram'){
    miniApp.openTelegramLink(props.SocialLink)
  } else {
    miniApp.openLink(props.SocialLink)
  }
}
</script>

<style>
.profile-social-button {
  font-size: 13px;
  font-weight: 600;
  color: var(--tg-theme-text-color);
}
.profile-social-image {
  width: 40px;
  height: 40px;
}
.profile-social-container {
  background-color: var(--tg-theme-section-bg-color);
  border-radius: 10px;
  display: flex;
  align-items: center;
  padding-right: 10px;
  box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
}
</style>