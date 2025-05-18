<template>
  <div class="friends-container">
    <div class="friends-top-section">
      <DotLottieVue class="friends-image" autoplay :src="'https://lottie.host/7c7f4d2e-6d98-4b39-8c5e-b7ebb51a560f/OSaWjPIXCA.lottie'"/>
      <span class="friends-top-section-text">Your referals and friends</span>
      <span class="friends-top-section-text-sub">Invite friends and get 1<nuxt-icon name="telegramStar" style="color: #ffc400;"/> from their each spin.</span>
    </div>
    <div class="friends-balance-sectio-container">
      <div class="friends-balance-section">
        <div class="friends-balance-section-data-container">
          <nuxt-icon name="telegramStar" style="color: #ffc400; font-size: 35px;"/>
          <span class="friends-balance-section-data">0</span> 
        </div>
        <button class="friends-balance-section-button" :class="{ can: canWithdraw }">
          <div class="friends-balance-section-button-text">
            Clime
          </div>
        </button>
      </div>
    </div>
    <div class="friends-invite-section">
      <button class="friends-invite-section-button-invite" @click="inviteClick">
        Invite <span v-if="activeTab === 'Referals'">referal</span><span v-if="activeTab === 'Friends'">friend</span>
      </button>
      <button class="friends-invite-section-copy" @click="copyClick">
        <nuxt-icon name="copy" />
      </button>
    </div>
    <div class="friends-main-section-tabs">
      <div class="friends-main-section-tabs-container" style="margin-bottom: 7px;">
        <button class="friends-main-section-tab" :class="{ active: activeTab === 'Referals' }" @click="activeTab = 'Referals'">
            Referals
        </button>
        <button class="friends-main-section-tab" :class="{ active: activeTab === 'Friends' }" @click="activeTab = 'Friends'">
            Friends
        </button>
      </div>
      <FriendsItemsReferals v-if="activeTab === 'Referals'" />
      <FriendsItemsFriends v-if="activeTab === 'Friends'" />
    </div>
  </div>
  <transition
    name="fade-out"
    appear
  >
    <DotLottieVue
      v-if="copyed"
      speed="2"
      style="width: 120px; height: 120px; position: fixed; bottom: calc(var(--bottom-menu-height) + 20px); right: 50%; transform: translate(50%, 0);"
      autoplay
      :src="'https://lottie.host/0314a16a-10c6-4dcf-8735-2d7615d4b2fe/Cb8tuegQNY.lottie'"
    />
  </transition>
</template>

<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'
import { useMiniApp } from 'vue-tg'

const miniApp = useMiniApp()
const activeTab = useState('activeTab')

const canWithdraw = ref(false)
const referalLink = ref('https://t.me/catizenbot/gameapp?startapp=rp_1365932')
const friendInviteLink = ref('https://t.me/catizenbot/gameapp?startapp=rp_1365932')
const messageText = ref('%F0%9F%92%B0Catizen%3A%20Unleash%2C%20Play%2C%20Earn%20-%20Where%20Every%20Game%20Leads%20to%20an%20Airdrop%20Adventure!%0A%F0%9F%8E%81Let%27s%20play-to-earn%20airdrop%20right%20now!')
const copyed = ref(false)
const canCopy = ref(true)

activeTab.value = 'Referals'

const copyToClipboard = async (text) => {
  await navigator.clipboard.writeText(text)
}
const copyClick = async () => {
  if (!canCopy.value) return
  try {
    copyed.value = true
    canCopy.value = false
    if (activeTab.value = 'Referals') {
      await copyToClipboard(referalLink.value)
    } else {
      await copyToClipboard(friendInviteLink.value)
    }
    setTimeout(() => {
      copyed.value = false
      canCopy.value = true
    }, 1000);
  } catch {
    setTimeout(() => {
      copyed.value = false
      canCopy.value = true
    }, 1000);
  }
}

const inviteClick = async () => {
  miniApp.openTelegramLink(`https://t.me/share/url?url=${referalLink.value}&text=${messageText.value}`)
}
</script>

<style>
.fade-out-enter-active {
  transition: none;
}

.fade-out-leave-active {
  transition: opacity 1s ease;
}

.fade-out-leave-to {
  opacity: 0;
}
.friends-invite-section-copy {
  background-color: rgb(49, 135, 192);
  border-radius: 10px;
  height: 50px;
  width: 50px;
  font-size: 17px;
  color: var(--tg-theme-button-text-color);
  cursor: pointer;
}
.friends-invite-section-button-invite {
  background-color: var(--tg-theme-button-color);
  border-radius: 10px;
  width: 84%;
  height: 50px;
  color: var(--tg-theme-button-text-color);
  font-size: 17px;
  font-weight: 700;
  cursor: pointer;
}
.friends-invite-section {
  width: 100%;
  display: flex;
  justify-content: space-between;
}
.friends-main-section-tabs {
  width: 100%;
}
.friends-main-section-tab.active {
  color: var(--tg-theme-text-color);
  background-color: var(--tg-theme-section-bg-color);
  box-shadow: 0 0px 12px rgba(0, 0, 0, 0.1);
}
.friends-main-section-tab {
  color: var(--tg-theme-subtitle-text-color);
  font-weight: bold;
  font-size: 16px;
  border-radius: 10px;
  padding: 5px;
  width: 50%;
}
.friends-main-section-tabs-container {
  display: flex;
  justify-content: space-around;
}
.friends-balance-section-button.can {
  background-color: var(--tg-theme-button-color);
  color: var(--tg-theme-button-text-color);
}
.friends-balance-section-button-text {
  font-size: 15px;
  font-weight: 700;
  padding: 12px;
}
.friends-balance-section-button {
  width: 100%;
  background-color: #395a7e;
  color: #9db2c9;
  border-radius: 10px;
}
.friends-balance-section-data-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 5px;
}
.friends-balance-section-data {
  font-size: 40px;
  font-weight: 700;
}
.friends-balance-section-icon {
  width: 35px;
  height: 35px;
}
.friends-top-section-text-sub {
  text-align: center;
  font-size: 14px;
  font-weight: 500;
  color: var(--tg-theme-subtitle-text-color);
}

.friends-balance-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 13px;
  gap: 6px;
}
.friends-balance-sectio-container {
  box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  border-radius: 10px;
}
.friends-top-section-text {
  font-size: 20px;
  font-weight: bold;
}
.friends-top-section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 7px;
}
.friends-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 0px 5px 0px 5px;
  gap: 13px;
}
.friends-image {
  width: 100px;
  height: 100px;
}
</style>