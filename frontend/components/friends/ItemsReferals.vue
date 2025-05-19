<template>
  <div class="friends-referals-container">
    <FriendsItem 
      :UserName="'MaxPower'"
      :PhotoUrl="userStore.dataUnsafe.user.photo_url"
      :Popularity="98000"
      :Profit="2"
    />
  </div>
</template>

<script setup>
const userStore = useUserStore()

</script>

<style>

</style>