<script setup>
import { computed, ref } from 'vue'
import CardWheel from '@/components/CardWheel.vue'
import GetInterpretationButton from '@/components/GetInterpretationButton.vue'
import PersonalitySelector from '@/components/PersonalitySelector.vue'

import generalIcon from '@/assets/icons/general.png'
import questionIcon from '@/assets/icons/question.png'
import loveIcon from '@/assets/icons/love.png'
import friendshipIcon from '@/assets/icons/friendship.png'
import familyIcon from '@/assets/icons/family.png'
import healthIcon from '@/assets/icons/health.png'
import spiritualityIcon from '@/assets/icons/spirituality.png'
import projectsIcon from '@/assets/icons/projects.png'
import workIcon from '@/assets/icons/work.png'
import studiesIcon from '@/assets/icons/studies.png'
import moneyIcon from '@/assets/icons/money.png'
import travelIcon from '@/assets/icons/travel.png'
import leisureIcon from '@/assets/icons/leisure.png'

const topics = {
  general: {
    name: 'General',
    img: generalIcon
  },
  question: {
    name: 'Pregunta',
    img: questionIcon
  },
  love: {
    name: 'Amor',
    img: loveIcon
  },
  friendship: {
    name: 'Amistad',
    img: friendshipIcon
  },
  family: {
    name: 'Familia',
    img: familyIcon
  },
  health: {
    name: 'Salud',
    img: healthIcon
  },
  spirituality: {
    name: 'Espiritualidad',
    img: spiritualityIcon
  },
  projects: {
    name: 'Proyectos',
    img: projectsIcon
  },
  work: {
    name: 'Trabajo',
    img: workIcon
  },
  studies: {
    name: 'Estudios',
    img: studiesIcon
  },
  money: {
    name: 'Dinero',
    img: moneyIcon
  },
  travel: {
    name: 'Viajes',
    img: travelIcon
  },
  leisure: {
    name: 'Ocio',
    img: leisureIcon
  }
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

function chooseRandomCard() {
  if (chosenCards.value.length < 22) {
    const seed = Math.floor(Math.random() * (22 - chosenCards.value.length))
    let index = 0
    for (let i = 0; i < 22; i++) {
      if (!chosenCards.value.includes(i)) {
        if (index === seed) {
          toggleCardChosen(i)
          break
        }
        index++
      }
    }
  }
}

async function getInterpretation() {
  gettingInterpretation.value = true
  const apiUrl = import.meta.env.VITE_API_URL
  try {
    const response = await fetch(
      `${apiUrl}?${chosenCards.value.map((i) => `cards=${i}`).join('&')}${
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
      <div class="wheel-container">
        <CardWheel :chosen-cards="chosenCards" @toggle-card-chosen="toggleCardChosen($event)">
          <div class="topics">
            <div class="topic-line" v-for="line in topicLines" :key="line">
              <img
                v-for="topic in line"
                :key="topic"
                :src="topics[topic].img"
                class="topic"
                :class="{ selected: selectedTopic === topic }"
                :alt="topics[topic].name"
                @click="selectedTopic = topic"
              />
            </div>
          </div>
          <div v-if="selectedTopic === 'question'" class="question-container">
            <p
              contenteditable
              class="question-input"
              @focus="questionInputFocused = true"
              @blur="
                ($event) => {
                  questionInputFocused = false
                  question = $event.target.innerText
                }
              "
              v-text="question"
            />
            <div class="question-placeholder" v-if="!question && !questionInputFocused">
              Escribe tu pregunta aquí...
            </div>
          </div>
          <p class="selected-topic" v-else>
            {{ topics[selectedTopic].name }}
          </p>
          <GetInterpretationButton
            @click="getInterpretation"
            :disabled="chosenCards.length === 0"
            :waiting="gettingInterpretation"
          />
        </CardWheel>
      </div>

      <PersonalitySelector
        :personalities="personalities"
        :selected-personality="selectedPersonality"
        class="personality-selector"
        @update:selected-personality="selectedPersonality = $event"
      />

      <div class="random-card" @click="chooseRandomCard">
        <img src="@/assets/icons/dice.png" alt="Carta aleatoria" />
      </div>
    </div>

    <div class="interpretation-column">
      <div class="interpretation" v-if="interpretation.length > 0">
        <p v-for="line in interpretation" :key="line">{{ line }}</p>
      </div>
    </div>
  </main>
</template>

<style scoped>
.app-content * {
  outline: transparent solid 1px;
}
.app-content {
  max-width: 1400px;
  margin: 0 auto;
  font-weight: normal;
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 100%;
  height: 100vh;
}

.wheel-column {
  flex: 0 1 60%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  padding: 2rem;
}

.wheel-container {
  width: 100%;

  max-height: 100%;
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-wheel {
  height: 100%;
}

.interpretation-column {
  flex: 1 0 40%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 2rem 2rem 2rem 0;
  max-height: 100%;
}

.interpretation {
  overflow: auto;
  max-width: 30rem;
  margin: 0 auto;
  padding: 0 1rem;
}

.interpretation-column p:not(:last-child) {
  margin-bottom: 1rem;
}

.topics {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 1em;
}

.topic-line {
  display: flex;
  justify-content: center;
  width: 100%;
  margin-bottom: 1em;
}

.topic {
  width: 1.7em;
  height: 1.7em;
  transition: transform 0.2s ease, opacity 0.2s ease, filter 0.2s ease;
  opacity: 0.4;
  cursor: pointer;
  filter: grayscale(100%) brightness(200%);
  margin: 0 0.35em;
}

.topic:hover {
  transform: scale(1.15);
  opacity: 1;
}

.topic.selected {
  transform: scale(1.15);
  opacity: 1;
  filter: grayscale(0%) brightness(125%);
}

.selected-topic {
  font-size: 1.2em;
  text-align: center;
  margin-bottom: 1.8em;
  color: white;
}

.question-container {
  font-size: 1.2em;
  width: 100%;
  position: relative;
}

.question-input {
  width: 100%;
  text-align: center;
  margin-top: -0.5em;
  margin-bottom: 1.5em;
  border-radius: 8px;
  transition: background-color 0.2s ease;
  padding: 0.5em 0.75em;
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
  padding: 1em;
}

.random-card {
  position: absolute;
  bottom: 0;
  left: 0;
  padding: 1em;
  cursor: pointer;
  opacity: 0.8;
  transition: opacity 0.2s ease-in-out, transform 0.2s ease-in-out;
}

.random-card:hover {
  opacity: 1;
  transform: scale(1.1);
}

.random-card img {
  width: 1.5em;
  height: 1.5em;
}

@media (max-width: 1120px) {
  .card-wheel {
    font-size: 0.9rem;
  }
}

@media (max-width: 960px) {
  .app-content {
    flex-direction: column;
    justify-content: flex-start;
    height: auto;
    min-height: 100vh;
  }

  .wheel-column {
    width: 100%;
    max-width: 48rem;
    aspect-ratio: 1;
  }

  .card-wheel {
    font-size: 1rem;
  }

  .interpretation-column {
    padding: 0.5rem 2rem 2rem;
  }

  .interpretation {
    padding: 0;
  }

  .random-card {
    top: 0;
    right: 0;
    left: auto;
    bottom: auto;
  }
}

@media (max-width: 640px) {
  .card-wheel {
    font-size: 0.8rem;
  }
}

@media (max-width: 520px) {
  .card-wheel {
    font-size: 0.7rem;
  }
}
</style>
