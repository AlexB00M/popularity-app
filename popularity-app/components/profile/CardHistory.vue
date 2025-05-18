<template>
    <div @click="openBetInfoModal" class="card-history-container">
        <img class="streamer-avatar" :src="UserFromPhotoUrl"/>
        <div class="card-history-container-right">
            <div class="card-history-container-top">
                <div class="card-history-container-top-name">
                    {{ UserNameFrom }} 
                </div>
                <div class="card-history-container-top-profit-container" :style="{ color: appStore.colorTotal }">
                    <div class="card-history-container-top-profit">
                        +{{ formatNumberShort(Count*PointsPerOne) }}
                    </div>
                    <nuxt-icon name="fire"/>
                </div>
            </div>
            <div class="card-history-container-bottom">
                <div class="card-history-container-top-data">
                    {{ Data }} 12 March
                </div>
                <div class="card-history-container-top-count">
                    {{ Count }}x
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
defineProps({
    UserNameFrom: String,
    UserFromPhotoUrl: String,
    Data: String,
    Count: Number,
    PointsPerOne: Number,
});

const appStore = useAppStore()

</script>

<style>
.card-history-container-top-profit-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 3px;
}
.card-history-container-top-data {
    font-style: italic;
    color: var(--tg-theme-subtitle-text-color);
}
.card-history-container-top-profit {
    font-weight: bold;
}
.card-history-container-top-count {
    font-weight: bold;
}
.card-history-container-top-name {
    font-weight: bold;
}
.card-history-container-bottom {
    display: flex;
    justify-content: space-between;
    width: 100%;
}
.card-history-container-top {
    display: flex;
    justify-content: space-between;
    
}
.card-history-container-right {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    width: 100%;
}
.card-history-container {
    display: flex;
    gap: 10px;
}
.streamer-avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
}
</style>