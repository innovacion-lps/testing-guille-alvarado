<script setup>
import { ref, nextTick } from 'vue'

const stages = ref([
  {
    id: 1,
    title: 'Requerimiento recibido',
    date: '15/09/2026',
    icon: '✓'
  },
  {
    id: 2,
    title: '1er contacto',
    date: '16/09/2026',
    icon: '✓'
  },
  {
    id: 3,
    title: '1ra entrevista',
    date: '',
    icon: '✓'
  },
  {
    id: 4,
    title: 'Segunda entrevista',
    date: '',
    icon: '✓'
  },
  {
    id: 5,
    title: 'Selección',
    date: '',
    icon: '✓'
  },
  {
    id: 6,
    title: 'Cierre',
    date: '',
    icon: '⚑'
  }
])

const isEditing = ref(false)
const dateInputs = ref([])

function hasDate(stage) {
  return stage.date.trim() !== ''
}

function isLineActive(index) {
  const nextStage = stages.value[index + 1]

  if (!nextStage) {
    return false
  }

  return hasDate(nextStage)
}

function toggleEditing() {
  isEditing.value = !isEditing.value

  if (isEditing.value) {
    nextTick(() => {
      dateInputs.value[0]?.focus()
    })
  }
}

function focusDate(index) {
  isEditing.value = true

  nextTick(() => {
    dateInputs.value[index]?.focus()
  })
}

function saveChanges() {
  isEditing.value = false
}
</script>

<template>
  <section class="tracking-card">
    <!-- HEADER -->
    <div class="tracking-header">
      <div class="tracking-title">
        <div class="title-icon">◷</div>

        <h2>Seguimiento del proceso</h2>
      </div>

      <div class="header-actions">
        <button class="edit-button" type="button" @click="toggleEditing">
          <span>✎</span>
          Editar fechas
        </button>

        <button v-if="isEditing" class="btn btn-primary" type="button" @click="saveChanges">
          <span>✓</span>
          Guardar cambios
        </button>
      </div>
    </div>

    <!-- PROCESS -->
    <div class="process-container">
      <div class="process-line"></div>

      <div v-for="(stage, index) in stages" :key="stage.id" class="stage">
        <!-- CONNECTING LINE -->
        <div
          v-if="index < stages.length - 1"
          class="stage-connector"
          :class="{
            active: isLineActive(index)
          }"
        ></div>

        <!-- CIRCLE -->
        <button
          type="button"
          class="stage-circle"
          :class="{
            completed: hasDate(stage),
            pending: !hasDate(stage),
            'last-stage': index === stages.length - 1
          }"
          @click="focusDate(index)"
        >
          <span v-if="hasDate(stage)"> ✓ </span>

          <span v-else-if="index === stages.length - 1"> ⚑ </span>

          <span v-else> ✓ </span>
        </button>

        <!-- INFORMATION -->
        <div class="stage-content">
          <div class="stage-name">
            {{ stage.title }}
          </div>

          <input
            :ref="el => (dateInputs[index] = el)"
            v-model="stage.date"
            class="stage-date"
            :class="{
              filled: hasDate(stage)
            }"
            type="text"
            placeholder="0"
            :readonly="!isEditing"
            @click.stop
          />
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.tracking-card {
  width: 100%;
  box-sizing: border-box;

  margin-top: 30px;
  padding: 28px 32px 34px;

  background: #ffffff;

  border: 1px solid #e6e3dd;
  border-radius: 18px;

  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
}

/* --------------------------------
   HEADER
-------------------------------- */

.tracking-header {
  display: flex;
  align-items: center;
  justify-content: space-between;

  margin-bottom: 38px;
}

.tracking-title {
  display: flex;
  align-items: center;
  gap: 12px;
}

.title-icon {
  width: 26px;
  height: 26px;

  display: flex;
  align-items: center;
  justify-content: center;

  color: #d97757;

  font-size: 26px;
  font-weight: 500;
}

