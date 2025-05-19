<template>
    <div class="main-section-container">
        <div class="main-section-tabs-container">
            <button class="main-section-tab" :class="{ active: activeTab === 'Inventory' }" @click="activeTab = 'Inventory'">
                Inventory
            </button>
            <button class="main-section-tab" :class="{ active: activeTab === 'Raiting' }" @click="activeTab = 'Raiting'" >
                Raiting
            </button>
            <button class="main-section-tab" :class="{ active: activeTab === 'History' }" @click="activeTab = 'History'">
                History
            </button>
            <button class="main-section-tab" :class="{ active: activeTab === 'Messages' }" @click="activeTab = 'Messages'" >
                Messages
            </button>
        </div>
        <ProfileInventory v-if="activeTab === 'Inventory'" />
        <ProfileMessages v-if="activeTab === 'Messages'" />
        <ProfileRaiting v-if="activeTab === 'Raiting'" />
        <ProfileHistory v-if="activeTab === 'History'" />
    </div>
</template>

<script setup>

const activeTab = ref('Inventory')

</script>

<style>
.main-section-tab.active {
  color: var(--tg-theme-text-color);
  background-color: var(--tg-theme-section-bg-color);
  box-shadow: 0 0px 12px rgba(0, 0, 0, 0.1);
}
.main-section-container {
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.main-section-tab {
    color: var(--tg-theme-subtitle-text-color);
    font-weight: bold;
    font-size: 16px;
    border-radius: 10px;
    padding: 5px;
    width: 25%;
}
.main-section-tabs-container {
    display: flex;
}
</style>