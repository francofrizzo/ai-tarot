<script setup>
import { onMounted, ref, defineProps } from 'vue'

const cards = ref([
  { img: '00_le_mat', name: 'El Loco' },
  { img: '01_le_bateleur', name: 'El Mago' },
  { img: '02_la_papesse', name: 'La Papisa' },
  { img: '03_limperatrise', name: 'La Emperatriz' },
  { img: '04_lempereur', name: 'El Emperador' },
  { img: '05_le_pape', name: 'El Papa' },
  { img: '06_lamoureux', name: 'Los Enamorados' },
  { img: '07_le_charior', name: 'El Carro' },
  { img: '08_justice', name: 'La Justicia' },
  { img: '09_lermite', name: 'El Emitaño' },
  { img: '10_la_roue_de_fortune', name: 'La Rueda de la Fortuna' },
  { img: '11_la_force', name: 'La Fuerza' },
  { img: '12_le_pendu', name: 'El Colgado' },
  { img: '13', name: 'El Arcano sin Nombre' },
  { img: '14_tenperance', name: 'La Templanza' },
  { img: '15_le_diable', name: 'El Diablo' },
  { img: '16_la_maison_dieu', name: 'La Torre' },
  { img: '17_lestoille', name: 'La Estrella' },
  { img: '18_la_lune', name: 'La Luna' },
  { img: '19_le_soleil', name: 'El Sol' },
  { img: '20_le_jugement', name: 'El Juicio' },
  { img: '21_le_monde', name: 'El Mundo' }
])

const props = defineProps({
  chosenCards: Array
})

const wheelDiv = ref(null)
const wheelRadius = ref(0)

const emit = defineEmits(['toggle-card-chosen'])

function recomputeWheelRadius() {
  wheelRadius.value = wheelDiv.value.clientWidth / 2
}

onMounted(function () {
  recomputeWheelRadius()
  window.onresize = recomputeWheelRadius
})

function cardContainerStyle(index) {
  const radius = wheelRadius.value
  const angle = (index - 1) * (360 / cards.value.length)
  const radians = angle * (Math.PI / 180)
  const x = radius + Math.round(Math.cos(radians) * radius * 0.7)
  const y = radius + Math.round(Math.sin(radians) * radius * 0.7)
  return {
    transform: `translate(${x}px, ${y}px) rotate(${90 + angle}deg)`
  }
}

function toggleChosen(index) {
  emit('toggle-card-chosen', index)
}
</script>

<template>
  <div class="card-wheel" :class="{ 'some-chosen': props.chosenCards.length }" ref="wheelDiv">
    <div class="card-wheel-content">
      <slot></slot>
    </div>
    <div
      v-for="(card, index) in cards"
      :key="index"
      class="card-container"
      :style="cardContainerStyle(index)"
      :class="{ chosen: props.chosenCards.includes(index) }"
    >
      <div class="card" @click="toggleChosen(index)">
        <img :src="`./src/assets/${card.img}.jpg`" class="card-img" :alt="card.name" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-wheel {
  position: relative;
  width: 100%;
  aspect-ratio: 1;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.card-container {
  position: absolute;
  top: 0%;
  left: -5%;
  width: 10%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.card-container:nth-child(even) {
  z-index: 0;
}

.card-container:nth-child(odd) {
  z-index: 1;
}

.card-container:hover {
  z-index: 2;
}

.card-wheel.some-chosen .card-container.chosen:nth-child(even) {
  z-index: 2;
}

.card-wheel.some-chosen .card-container.chosen:nth-child(odd) {
  z-index: 3;
}

.card-wheel.some-chosen .card-container.chosen:hover {
  z-index: 4;
}

.card {
  position: absolute;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
  transition: transform 0.2s ease, opacity 0.2s ease, filter 0.2s ease;
  border-radius: 4px;
  overflow: hidden;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.card:hover {
  transform: scale(1.15) translate(0, -15px);
}

.card-wheel.some-chosen .card {
  opacity: 0.5;
  filter: grayscale(100%);
}

.card-wheel.some-chosen .card:hover {
  opacity: 0.8;
}

.card-wheel.some-chosen .card-container.chosen .card {
  opacity: 1;
  filter: grayscale(0%);
  transform: scale(1.15) translate(0, -15px);
}

.card-img {
  width: 100%;
}

.card-wheel-content {
  width: 100%;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 30%;
}
</style>
