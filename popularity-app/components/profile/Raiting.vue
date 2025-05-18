<template>
  <div class="profile-raiting-container">
    <ProfileItemRaiting :UserName="'Sgmt11'" :PhotoUrl="userStore.dataUnsafe.user.photo_url" :DonatedPopularity="12620" :Position="1"/>
  </div>
</template>
UserName: String,
UserId: Number,
PhotoUrl: String,
DonatedPopularity: Number,
Position: Number,
<script setup>

const userStore = useUserStore()

</script>

<style>

</style>