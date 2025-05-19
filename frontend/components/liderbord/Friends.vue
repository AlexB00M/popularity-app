<template>
  <div class="liderbord-friends-container">
    <LiderbordUser 
      :UserName="'MaxPower'"
      :PhotoUrl="userStore.dataUnsafe.user.photo_url"
      :Popularity="98000"
      :Possition="232"
    />
  </div>
</template>

<script setup>

const userStore = useUserStore()

</script>

<style>

</style>