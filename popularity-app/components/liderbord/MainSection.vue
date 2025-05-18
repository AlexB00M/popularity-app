<template>
    <div class="liderbord-main-section-container">
        <div class="liderbord-main-section-tabs-container" style="margin-bottom: 7px;">
            <button class="liderbord-main-section-tab" :class="{ active: activeTab === 'Top' }" @click="activeTab = 'Top'">
                Top
            </button>
            <button class="liderbord-main-section-tab" :class="{ active: activeTab === 'Hot' }" @click="activeTab = 'Hot'">
                Hot
            </button>
            <button class="liderbord-main-section-tab" :class="{ active: activeTab === 'Friends' }" @click="activeTab = 'Friends'" >
                Friends
            </button>
        </div>
        <LiderbordTop v-if="activeTab === 'Top'" />
        <LiderbordFriends v-if="activeTab === 'Friends'" />
        <LiderbordHot v-if="activeTab === 'Hot'" />
    </div>
</template>

<script setup>

const activeTab = useState('activeTab')
activeTab.value ='Top'

</script>

<style>
.liderbord-main-section-tab.active {
  color: var(--tg-theme-text-color);
  background-color: var(--tg-theme-section-bg-color);
  box-shadow: 0 0px 12px rgba(0, 0, 0, 0.1);
}
.liderbord-main-section-tab {
  color: var(--tg-theme-subtitle-text-color);
  font-weight: bold;
  font-size: 16px;
  border-radius: 10px;
  padding: 5px;
  width: 33%;
}
.liderbord-main-section-tabs-container {
  display: flex;
}
</style>