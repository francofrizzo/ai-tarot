<script setup>
import InfinityLoader from '@/components/InfinityLoader.vue'

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
  display: flex;
  align-items: center;
}

button {
  padding: 0.4em 1em;
  border-radius: 10px;
  border: none;
  background: linear-gradient(0deg, rgb(238, 117, 89), rgb(249, 140, 116));
  transition: background 0.2s ease, box-shadow 0.2s ease;
  color: #0f101f;
  cursor: pointer;
  font-family: 'Spectral', serif;
  font-variant: small-caps;
  font-size: 1.5em;
}

button:not(:disabled):hover {
  background: linear-gradient(0deg, rgb(248, 142, 118), rgb(250, 165, 146));
  box-shadow: 0 5px 15px rgba(238, 117, 89, 0.4);
}

button:disabled {
  background: linear-gradient(0deg, rgba(170, 154, 149, 0.6), rgba(234, 210, 204, 0.5));
  color: rgba(15, 16, 31, 0.7);
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
