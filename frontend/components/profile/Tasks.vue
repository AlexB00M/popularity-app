<template>
  <div v-if="Visible" class="tasks-container">
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
.tasks-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); 
  gap: 10px; 
}
</style>