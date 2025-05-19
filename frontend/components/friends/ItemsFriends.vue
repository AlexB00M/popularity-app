<template>
  <div class="friends-friends-container">
    <FriendsItem 
      :UserName="'MaxPower'"
      :PhotoUrl="userStore.dataUnsafe.user.photo_url"
      :Popularity="98000"
      :Profit="4"
    />
    <FriendsItem 
      :UserName="'MaxPower'"
      :PhotoUrl="userStore.dataUnsafe.user.photo_url"
      :Popularity="8000"
      :Profit="15"
    />
  </div>
</template>

<script setup>

const userStore = useUserStore()

</script>

<style>

</style>