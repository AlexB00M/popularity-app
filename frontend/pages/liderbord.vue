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

onMounted(() => {
  fetch('http://localhost:8000/api/users/leaderboard/1', {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
        'Content-Type': 'application/json'
    }
    })
    .then(response => {
      if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json()
    })
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error('Ошибка при запросе профиля:', error);
  })
})
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