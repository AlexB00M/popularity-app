<template>
    <transition name="slide-up">
        <div class="alert-bottom-container">
            <div class="alert-bottom-text">
                {{ Text }}
            </div>
        </div>
    </transition>
</template>

<script setup>
defineProps({
    Text: String,
})

</script>

<style>
.alert-bottom-container{
    position: fixed;
    left: 50%;
    bottom: calc(var(--bottom-menu-height) + 20px);
    background-color: var(--tg-theme-section-header-text-color);
    width: 95%;
    transform: translate(-50%, 0);
}

.slide-up-enter-active, .slide-up-leave-active {
  transition: transform 0.3s ease, opacity 0.3s ease;
}
.slide-up-enter-from, .slide-up-leave-to {
  transform: translateY(100%);
  opacity: 0;
}
</style>