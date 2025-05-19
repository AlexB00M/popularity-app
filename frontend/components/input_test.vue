<template>
    <input
      type="text"
      inputmode="decimal"
      pattern="[0-9]*"
      placeholder="0"
      class="text-2xl font-bold w-full text-right"
    />
</template>

<script setup>
import { onMounted, onBeforeUnmount } from 'vue'

onMounted(() => {
  document.addEventListener('click', handleOutsideClick)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleOutsideClick)
})

function handleOutsideClick(event) {
  const target = event.target
  if (
    !(target instanceof HTMLInputElement || target.closest('input')) &&
    document.activeElement instanceof HTMLElement
  ) {
    document.activeElement.blur()
  }
}
</script>

<style>

</style>