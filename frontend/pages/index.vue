<template>
    <div class="page-container" :class="{winModal: winModalVisible}">
        <TopUserData />
        <!-- <StoreChartSection /> -->
        <StoreRouletteSection />
        <StoreSection />
    </div>
</template>

<script setup>

const winModalVisible = useState('winModalVisible')

</script>

<style>
.page-container.winModal {
    overflow: hidden;
}
.page-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding-bottom: 70px;
}
.section-lable {
    font-weight: 600;
    font-size: 20px;
    margin-bottom: 10px;
    margin-left: 5px;
}
.section-container {
    background-color: var(--tg-theme-section-bg-color);
    border-radius: 10px;
    padding: 7px;
    box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
}
</style>