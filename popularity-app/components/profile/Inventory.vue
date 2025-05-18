<template>
  <div class="inventory-container">
    <ProfileItemInventory
      v-for="(item, index) in appStore.userCards"
      :key="index"
      :Name="item.name"
    />
  </div>
</template>

<script setup>

const appStore = useAppStore()

</script>

<style>
.inventory-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); 
  gap: 10px; 
}
</style>