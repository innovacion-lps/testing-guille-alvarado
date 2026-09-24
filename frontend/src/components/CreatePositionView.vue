<script setup>
import { ref } from 'vue'
import SidebarMain from './SidebarMain.vue'
const emit = defineEmits(['cancel'])

const requirements = ref([
  {
    id: 1,
    text: 'Experiencia con Python',
    required: true
  },
  {
    id: 2,
    text: 'Experiencia con FastAPI',
    required: true
  },
  {
    id: 3,
    text: 'Conocimientos de PostgreSQL',
    required: true
  }
])

const newRequirement = ref('')

function addRequirement() {
  const value = newRequirement.value.trim()

  if (!value) return

  requirements.value.push({
    id: Date.now(),
    text: value,
    required: true
  })

  newRequirement.value = ''
}

function removeRequirement(id) {
  requirements.value = requirements.value.filter(requirement => requirement.id !== id)
}
</script>

<template>
  <div class="dashboard">
    <SidebarMain />
    <main class="create-position-page">
      <!-- HEADER -->
      <header class="page-header">
        <div class="breadcrumb">
          <span>Inicio</span>
          <span class="breadcrumb-separator">/</span>
          <span>Posiciones</span>
          <span class="breadcrumb-separator">/</span>
          <span class="current">Nueva posición</span>
        </div>

        <div class="header-content">
          <div>
            <span class="eyebrow"> NUEVO PROCESO </span>

            <h1>Crear posición</h1>

            <p>
              Define la posición y los criterios que utilizaremos para evaluar a los candidatos.
            </p>
          </div>

          <div class="header-actions">
            <button class="cancel-button" @click="emit('cancel')">Cancelar</button>

            <button class="create-button">Crear posición</button>
          </div>
        </div>
      </header>

      <!-- CONTENT -->
      <div class="form-layout">
        <!-- MAIN FORM -->
        <section class="form-column">
          <!-- POSITION INFORMATION -->
          <div class="form-card">
            <div class="card-heading">
              <div class="card-number">01</div>

              <div>
                <h2>Información de la posición</h2>

                <p>Información básica de la vacante.</p>
              </div>
            </div>

            <div class="form-grid">
              <div class="field field-full">
                <label> Nombre de la posición </label>

                <input type="text" placeholder="Ej. Senior Backend Developer" />
              </div>

              <div class="field">
                <label> Departamento </label>

                <select>
                  <option value="">Seleccionar departamento</option>

                  <option>Tecnología</option>

                  <option>Recursos Humanos</option>

                  <option>Finanzas</option>

                  <option>Marketing</option>

                  <option>Diseño</option>
                </select>
              </div>

              <div class="field">
                <label> Modalidad </label>

                <select>
                  <option>Presencial</option>

                  <option>Híbrido</option>

                  <option>Remoto</option>
                </select>
              </div>

              <div class="field">
                <label> Tipo de contrato </label>

                <select>
                  <option>Tiempo completo</option>

                  <option>Tiempo parcial</option>

                  <option>Temporal</option>

                  <option>Freelance</option>
                </select>
              </div>

              <div class="field">
                <label> Ubicación </label>

                <input type="text" placeholder="Ej. Lima, Perú" />
              </div>
            </div>
          </div>

          <!-- DESCRIPTION -->
          <div class="form-card">
            <div class="card-heading">
              <div class="card-number">02</div>

              <div>
                <h2>Descripción</h2>

                <p>Describe el objetivo y las responsabilidades del puesto.</p>
              </div>
            </div>

            <div class="field">
              <label> Descripción del puesto </label>

              <textarea
                rows="7"
                placeholder="Describe brevemente el propósito de esta posición, sus principales responsabilidades y el contexto del equipo..."
              ></textarea>
              <span class="field-hint">
                Una descripción clara ayudará a evaluar mejor a los candidatos.
              </span>
            </div>
          </div>

          <!-- REQUIREMENTS -->
          <div class="form-card">
            <div class="card-heading">
              <div class="card-number">03</div>

              <div>
                <h2>Requisitos</h2>

                <p>Define los criterios que utilizaremos durante el screening.</p>
              </div>
            </div>

            <div class="requirements-section">
              <div class="requirements-label">
                <div>
                  <strong> Requisitos del puesto </strong>

                  <span> {{ requirements.length }} definidos </span>
                </div>
              </div>

              <div class="requirements-list">
                <div
                  v-for="requirement in requirements"
                  :key="requirement.id"
                  class="requirement-item"
                >
                  <div class="requirement-check">✓</div>

                  <span class="requirement-text">
                    {{ requirement.text }}
                  </span>

                  <span v-if="requirement.required" class="required-badge"> Obligatorio </span>

                  <button class="remove-requirement" @click="removeRequirement(requirement.id)">
                    ×
                  </button>
                </div>
              </div>

              <div class="add-requirement">
                <input
                  v-model="newRequirement"
                  type="text"
                  placeholder="Ej. Experiencia con Docker"
                  @keyup.enter="addRequirement"
                />

                <button class="add-requirement-button" @click="addRequirement">+ Agregar</button>
              </div>
            </div>
          </div>

          <!-- PROCESS CONFIGURATION -->
          <div class="form-card">
            <div class="card-heading">
              <div class="card-number">04</div>

              <div>
                <h2>Configuración del proceso</h2>

                <p>Define cómo quieres gestionar esta posición.</p>
              </div>
            </div>

            <div class="process-options">
              <div class="process-option">
                <div class="option-content">
                  <strong> Screening automático </strong>

                  <span> Analizar automáticamente los CV según los requisitos definidos. </span>
                </div>

                <label class="switch">
                  <input type="checkbox" checked />

                  <span class="slider"></span>
                </label>
              </div>

              <div class="process-option">
                <div class="option-content">
                  <strong> Notificaciones </strong>

                  <span> Recibir avisos cuando nuevos candidatos sean evaluados. </span>
                </div>

                <label class="switch">
                  <input type="checkbox" checked />

                  <span class="slider"></span>
                </label>
              </div>
            </div>
          </div>
        </section>

        <!-- SUMMARY -->
        <aside class="summary-column">
          <div class="summary-card">
            <span class="summary-eyebrow"> RESUMEN </span>

            <h3>Nueva posición</h3>

            <p>Revisa la información antes de crear el proceso.</p>

            <div class="summary-divider"></div>
            <div class="summary-item">
              <span> Posición </span>

              <strong> Sin definir </strong>
            </div>

            <div class="summary-item">
              <span> Departamento </span>

              <strong> Sin definir </strong>
            </div>

            <div class="summary-item">
              <span> Requisitos </span>

              <strong>
                {{ requirements.length }}
              </strong>
            </div>

            <div class="summary-divider"></div>
            <div class="summary-note">
              <div class="note-icon">✦</div>

              <p>
                Los requisitos definidos aquí serán utilizados posteriormente para evaluar los CV de
                los candidatos.
              </p>
            </div>
          </div>

          <div class="help-card">
            <div class="help-icon">?</div>

            <div>
              <strong> ¿Necesitas ayuda? </strong>

              <p>Puedes modificar los requisitos después de crear la posición.</p>
            </div>
          </div>
        </aside>
      </div>
    </main>
  </div>
