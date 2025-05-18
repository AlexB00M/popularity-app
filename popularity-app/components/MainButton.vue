<template> 
    <div class="main-button-container">
        <button class="main-button-inner">
            <div class="main-button-text">
                {{ Text }}
            </div>
        </button>
    </div>
</template>

<script setup>
defineProps({
    Text: String,
    ImageSrc: String
})

</script>

<style>
.main-button-inner {
    background-color: var(--tg-theme-button-color);
    padding: 10px;
    border-radius: 10px;
}
.main-button-text {
    color: var(--tg-theme-button-text-color);
    font-weight: bold;
    font-size: 17px;
}
.main-button-container {
    outline: 1px solid rgba(255, 255, 255, 0.438);
    /* position: fixed;
    left: 0; */
    /* background-color: var(--tg-theme-secondary-bg-color); */
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: black;
    height: var(--bottom-menu-height);
    width: 100%;
}
</style>