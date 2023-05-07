<script setup>
import { computed, ref } from 'vue'
import CardWheel from './components/CardWheel.vue'
import GetInterpretationButton from './components/GetInterpretationButton.vue'
import PersonalitySelector from './components/PersonalitySelector.vue'

const topics = {
  general: 'General',
  question: 'Pregunta',
  love: 'Amor',
  friendship: 'Amistad',
  family: 'Familia',
  health: 'Salud',
  spirituality: 'Espiritualidad',
  projects: 'Proyectos',
  work: 'Trabajo',
  studies: 'Estudios',
  money: 'Dinero',
  travel: 'Viajes',
  leisure: 'Ocio'
}

const personalities = {
  default: 'Normal',
  creative: 'Creativo',
  practical: 'Práctico',
  sarcastic: 'Gracioso',
  esoteric: 'Esotérico',
  optimistic: 'Optimista',
  pessimistic: 'Pesimista'
}

const chosenCards = ref([])
const selectedTopic = ref('general')
const selectedPersonality = ref('default')
const question = ref('')
const questionInputFocused = ref(false)
const gettingInterpretation = ref(false)
const interpretation = ref([])

const topicLines = computed(() => {
  const keys = Object.keys(topics).reverse()
  const lineCount = Math.max(1, Math.round(keys.length / 6))
  const itemsPerLine = Math.ceil(keys.length / lineCount)
  const lines = []
  for (let i = 0; i < lineCount; i++) {
    lines.push(keys.slice(i * itemsPerLine, (i + 1) * itemsPerLine).reverse())
  }
  return lines.reverse()
})

function toggleCardChosen(index) {
  if (chosenCards.value.includes(index)) {
    chosenCards.value = chosenCards.value.filter((i) => i !== index)
  } else {
    chosenCards.value = [...chosenCards.value, index]
  }
}

async function getInterpretation() {
  gettingInterpretation.value = true
  try {
    const response = await fetch(
      `http://localhost:3000?${chosenCards.value.map((i) => `cards=${i}`).join('&')}${
        selectedTopic.value === 'question' && question.value ? `&question=${question.value}` : ''
      }${
        !['general', 'question'].includes(selectedTopic.value)
          ? `&topic=${selectedTopic.value}`
          : ''
      }&personality=${selectedPersonality.value}`,
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      }
    )
    const data = await response.json()
    interpretation.value = data.response.split(/\n+/)
  } finally {
    gettingInterpretation.value = false
  }
}
</script>

<template>
  <main class="app-content">
    <div class="wheel-column">
      <CardWheel :chosen-cards="chosenCards" @toggle-card-chosen="toggleCardChosen($event)">
        <div class="topics">
          <div class="topic-line" v-for="line in topicLines" :key="line">
            <img
              v-for="topic in line"
              :key="topic"
              :src="`./src/assets/${topic}.png`"
              class="topic"
              :class="{ selected: selectedTopic === topic }"
              :alt="topic"
              @click="selectedTopic = topic"
            />
          </div>
        </div>
        <div v-if="selectedTopic === 'question'" class="question-container">
          <p
            contenteditable
            class="question-input"
            @input="question = $event.target.innerText"
            @focus="questionInputFocused = true"
            @blur="questionInputFocused = false"
          >
            {{ question }}
          </p>
          <div class="question-placeholder" v-if="!question && !questionInputFocused">
            Escribe tu pregunta aquí...
          </div>
        </div>
        <p class="selected-topic" v-else>
          {{ topics[selectedTopic] }}
        </p>
        <GetInterpretationButton
          @click="getInterpretation"
          :disabled="chosenCards.length === 0"
          :waiting="gettingInterpretation"
        />
      </CardWheel>
    </div>

    <div class="interpretation-column">
      <div class="interpretation">
        <p v-for="line in interpretation" :key="line">{{ line }}</p>
      </div>
    </div>

    <PersonalitySelector
      :personalities="personalities"
      :selected-personality="selectedPersonality"
      class="personality-selector"
      @update:selected-personality="selectedPersonality = $event"
    />
  </main>
</template>

<style scoped>
.app-content {
  max-width: 1400px;
  margin: 0 auto;
  font-weight: normal;
  display: flex;
  width: 100%;
  height: 100vh;
  align-items: center;
  overflow: hidden;
}

.wheel-column {
  flex: 7;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  position: relative;
  padding: 2rem;
}

.interpretation-column {
  flex: 3;
  min-width: 25rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 2rem 2rem 2rem 0;
  max-height: 100%;
}

.interpretation {
  overflow: auto;
  padding: 0 1rem;
}

.interpretation-column p:not(:last-child) {
  margin-bottom: 1rem;
}

.topics {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 1rem;
}

.topic-line {
  display: flex;
  justify-content: center;
  width: 100%;
  margin-bottom: 1rem;
}

.topic {
  width: 1.7rem;
  height: 1.7rem;
  transition: transform 0.2s ease, opacity 0.2s ease, filter 0.2s ease;
  opacity: 0.4;
  cursor: pointer;
  filter: grayscale(100%) brightness(200%);
  margin: 0 0.35rem;
}

.topic:hover {
  transform: scale(1.15);
  opacity: 1;
}

.topic.selected {
  transform: scale(1.15);
  opacity: 1;
  filter: grayscale(0%) brightness(100%);
}

.selected-topic {
  font-size: 1.2rem;
  text-align: center;
  margin-bottom: 2rem;
  color: white;
}

.question-container {
  font-size: 1.2rem;
  width: 100%;
  position: relative;
}

.question-input {
  width: 100%;
  text-align: center;
  margin-top: -0.5rem;
  margin-bottom: 1.5rem;
  border-radius: 8px;
  transition: background-color 0.2s ease;
  padding: 0.5rem 0.75rem;
}

.question-placeholder {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  pointer-events: none;
  opacity: 0.4;
}

.question-input:focus {
  outline: none;
  background-color: rgba(255, 255, 255, 0.1);
}

.personality-selector {
  position: absolute;
  top: 0;
  left: 0;
  padding: 1rem;
}
</style>