</template>

<style scoped>
.dashboard {
  min-height: 100vh;
  display: flex;
  background: #f7f3ed;
}
.main-content {
  flex: 1;
  min-width: 0;
}

* {
  box-sizing: border-box;
}

.create-position-page {
  flex: 1;
  min-width: 0;
  min-height: 100vh;
  padding: 38px 46px 70px;
  background: #f7f3ed;
  color: #29231e;
}

/* HEADER */

.page-header {
  max-width: 100%;
  margin: 0 0 32px;
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 9px;
  margin-bottom: 24px;
  color: #918b83;
  font-size: 12px;
}

.breadcrumb-separator {
  color: #c8c0b7;
}

.breadcrumb .current {
  color: #6b6560;
}

.header-content {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 30px;
}

.eyebrow {
  display: block;
  margin-bottom: 8px;
  color: #d97757;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.6px;
}

.header-content h1 {
  margin: 0 0 8px;
  font-size: 34px;
  font-weight: 600;
  letter-spacing: -1px;
}

.header-content p {
  max-width: 620px;
  margin: 0;
  color: #6b6560;
  font-size: 14px;
  line-height: 1.6;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.cancel-button,
.create-button {
  padding: 11px 18px;
  border-radius: 10px;
  font-family: inherit;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.cancel-button {
  background: transparent;
  border: 1px solid #ded7ce;
  color: #6b6560;
}

.cancel-button:hover {
  background: #fffdfb;
}

.create-button {
  background: #d97757;
  border: 1px solid #d97757;
  color: white;
  box-shadow: 0 5px 15px rgba(217, 119, 87, 0.18);
}

.create-button:hover {
  background: #c96643;
}

/* LAYOUT */

.form-layout {
  max-width: 100%;
  margin: 0;
  display: grid;
  grid-template-columns: minmax(0, 1fr) 320px;
  gap: 24px;
  align-items: start;
}

.form-column {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* CARDS */

.form-card {
  padding: 27px 30px;
  background: #fffdfb;
  border: 1px solid #e7e0d7;
  border-radius: 16px;
  box-shadow: 0 5px 20px rgba(42, 37, 32, 0.025);
}

.card-heading {
  display: flex;
  gap: 14px;
  margin-bottom: 26px;
}

.card-number {
  width: 31px;
  height: 31px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 9px;
  background: #f4e5de;
  color: #d97757;
  font-size: 10px;
  font-weight: 700;
}

.card-heading h2 {
  margin: 1px 0 4px;
  font-size: 17px;
  font-weight: 600;
}

.card-heading p {
  margin: 0;
  color: #918b83;
  font-size: 12px;
}

/* FORM */

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 19px;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.field-full {
  grid-column: 1 / -1;
}

.field label {
  color: #4d4741;
  font-size: 12px;
  font-weight: 600;
}

.field input,
.field select,
.field textarea,
.add-requirement input {
  width: 100%;
  padding: 11px 13px;
  background: #fff;
  border: 1px solid #e3ddd5;
  border-radius: 9px;
  outline: none;
  color: #29231e;
  font-family: inherit;
  font-size: 13px;
  transition:
    border-color 0.2s ease,
    box-shadow 0.2s ease;
}

.field input::placeholder,
.field textarea::placeholder,
.add-requirement input::placeholder {
  color: #b0aaa2;
}

.field input:focus,
.field select:focus,
.field textarea:focus,
.add-requirement input:focus {
  border-color: #d97757;
  box-shadow: 0 0 0 3px rgba(217, 119, 87, 0.08);
}

.field textarea {
  resize: vertical;
  line-height: 1.6;
}

.field-hint {
  color: #a39c94;
  font-size: 11px;
}

/* REQUIREMENTS */

.requirements-section {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.requirements-label {
  display: flex;
  justify-content: space-between;
}

.requirements-label strong {
  font-size: 12px;
  font-weight: 600;
}

.requirements-label span {
  margin-left: 8px;
  color: #918b83;
  font-size: 11px;
}

.requirements-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.requirement-item {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 45px;
  padding: 9px 11px;
  background: #faf8f5;
  border: 1px solid #eee8e1;
  border-radius: 9px;
}

.requirement-check {
  width: 23px;
  height: 23px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 7px;
  background: #f4e5de;
  color: #d97757;
  font-size: 11px;
  font-weight: 700;
}

.requirement-text {
  flex: 1;
  color: #4d4741;
  font-size: 12px;
}

.required-badge {
  padding: 4px 7px;
  border-radius: 5px;
  background: #f4e5de;
  color: #b65e43;
  font-size: 9px;
  font-weight: 700;
}

.remove-requirement {
  width: 25px;
  height: 25px;
  border: none;
  background: transparent;
  color: #aaa29a;
  font-size: 17px;
  cursor: pointer;
}

.remove-requirement:hover {
  color: #c94b4b;
}

.add-requirement {
  display: flex;
  gap: 9px;
}

.add-requirement-button {
  flex-shrink: 0;
  padding: 0 15px;
  border: 1px solid #e3ddd5;
  border-radius: 9px;
  background: #fff;
  color: #6b6560;
  font-family: inherit;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.add-requirement-button:hover {
  background: #f7f3ed;
  border-color: #d8cfc5;
  color: #29231e;
}

/* PROCESS OPTIONS */

.process-options {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.process-option {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 16px 0;
  border-bottom: 1px solid #eee8e1;
}

.process-option:first-child {
  padding-top: 0;
}

.process-option:last-child {
  padding-bottom: 0;
  border-bottom: none;
}

.option-content {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.option-content strong {
  color: #4d4741;
  font-size: 12px;
}

.option-content span {
  max-width: 550px;
  color: #918b83;
  font-size: 11px;
  line-height: 1.5;
}

/* SWITCH */

.switch {
  position: relative;
  width: 40px;
  height: 22px;
  flex-shrink: 0;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  background: #d9d2ca;
  cursor: pointer;
  transition: 0.2s;
}

.slider::before {
  content: '';
  position: absolute;
  width: 16px;
  height: 16px;
  left: 3px;
  top: 3px;
  border-radius: 50%;
  background: white;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.15);
  transition: 0.2s;
}

.switch input:checked + .slider {
  background: #d97757;
}

.switch input:checked + .slider::before {
  transform: translateX(18px);
}

/* SUMMARY */

.summary-column {
  position: sticky;
  top: 25px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.summary-card {
  padding: 24px;
  background: #fffdfb;
  border: 1px solid #e7e0d7;
  border-radius: 16px;
  box-shadow: 0 5px 20px rgba(42, 37, 32, 0.025);
}

.summary-eyebrow {
  color: #d97757;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 1.4px;
}

.summary-card h3 {
  margin: 8px 0 5px;
  font-size: 18px;
  font-weight: 600;
}

.summary-card > p {
  margin: 0;
  color: #918b83;
  font-size: 11px;
  line-height: 1.5;
}

.summary-divider {
  height: 1px;
  margin: 19px 0;
  background: #eee8e1;
}

.summary-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 8px 0;
}

.summary-item span {
  color: #918b83;
  font-size: 11px;
}

.summary-item strong {
  color: #4d4741;
  font-size: 11px;
  font-weight: 600;
  text-align: right;
}

.summary-note {
  display: flex;
  gap: 10px;
  padding: 12px;
  background: #f9f1ed;
  border-radius: 9px;
}

.note-icon {
  color: #d97757;
  font-size: 14px;
}

.summary-note p {
  margin: 0;
  color: #7c6c63;
  font-size: 10px;
  line-height: 1.5;
}

/* HELP */

.help-card {
  display: flex;
  gap: 12px;
  padding: 16px;
  background: #f1ece5;
  border-radius: 13px;
}

.help-icon {
  width: 26px;
  height: 26px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: #fffdfb;
  color: #d97757;
  font-size: 12px;
  font-weight: 700;
}

.help-card strong {
  display: block;
  margin-bottom: 3px;
  color: #4d4741;
  font-size: 11px;
}

.help-card p {
  margin: 0;
  color: #918b83;
  font-size: 10px;
  line-height: 1.5;
}

/* RESPONSIVE */

@media (max-width: 1050px) {
  .form-layout {
    grid-template-columns: 1fr;
  }

  .summary-column {
    position: static;
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 700px) {
  .create-position-page {
    padding: 25px 16px 50px;
  }

  .header-content {
    align-items: flex-start;
    flex-direction: column;
  }

  .header-actions {
    width: 100%;
  }

  .cancel-button,
  .create-button {
    flex: 1;
  }

  .form-grid {
    grid-template-columns: 1fr;
  }

  .field-full {
    grid-column: auto;
  }

  .form-card {
    padding: 22px 18px;
  }

  .summary-column {
    grid-template-columns: 1fr;
  }

  .add-requirement {
    flex-direction: column;
  }

  .add-requirement-button {
    height: 40px;
  }
}
</style>
