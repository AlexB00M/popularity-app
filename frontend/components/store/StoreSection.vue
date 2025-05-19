<template>
    <div class="section-container-store">
        <div class="store-section-cards-container">
            <StoreItemStore
                v-for="(cardConfig, cardName) in appStore.cardsConfig"
                :key="cardName"
                :Name="cardName"
            />
        </div>
    </div>
</template>

<script setup>

const appStore = useAppStore()

</script>

<style>
.section-container-store {
    border-radius: 10px;
}
.store-section-cards-container {
    width: 100%;
    display: grid;
    justify-items: center;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
}
</style>