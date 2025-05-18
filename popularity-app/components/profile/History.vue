<template>
  <div v-if="Visible" class="history-container">
    <ProfileItemInventory
      v-for="(item, index) in appStore.userCards"
      :key="index"
      :Name="item.name"
    />
  </div>
</template>

<script setup>
defineProps({
  Visible: Boolean,
})

const appStore = useAppStore()

</script>

<style>
.history-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); 
  gap: 10px; 
}
</style>