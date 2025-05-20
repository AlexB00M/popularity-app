<template>
  <UApp>
    <NuxtLayout>
      <NuxtPage/>
    </NuxtLayout>
  </UApp>
</template>

<script setup>

const webapp = useUserStore().webAppData
setupTelegramApp(webapp)

fetch('http://localhost:8000/api/users/user_gifts/', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
    },
})
.then(response => response.json())
.then(data => {
    
})
.catch(error => {
    console.error('Ошибка при получении токенов:', error)
});


</script>