<script setup>
import { ref } from 'vue'

const totalProcessDays = ref(15)
const cvToCloseDays = ref(10)

const recruitmentSource = ref('LinkedIn')
const processResponsible = ref('María García')

const comments = ref(
  'El proceso se desarrolló de acuerdo con los tiempos establecidos. Se recibieron candidatos con experiencia relevante para la posición.'
)

const isEditing = ref(false)

function toggleEditing() {
  isEditing.value = !isEditing.value
}

function saveChanges() {
  isEditing.value = false
}
</script>

<template>
  <section class="analysis-card">
    <!-- HEADER -->
    <div class="analysis-header">
      <div class="analysis-title">
        <div class="title-icon">✦</div>

        <h2>Análisis final</h2>
      </div>

      <div class="header-actions">
        <button class="edit-button" type="button" @click="toggleEditing">
          <span>✎</span>
          Editar
        </button>

        <button v-if="isEditing" class="btn btn-primary" type="button" @click="saveChanges">
          <span>✓</span>
          Guardar cambios
        </button>
      </div>
    </div>

    <!-- METRICS -->
    <div class="metrics-grid">
      <!-- TOTAL PROCESS DAYS -->
      <div class="metric-card">
        <div class="metric-icon">◷</div>

        <div class="metric-content">
          <span class="metric-label"> Días totales del proceso </span>

          <strong class="metric-value">
            {{ totalProcessDays }}
          </strong>

          <span class="metric-description"> Requerimiento recibido hasta cierre </span>
        </div>
      </div>

      <!-- CV TO CLOSE -->
      <div class="metric-card">
        <div class="metric-icon">◷</div>

        <div class="metric-content">
          <span class="metric-label"> Días desde CVs hasta cierre </span>

          <strong class="metric-value">
            {{ cvToCloseDays }}
          </strong>

          <span class="metric-description"> Desde carga de candidatos hasta cierre </span>
        </div>
      </div>

      <!-- RECRUITMENT SOURCE -->
      <div class="info-field">
        <label> Fuente de reclutamiento </label>

        <select v-model="recruitmentSource" :disabled="!isEditing">
          <option value="LinkedIn">LinkedIn</option>

          <option value="Computrabajo">Computrabajo</option>

          <option value="Indeed">Indeed</option>

          <option value="Bumeran">Bumeran</option>

          <option value="Referidos">Referidos</option>

          <option value="Otros">Otros</option>
        </select>
      </div>

      <!-- RESPONSIBLE -->
      <div class="info-field">
        <label> Responsable del proceso </label>

        <select v-model="processResponsible" :disabled="!isEditing">
          <option value="María García">María García</option>

          <option value="Juan Pérez">Juan Pérez</option>

          <option value="Ana Torres">Ana Torres</option>

          <option value="Carlos López">Carlos López</option>
        </select>
      </div>
    </div>

    <!-- COMMENTS -->
    <div class="comments-section">
      <label> Comentarios / Observaciones </label>

      <textarea
        v-model="comments"
        :readonly="!isEditing"
        placeholder="Escribe aquí cualquier comentario u observación sobre el proceso..."
      ></textarea>

      <div class="character-count">{{ comments.length }} caracteres</div>
    </div>
  </section>
</template>

<style scoped>
.analysis-card {
  width: 100%;
  box-sizing: border-box;

  margin-top: 30px;
  margin-bottom: 40px;

  padding: 28px 32px 32px;

  background: #ffffff;

  border: 1px solid #e6e3dd;
  border-radius: 18px;

  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
}

/* --------------------------------
   HEADER
-------------------------------- */

.analysis-header {
  display: flex;
  align-items: center;
  justify-content: space-between;

  margin-bottom: 30px;
}

.analysis-title {
  display: flex;
  align-items: center;
  gap: 12px;
}

.title-icon {
  width: 28px;
  height: 28px;

  display: flex;
  align-items: center;
  justify-content: center;

  color: #d97757;

  font-size: 22px;
}

.analysis-title h2 {
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
   METRICS
-------------------------------- */

.metrics-grid {
  display: grid;

  grid-template-columns:
    1.1fr
    1.1fr
    1fr
    1fr;

  gap: 18px;
}

.metric-card {
  min-height: 125px;

  display: flex;
  align-items: center;

  gap: 16px;

  padding: 20px;

  box-sizing: border-box;

  background: #faf9f7;

  border: 1px solid #eeeae4;
  border-radius: 14px;
}

.metric-icon {
  width: 44px;
  height: 44px;

  flex-shrink: 0;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 12px;

  background: #f4e8e3;

  color: #d97757;

  font-size: 22px;
}

.metric-content {
  display: flex;
  flex-direction: column;
}

.metric-label {
  color: #6b6560;

  font-size: 13px;
  line-height: 1.4;
}

.metric-value {
  margin-top: 3px;

  color: #2a2520;

  font-size: 28px;
  font-weight: 600;
  line-height: 1.2;
}

.metric-description {
  margin-top: 4px;

  color: #918b83;

  font-size: 12px;
}

/* --------------------------------
   INFORMATION FIELDS
-------------------------------- */

.info-field {
  display: flex;
  flex-direction: column;
  gap: 9px;

  justify-content: center;

  padding: 20px;

  background: #ffffff;

  border: 1px solid #e6e3dd;
  border-radius: 14px;
}

.info-field label,
.comments-section label {
  color: #4f4a45;

  font-size: 14px;
  font-weight: 500;
}

.info-field select {
  width: 100%;
  height: 48px;

  padding: 0 14px;

  box-sizing: border-box;

  background: #ffffff;

  border: 1px solid #e6e3dd;
  border-radius: 10px;

  color: #4f4a45;

  font-family: inherit;
  font-size: 14px;
}

.info-field select:focus {
  outline: none;

  border-color: #d97757;

  box-shadow: 0 0 0 3px rgba(217, 119, 87, 0.08);
}

.info-field select:disabled {
  appearance: none;

  background: #faf9f7;

  color: #4f4a45;

  cursor: default;
}

/* --------------------------------
   COMMENTS
-------------------------------- */

.comments-section {
  position: relative;

  display: flex;
  flex-direction: column;

  margin-top: 22px;
}

.comments-section textarea {
  width: 100%;
  min-height: 120px;

  margin-top: 9px;

  padding: 14px 16px;

  box-sizing: border-box;

  resize: vertical;

  border: 1px solid #e6e3dd;
  border-radius: 12px;

  background: #ffffff;

  color: #4f4a45;

  font-family: inherit;
  font-size: 14px;

  line-height: 1.5;
}

.comments-section textarea:focus {
  outline: none;

  border-color: #d97757;

  box-shadow: 0 0 0 3px rgba(217, 119, 87, 0.08);
}

.comments-section textarea[readonly] {
  background: #faf9f7;

  cursor: default;
}

.character-count {
  align-self: flex-end;

  margin-top: 6px;

  color: #918b83;

  font-size: 12px;
}

/* --------------------------------
   RESPONSIVE
-------------------------------- */

@media (max-width: 1100px) {
  .metrics-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 700px) {
  .analysis-card {
    padding: 22px;
  }

  .analysis-header {
    align-items: flex-start;
    gap: 20px;
  }

  .header-actions {
    flex-direction: column;
    align-items: stretch;
  }

  .metrics-grid {
    grid-template-columns: 1fr;
  }
}
</style>