.tracking-title h2 {
  margin: 0;

  color: #2a2520;

  font-family: var(--font-display, Georgia, serif);
  font-size: 22px;
  font-weight: 600;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.edit-button {
  height: 42px;

  display: flex;
  align-items: center;
  gap: 8px;

  padding: 0 16px;

  border-radius: 10px;

  font-family: inherit;
  font-size: 14px;
  font-weight: 500;

  cursor: pointer;

  transition: all 0.2s ease;
}

.edit-button {
  background: #ffffff;
  color: #4f4a45;
  border: 1px solid #e6e3dd;
}

.edit-button:hover {
  border-color: #d97757;
  color: #d97757;
}

.edit-button span {
  color: #d97757;
  font-size: 17px;
}

/* .save-button migrado a global .btn-primary (assets/global.css) */

/* --------------------------------
   PROCESS
-------------------------------- */

.process-container {
  position: relative;

  display: grid;
  grid-template-columns: repeat(6, 1fr);

  width: 100%;
}

/*
  Línea base gris que recorre todo el proceso.
*/
.process-line {
  position: absolute;

  top: 21px;
  left: 8.5%;
  right: 8.5%;

  height: 2px;

  background: #dedbd5;

  z-index: 0;
}

.stage {
  position: relative;

  display: flex;
  flex-direction: column;
  align-items: center;

  min-width: 0;
}

/*
  Línea individual entre cada etapa.
*/
.stage-connector {
  position: absolute;

  top: 20px;

  left: 50%;
  width: 100%;

  height: 3px;

  background: #dedbd5;

  z-index: 1;

  transition: background 0.3s ease;
}

.stage-connector.active {
  background: #d97757;
}

/* --------------------------------
   CIRCLE
-------------------------------- */

.stage-circle {
  position: relative;

  z-index: 2;

  width: 42px;
  height: 42px;

  display: flex;
  align-items: center;
  justify-content: center;

  padding: 0;

  border-radius: 50%;

  border: none;

  font-size: 20px;
  font-weight: 600;

  cursor: pointer;

  transition:
    background 0.25s ease,
    transform 0.2s ease,
    box-shadow 0.25s ease;
}

.stage-circle:hover {
  transform: scale(1.08);
}

.stage-circle.completed {
  background: #d97757;
  color: #ffffff;

  box-shadow: 0 0 0 5px rgba(217, 119, 87, 0.08);
}

.stage-circle.pending {
  background: #e2e1df;
  color: #ffffff;
}

.stage-circle.last-stage.pending {
  background: #b9b7b3;
}

.stage-circle.last-stage.completed {
  background: #d97757;
}

/* --------------------------------
   STAGE CONTENT
-------------------------------- */

.stage-content {
  width: 100%;

  display: flex;
  flex-direction: column;
  align-items: center;

  margin-top: 16px;

  padding: 0 8px;

  box-sizing: border-box;
}

.stage-name {
  min-height: 42px;

  display: flex;
  align-items: flex-start;
  justify-content: center;

  text-align: center;

  color: #3f4b59;

  font-size: 14px;
  font-weight: 500;
  line-height: 1.45;
}

.stage-date {
  width: 100%;
  max-width: 125px;

  margin-top: 7px;

  padding: 0;

  border: none;
  outline: none;

  background: transparent;

  color: #8c9299;

  font-family: inherit;
  font-size: 13px;

  text-align: center;

  transition: color 0.2s ease;
}

.stage-date::placeholder {
  color: #a5a5a5;
  opacity: 1;
}

.stage-date.filled {
  color: #777d84;
}

.stage-date:not([readonly]) {
  height: 32px;

  padding: 0 8px;

  border: 1px solid #e6e3dd;
  border-radius: 8px;

  background: #ffffff;
}

.stage-date:not([readonly]):focus {
  border-color: #d97757;

  box-shadow: 0 0 0 3px rgba(217, 119, 87, 0.08);
}

/* --------------------------------
   RESPONSIVE
-------------------------------- */

@media (max-width: 1000px) {
  .tracking-card {
    overflow-x: auto;
  }

  .tracking-header {
    min-width: 900px;
  }

  .process-container {
    min-width: 900px;
  }
}

@media (max-width: 700px) {
  .tracking-card {
    padding: 22px;
  }
}
</style>
