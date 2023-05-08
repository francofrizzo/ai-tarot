<script setup>
import { onMounted, ref } from 'vue'

import leMat from '@/assets/cards/00_le_mat.jpg'
import leBateleur from '@/assets/cards/01_le_bateleur.jpg'
import laPapesse from '@/assets/cards/02_la_papesse.jpg'
import lImperatrise from '@/assets/cards/03_limperatrise.jpg'
import lEmpereur from '@/assets/cards/04_lempereur.jpg'
import lePape from '@/assets/cards/05_le_pape.jpg'
import lAmoureux from '@/assets/cards/06_lamoureux.jpg'
import leCharior from '@/assets/cards/07_le_charior.jpg'
import justice from '@/assets/cards/08_justice.jpg'
import lErmite from '@/assets/cards/09_lermite.jpg'
import laRoueDeFortune from '@/assets/cards/10_la_roue_de_fortune.jpg'
import laForce from '@/assets/cards/11_la_force.jpg'
import lePendu from '@/assets/cards/12_le_pendu.jpg'
import leArcaneSansNom from '@/assets/cards/13.jpg'
import tenperance from '@/assets/cards/14_tenperance.jpg'
import leDiable from '@/assets/cards/15_le_diable.jpg'
import laMaisonDieu from '@/assets/cards/16_la_maison_dieu.jpg'
import lEstoille from '@/assets/cards/17_lestoille.jpg'
import laLune from '@/assets/cards/18_la_lune.jpg'
import leSoleil from '@/assets/cards/19_le_soleil.jpg'
import leJugement from '@/assets/cards/20_le_jugement.jpg'
import leMonde from '@/assets/cards/21_le_monde.jpg'

const cards = ref([
  { img: leMat, name: 'El Loco' },
  { img: leBateleur, name: 'El Mago' },
  { img: laPapesse, name: 'La Papisa' },
  { img: lImperatrise, name: 'La Emperatriz' },
  { img: lEmpereur, name: 'El Emperador' },
  { img: lePape, name: 'El Papa' },
  { img: lAmoureux, name: 'Los Enamorados' },
  { img: leCharior, name: 'El Carro' },
  { img: justice, name: 'La Justicia' },
  { img: lErmite, name: 'El Emitaño' },
  { img: laRoueDeFortune, name: 'La Rueda de la Fortuna' },
  { img: laForce, name: 'La Fuerza' },
  { img: lePendu, name: 'El Colgado' },
  { img: leArcaneSansNom, name: 'El Arcano sin Nombre' },
  { img: tenperance, name: 'La Templanza' },
  { img: leDiable, name: 'El Diablo' },
  { img: laMaisonDieu, name: 'La Torre' },
  { img: lEstoille, name: 'La Estrella' },
  { img: laLune, name: 'La Luna' },
  { img: leSoleil, name: 'El Sol' },
  { img: leJugement, name: 'El Juicio' },
  { img: leMonde, name: 'El Mundo' }
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
  const angle = index * (360 / cards.value.length) - 90
  const radians = angle * (Math.PI / 180)
  const x = radius + Math.round(Math.cos(radians) * radius * 0.8)
  const y = radius + Math.round(Math.sin(radians) * radius * 0.8)
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
        <img :src="card.img" class="card-img" :alt="card.name" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-wheel {
  aspect-ratio: 1;
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

.card-container:nth-child(odd) {
  z-index: 0;
}

.card-container:nth-child(even) {
  z-index: 1;
}

.card-container:hover {
  z-index: 2;
}

.card-wheel.some-chosen .card-container.chosen:nth-child(odd) {
  z-index: 2;
}

.card-wheel.some-chosen .card-container.chosen:nth-child(even) {
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
  /* opacity: 0.5; */
  filter: grayscale(100%) brightness(60%) contrast(90%);
}

.card-wheel.some-chosen .card:hover {
  filter: grayscale(100%) brightness(90%);
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
