<script setup>
import InfinityLoader from './InfinityLoader.vue'

const props = defineProps({
  waiting: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['click'])
</script>

<template>
  <div class="container">
    <Transition name="fade" mode="out-in">
      <button
        class="get-interpretation"
        v-if="!waiting"
        @click="emit('click')"
        :disabled="disabled"
      >
        Interpretar
      </button>
      <InfinityLoader width="60" v-else />
    </Transition>
  </div>
</template>

<style scoped>
.container {
  height: 60px;
}

button {
  padding: 0.6rem 1.4rem;
  border-radius: 10px;
  border: none;
  background-color: rgba(255, 255, 255, 0.8);
  transition: background-color 0.2s ease-in-out;
  cursor: pointer;
  font-family: 'Spectral', serif;
  font-variant: small-caps;
  font-size: 1.5rem;
}

button:not(:disabled):hover {
  background-color: rgba(255, 255, 255, 1);
}

button:disabled {
  background-color: rgba(255, 255, 255, 0.5);
  color: rgba(0, 0, 0, 0.5);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
