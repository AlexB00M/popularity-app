<template>
  <div class="section-container" style="padding: 0; overflow: hidden; position: relative; background-color: var(--tg-theme-bg-color);">
  <div id="bg-wrap">
    <svg viewBox="0 0 100 100" preserveAspectRatio="xMidYMid slice">
    <defs>
    <radialGradient id="Gradient1" cx="50%" cy="50%" fx="0.441602%" fy="50%" r=".5"><animate attributeName="fx" dur="34s" values="0%;3%;0%" repeatCount="indefinite"></animate><stop offset="0%" stop-color="rgba(255, 0, 255, 1)"></stop><stop offset="100%" stop-color="rgba(255, 0, 255, 0)"></stop></radialGradient>
    <radialGradient id="Gradient2" cx="50%" cy="50%" fx="2.68147%" fy="50%" r=".5"><animate attributeName="fx" dur="23.5s" values="0%;3%;0%" repeatCount="indefinite"></animate><stop offset="0%" stop-color="rgba(255, 255, 0, 1)"></stop><stop offset="100%" stop-color="rgba(255, 255, 0, 0)"></stop></radialGradient>
    <radialGradient id="Gradient3" cx="50%" cy="50%" fx="0.836536%" fy="50%" r=".5"><animate attributeName="fx" dur="21.5s" values="0%;3%;0%" repeatCount="indefinite"></animate><stop offset="0%" stop-color="rgba(0, 255, 255, 1)"></stop><stop offset="100%" stop-color="rgba(0, 255, 255, 0)"></stop></radialGradient>
    <radialGradient id="Gradient4" cx="50%" cy="50%" fx="4.56417%" fy="50%" r=".5"><animate attributeName="fx" dur="23s" values="0%;5%;0%" repeatCount="indefinite"></animate><stop offset="0%" stop-color="rgba(0, 255, 0, 1)"></stop><stop offset="100%" stop-color="rgba(0, 255, 0, 0)"></stop></radialGradient>
    <radialGradient id="Gradient5" cx="50%" cy="50%" fx="2.65405%" fy="50%" r=".5"><animate attributeName="fx" dur="24.5s" values="0%;5%;0%" repeatCount="indefinite"></animate><stop offset="0%" stop-color="rgba(0,0,255, 1)"></stop><stop offset="100%" stop-color="rgba(0,0,255, 0)"></stop></radialGradient>
    <radialGradient id="Gradient6" cx="50%" cy="50%" fx="0.981338%" fy="50%" r=".5"><animate attributeName="fx" dur="25.5s" values="0%;5%;0%" repeatCount="indefinite"></animate><stop offset="0%" stop-color="rgba(255,0,0, 1)"></stop><stop offset="100%" stop-color="rgba(255,0,0, 0)"></stop></radialGradient>
    </defs>
    <!-- <rect x="0" y="0" width="100%" height="100%" fill="url(#Gradient4)">
    <animate attributeName="x" dur="20s" values="25%;0%;25%" repeatCount="indefinite" />
    <animate attributeName="y" dur="21s" values="0%;25%;0%" repeatCount="indefinite" />
    <animateTransform attributeName="transform" type="rotate" from="0 50 50" to="360 50 50" dur="17s" repeatCount="indefinite"/>
    </rect>
    <rect x="0" y="0" width="100%" height="100%" fill="url(#Gradient5)">
    <animate attributeName="x" dur="23s" values="0%;-25%;0%" repeatCount="indefinite" />
    <animate attributeName="y" dur="24s" values="25%;-25%;25%" repeatCount="indefinite" />
    <animateTransform attributeName="transform" type="rotate" from="0 50 50" to="360 50 50" dur="18s" repeatCount="indefinite"/>
    </rect>
    <rect x="0" y="0" width="100%" height="100%" fill="url(#Gradient6)">
    <animate attributeName="x" dur="25s" values="-25%;0%;-25%" repeatCount="indefinite" />
    <animate attributeName="y" dur="26s" values="0%;-25%;0%" repeatCount="indefinite" />
    <animateTransform attributeName="transform" type="rotate" from="360 50 50" to="0 50 50" dur="19s" repeatCount="indefinite"/>
    </rect> -->
    <rect x="13.744%" y="1.18473%" width="100%" height="100%" fill="url(#Gradient1)" transform="rotate(334.41 50 50)"><animate attributeName="x" dur="20s" values="25%;0%;25%" repeatCount="indefinite"></animate><animate attributeName="y" dur="21s" values="0%;25%;0%" repeatCount="indefinite"></animate><animateTransform attributeName="transform" type="rotate" from="0 50 50" to="360 50 50" dur="7s" repeatCount="indefinite"></animateTransform></rect>
    <rect x="-2.17916%" y="35.4267%" width="100%" height="100%" fill="url(#Gradient2)" transform="rotate(255.072 50 50)"><animate attributeName="x" dur="23s" values="-25%;0%;-25%" repeatCount="indefinite"></animate><animate attributeName="y" dur="24s" values="0%;50%;0%" repeatCount="indefinite"></animate><animateTransform attributeName="transform" type="rotate" from="0 50 50" to="360 50 50" dur="12s" repeatCount="indefinite"></animateTransform>
    </rect>
    <rect x="9.00483%" y="14.5733%" width="100%" height="100%" fill="url(#Gradient3)" transform="rotate(139.903 50 50)"><animate attributeName="x" dur="25s" values="0%;25%;0%" repeatCount="indefinite"></animate><animate attributeName="y" dur="12s" values="0%;25%;0%" repeatCount="indefinite"></animate><animateTransform attributeName="transform" type="rotate" from="360 50 50" to="0 50 50" dur="9s" repeatCount="indefinite"></animateTransform>
    </rect>
    </svg>
  </div>
    <div class="placement-liderbord-container">
      <div class="placement-liderbord">
        <div class="placement-liderbord-line">
          <div class="placement-liderbord-top one">
            <div class="placement-liderbord-top-images-container" style="position: relative;">
              <img class="placement-liderbord-top-img" :src="userData.photo_url" style=" width: 80px; height: 80px;"/>
              <img class="placement-liderbord-top-1-img" src="~/assets/images/top1.png" style=" width: 35px; height: 35px; position: absolute; bottom: 0; left: calc(100% - 10px); transform: translate(-20px, 0) rotate(10deg);"/>
            </div>
            <div class="placement-liderbord-top-data">
              <div class="placement-liderbord-top-data-username">
                Maxik
              </div>
              <div class="placement-liderbord-top-data-points">
                <nuxt-icon name="fire"/>{{ formatNumberShort(1020000) }}
              </div>
            </div>
          </div>
        </div>
        <div class="placement-liderbord-line">
          <div class="placement-liderbord-top two">
            <div class="placement-liderbord-top-images-container" style="position: relative;">
              <img class="placement-liderbord-top-img" :src="userData.photo_url" style=" width: 65px; height: 65px;"/>
              <img class="placement-liderbord-top-2-img" src="~/assets/images/top2.png" style=" width: 28px; height: 28px; position: absolute; bottom: 0; left: 100%; transform: translate(-20px, 0) rotate(10deg);"/>
            </div>
            <div class="placement-liderbord-top-data">
              <div class="placement-liderbord-top-data-username">
                Maxik
              </div>
              <div class="placement-liderbord-top-data-points">
                <nuxt-icon name="fire"/>{{ formatNumberShort(1020000) }}
              </div>
            </div>
          </div>
          <div class="placement-liderbord-top free">
            <div class="placement-liderbord-top-images-container" style="position: relative;">
              <img class="placement-liderbord-top-img" :src="userData.photo_url" style=" width: 55px; height: 55px;"/>
              <img class="placement-liderbord-top-3-img" src="~/assets/images/top3.png" style=" width: 23px; height: 23px; position: absolute; bottom: 0; left: 100%; transform: translate(-20px, 0) rotate(10deg);"/>
            </div>
            <div class="placement-liderbord-top-data">
              <div class="placement-liderbord-top-data-username">
                Maxik
              </div>
              <div class="placement-liderbord-top-data-points">
                <nuxt-icon name="fire"/>{{ formatNumberShort(1020000) }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const userStore = useUserStore()
const appStore = useAppStore()

const totalPointsConfig = appStore.totalPointsConfig
const userData = userStore.dataUnsafe.user

</script>

<style>
#bg-wrap {
  height: 250px;
}
.placement-liderbord-top-data-points {
  font-weight: bold;
  font-size: 14px;
}
.placement-liderbord{
  width: 100%;
}
.placement-liderbord-line {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
}
.placement-liderbord-top-data {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.placement-liderbord-top {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.placement-liderbord-top-data-username {
  font-weight: bold;
}
.placement-liderbord-top-img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 2px solid white;
}
.placement-liderbord-container {
  display: flex;
  justify-content: space-around;
  align-items: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
}
</style>