<template>
  <div class="liderbord-container">
    <div class="liderbord-header">
    </div>
    <LiderbordPlacementSection />
    <LiderbordUserSection style="position: sticky; top: 5px; z-index: 100;"/>
    <LiderbordMainSection />
  </div>
</template>


<script setup>

</script>
  
<style scoped>
.liderbord-image {
  width: 140px;
  height: 140px;
}
.liderbord-image-container {
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.liderbord-container {
  display: flex;
  flex-direction: column;
  gap: 8px
}
</style>