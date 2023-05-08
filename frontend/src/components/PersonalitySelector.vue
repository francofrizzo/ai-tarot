<script setup>
const emit = defineEmits(['update:selectedPersonality'])

function rotatePersonality() {
  const personalities = Object.keys(props.personalities)
  const currentPersonalityIndex = personalities.indexOf(props.selectedPersonality)
  const nextPersonalityIndex = (currentPersonalityIndex + 1) % personalities.length
  const nextPersonalityKey = personalities[nextPersonalityIndex]
  emit('update:selectedPersonality', nextPersonalityKey)
}

const props = defineProps({
  personalities: {
    type: Object,
    required: true
  },
  selectedPersonality: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div @click="rotatePersonality">
    <div class="current-personality">
      <img src="@/assets/icons/settings.png" class="settings" alt="settings" />
      {{ personalities[selectedPersonality] }}
    </div>
  </div>
</template>

<style scoped>
.current-personality {
  font-size: 0.9em;
  display: flex;
  align-items: center;
  cursor: pointer;
  opacity: 0.9;
  transition: opacity 0.2s ease;
  user-select: none;
}

.current-personality:hover {
  opacity: 1;
}

.current-personality img {
  width: 1.5em;
  height: 1.5em;
  margin: 0 0.5em 0.1em 0;
  transition: transform 0.2s ease;
}

.current-personality:hover img {
  transform: rotate(45deg) scale(1.15);
}
</style>
