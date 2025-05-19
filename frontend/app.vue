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

</script>