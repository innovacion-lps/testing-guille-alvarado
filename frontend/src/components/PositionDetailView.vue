<script setup>
import { computed, ref } from 'vue'
import AdministrativeInfoView from './AdministrativeInfoView.vue'
import ProcessTrackingView from './ProcessTrackingView.vue'
import FinalAnalysisView from './FinalAnalysisView.vue'
import SidebarMain from './SidebarMain.vue'

const props = defineProps({
  position: { type: Object, default: null }
})

const emit = defineEmits(['back'])

const fallbackPosition = ref({
  title: 'Senior Backend Developer',
  department: 'Tecnología',
  location: 'Lima, Perú',
  modality: 'Remoto',
  contract: 'Tiempo completo',
  status: 'active',
  description: 'Buscamos un Senior Backend Developer...',
  salaryMin: 5000,
  salaryMax: 7000,
  currency: 'PEN',
  country: 'Perú',
  cvSource: 'LinkedIn'
})

const position = computed(() => props.position ?? fallbackPosition.value)

const requirements = ref([
  {
    id: 1,
    title: 'Experiencia con Python',
    description: 'Experiencia profesional desarrollando aplicaciones con Python.',
    type: 'score'
  },
  {
    id: 2,
    title: 'Experiencia con FastAPI',
    description: 'Experiencia desarrollando APIs utilizando FastAPI.',
    type: 'score'
  },
  {
    id: 3,
    title: 'Conocimientos de PostgreSQL',
    description: 'Experiencia trabajando con bases de datos PostgreSQL.',
    type: 'score'
  },
  {
    id: 4,
    title: 'Experiencia mínima de 3 años',
    description: 'Al menos 3 años de experiencia profesional en backend.',
    type: 'boolean'
  }
])

const candidates = ref([
  {
    id: 1,
    name: 'María López',
    initials: 'ML',
    status: 'screening',
    requirements: '8/9',
    source: 'LinkedIn'
  },
  {
    id: 2,
    name: 'Carlos Pérez',
    initials: 'CP',
    status: 'shortlist',
    requirements: '9/9',
    source: 'LinkedIn'
  },
  {
    id: 3,
    name: 'Ana Torres',
    initials: 'AT',
    status: 'interview',
    requirements: '8/9',
    source: 'Computrabajo'
  }
])

const stats = {
  candidates: 24,
  screening: 18,
  shortlist: 6,
  interviews: 3
}

const showMoreRequirements = ref(false)

const visibleRequirements = computed(() => {
  if (showMoreRequirements.value) {
    return requirements.value
  }

  return requirements.value.slice(0, 4)
})

function toggleRequirements() {
  showMoreRequirements.value = !showMoreRequirements.value
}

function statusLabel(status) {
  const labels = {
    screening: 'Screening',
    shortlist: 'Shortlist',
    interview: 'Entrevista'
  }

  return labels[status] || status
}

function statusClass(status) {
  return `status-${status}`
}
</script>

<template>
  <div class="dashboard">
    <SidebarMain />
    <main class="position-page">
    <!-- TOP BAR -->
    <header class="topbar">
      <div class="breadcrumb">
        <button class="back-button" @click="emit('back')">←</button>

        <span>Posiciones</span>
        <span class="breadcrumb-separator">/</span>
        <strong>{{ position.title }}</strong>
      </div>
    </header>

    <!-- POSITION HEADER -->
    <section class="position-header">
      <div class="position-heading">
        <div class="position-icon">
          <span>⌘</span>
        </div>

        <div>
          <div class="eyebrow">PROCESO DE SELECCIÓN</div>

          <h1>{{ position.title }}</h1>

          <div class="position-meta">
            <span>{{ position.department }}</span>
            <span>·</span>
            <span>{{ position.location }}</span>
            <span>·</span>

            <span class="status-pill">
              <span class="status-dot"></span>
              Activa
            </span>
          </div>
        </div>
      </div>

      <div class="header-actions">
        <button class="secondary-button">Editar posición</button>

        <button class="more-button">···</button>
      </div>
    </section>

    <!-- PROCESS METRICS -->
    <section class="metrics-grid">
      <article class="metric-card">
        <span class="metric-label"> Candidatos </span>

        <strong class="metric-value">
          {{ stats.candidates }}
        </strong>

        <span class="metric-description"> candidatos recibidos </span>
      </article>

      <article class="metric-card">
        <span class="metric-label"> Screening </span>

        <strong class="metric-value">
          {{ stats.screening }}
        </strong>

        <span class="metric-description"> en evaluación </span>
      </article>

      <article class="metric-card metric-highlight">
        <span class="metric-label"> Shortlist </span>

        <strong class="metric-value">
          {{ stats.shortlist }}
        </strong>

        <span class="metric-description"> candidatos seleccionados </span>
      </article>

      <article class="metric-card">
        <span class="metric-label"> Entrevistas </span>

        <strong class="metric-value">
          {{ stats.interviews }}
        </strong>

        <span class="metric-description"> programadas </span>
      </article>
    </section>

    <!-- MAIN CONTENT -->
    <section class="content-grid">
      <!-- LEFT -->
      <div class="main-column">
        <!-- DESCRIPTION -->
        <article class="content-card">
          <div class="card-header">
            <div>
              <span class="section-eyebrow"> POSICIÓN </span>

              <h2>Información de la posición</h2>
            </div>
          </div>

          <p class="description">
            {{ position.description }}
          </p>

          <div class="details-grid">
            <div class="detail-item">
              <span>Departamento</span>
              <strong>{{ position.department }}</strong>
            </div>

            <div class="detail-item">
              <span>Ubicación</span>
              <strong>{{ position.location }}</strong>
            </div>

            <div class="detail-item">
              <span>Modalidad</span>
              <strong>{{ position.modality }}</strong>
            </div>

            <div class="detail-item">
              <span>Tipo de contrato</span>
              <strong>{{ position.contract }}</strong>
            </div>

            <div class="detail-item">
              <span>Banda salarial</span>

              <strong>
                {{ position.currency }}
                {{ (position.salary_min ?? position.salaryMin ?? null)?.toLocaleString?.() ?? '—' }}
                —
                {{ position.currency }}
                {{ (position.salary_max ?? position.salaryMax ?? null)?.toLocaleString?.() ?? '—' }}
              </strong>
            </div>

            <div class="detail-item">
              <span>Fuente del CV</span>
              <strong>{{ position.cvSource }}</strong>
            </div>
          </div>
        </article>

        <!-- CANDIDATES -->
        <article class="content-card">
          <div class="card-header candidates-header">
            <div>
              <span class="section-eyebrow"> TALENTO </span>

              <h2>Candidatos recientes</h2>
            </div>

            <button class="text-button">Ver todos →</button>
          </div>

          <div class="candidate-list">
            <div v-for="candidate in candidates" :key="candidate.id" class="candidate-row">
              <div class="candidate-avatar">
                {{ candidate.initials }}
              </div>

              <div class="candidate-info">
                <strong>{{ candidate.name }}</strong>

                <span>
                  {{ candidate.source }}
                </span>
              </div>

              <div class="candidate-match">
                <strong>{{ candidate.requirements }}</strong>

                <span> requisitos </span>
              </div>

              <span class="candidate-status" :class="statusClass(candidate.status)">
                {{ statusLabel(candidate.status) }}
              </span>

              <button class="candidate-arrow">→</button>
            </div>
          </div>
        </article>
      </div>

      <!-- RIGHT -->
      <aside class="side-column">
        <!-- REQUIREMENTS -->
        <article class="content-card">
          <div class="card-header">
            <div>
              <span class="section-eyebrow"> EVALUACIÓN </span>

              <h2>Requisitos</h2>
            </div>

            <span class="requirements-count">
              {{ requirements.length }}
            </span>
          </div>

          <div class="requirements-list">
            <div
              v-for="requirement in visibleRequirements"
              :key="requirement.id"
              class="requirement-item"
            >
              <div class="requirement-check">✓</div>

              <div class="requirement-content">
                <strong>
                  {{ requirement.title }}
                </strong>

                <p>
                  {{ requirement.description }}
                </p>
              </div>
            </div>
          </div>

          <button
            v-if="requirements.length > 4"
            class="requirements-more"
            @click="toggleRequirements"
          >
            {{ showMoreRequirements ? 'Mostrar menos' : `Ver ${requirements.length - 4} más` }}
          </button>
        </article>

        <!-- PROCESS -->
        <article class="content-card process-card">
          <span class="section-eyebrow"> PROCESO </span>

          <h2>Estado del proceso</h2>

          <div class="process-line">
            <div class="process-step active">
              <span class="process-number">1</span>

              <div>
                <strong>Screening</strong>
                <span>18 candidatos</span>
              </div>
            </div>

            <div class="process-step">
              <span class="process-number">2</span>

              <div>
                <strong>Shortlist</strong>
                <span>6 candidatos</span>
              </div>
            </div>

            <div class="process-step">
              <span class="process-number">3</span>

              <div>
                <strong>Entrevista</strong>
                <span>3 candidatos</span>
              </div>
            </div>

            <div class="process-step">
              <span class="process-number">4</span>

              <div>
                <strong>Decisión</strong>
                <span>Pendiente</span>
              </div>
            </div>
          </div>
        </article>
      </aside>
    </section>
    <AdministrativeInfoView :position="position" />
    <ProcessTrackingView />
    <FinalAnalysisView />
    </main>
  </div>
</template>

<style scoped>
.dashboard {
  min-height: 100vh;
  display: flex;
  background: #f7f3ed;
}

.position-page {
  flex: 1;
  min-width: 0;
  min-height: 100vh;
  padding: 28px 42px 60px;
  background: #f7f3ed;
  color: #29231e;
  font-family: 'DM Sans', sans-serif;
}

/* TOPBAR */

.topbar {
  margin-bottom: 26px;
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 9px;
  color: #918b83;
  font-size: 0.82rem;
}

.breadcrumb strong {
  color: #6b6560;
  font-weight: 500;
}

.breadcrumb-separator {
  color: #c8c0b8;
}

.back-button {
  width: 32px;
  height: 32px;
  border: 1px solid #e7e0d7;
  border-radius: 8px;
  background: #fffdfb;
  color: #6b6560;
  cursor: pointer;
  font-size: 1rem;
  margin-right: 4px;
}

.back-button:hover {
  background: #f4e8e3;
  color: #d97757;
}

/* HEADER */

.position-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 30px;
  margin-bottom: 30px;
}

.position-heading {
  display: flex;
  align-items: flex-start;
  gap: 18px;
}

.position-icon {
  width: 54px;
  height: 54px;
  border-radius: 14px;
  background: #f4e5de;
  color: #d97757;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.45rem;
  flex-shrink: 0;
}

.eyebrow,
.section-eyebrow {
  display: block;
  margin-bottom: 6px;
  color: #a0978e;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.12em;
}

.position-heading h1 {
  margin: 0 0 8px;
  font-family: 'Crimson Pro', serif;
  font-size: 2.3rem;
  font-weight: 600;
  letter-spacing: -0.02em;
}

.position-meta {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 7px;
  color: #6b6560;
  font-size: 0.86rem;
}

.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: #5f8b69;
}

.status-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #6b9f78;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 9px;
}

.secondary-button,
.more-button {
  border: 1px solid #ddd5cc;
  background: #fffdfb;
  color: #514a44;
  border-radius: 8px;
  cursor: pointer;
  font-family: inherit;
}

.secondary-button {
  padding: 10px 16px;
  font-size: 0.84rem;
}

.secondary-button:hover {
  border-color: #d97757;
  color: #d97757;
}

.more-button {
  width: 40px;
  height: 40px;
  font-size: 1rem;
}

/* METRICS */

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 20px;
}

.metric-card {
  padding: 20px 22px;
  border: 1px solid #e7e0d7;
  border-radius: 12px;
  background: #fffdfb;
}

.metric-highlight {
  border-color: #efd7cc;
  background: #fff8f5;
}

.metric-label {
  display: block;
  color: #918b83;
  font-size: 0.75rem;
  margin-bottom: 8px;
}

.metric-value {
  display: block;
  font-family: 'Crimson Pro', serif;
  font-size: 1.9rem;
  line-height: 1;
  font-weight: 600;
}

.metric-description {
  display: block;
  margin-top: 7px;
  color: #918b83;
  font-size: 0.72rem;
}

/* CONTENT */

.content-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.7fr) minmax(300px, 0.9fr);
  gap: 20px;
}

.main-column,
.side-column {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.content-card {
  border: 1px solid #e7e0d7;
  border-radius: 12px;
  background: #fffdfb;
  padding: 24px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 20px;
  margin-bottom: 20px;
}

.card-header h2 {
  margin: 0;
  font-family: 'Crimson Pro', serif;
  font-size: 1.4rem;
  font-weight: 600;
}

.description {
  margin: 0 0 24px;
  color: #6b6560;
  font-size: 0.9rem;
  line-height: 1.7;
}

/* DETAILS */

.details-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  border-top: 1px solid #eee9e3;
  border-left: 1px solid #eee9e3;
}

.detail-item {
  padding: 16px;
  border-right: 1px solid #eee9e3;
  border-bottom: 1px solid #eee9e3;
}

.detail-item span {
  display: block;
  margin-bottom: 5px;
  color: #918b83;
  font-size: 0.72rem;
}

.detail-item strong {
  color: #403932;
  font-size: 0.84rem;
  font-weight: 600;
}

/* CANDIDATES */

.candidates-header {
  align-items: center;
}

.text-button {
  border: none;
  background: transparent;
  color: #d97757;
  font-family: inherit;
  font-size: 0.8rem;
  cursor: pointer;
}

.text-button:hover {
  color: #c96643;
}

.candidate-list {
  display: flex;
  flex-direction: column;
}

.candidate-row {
  display: grid;
  grid-template-columns: 40px minmax(0, 1fr) 80px 100px 28px;
  align-items: center;
  gap: 13px;
  padding: 14px 4px;
  border-top: 1px solid #eee9e3;
}

.candidate-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f4e5de;
  color: #b96345;
  font-size: 0.72rem;
  font-weight: 700;
}

.candidate-info {
  min-width: 0;
}

.candidate-info strong {
  display: block;
  margin-bottom: 3px;
  color: #403932;
  font-size: 0.84rem;
}

.candidate-info span {
  color: #918b83;
  font-size: 0.7rem;
}

.candidate-match {
  text-align: right;
}

.candidate-match strong {
  display: block;
  color: #403932;
  font-size: 0.82rem;
}

.candidate-match span {
  color: #918b83;
  font-size: 0.65rem;
}

.candidate-status {
  justify-self: end;
  padding: 5px 8px;
  border-radius: 999px;
  font-size: 0.66rem;
  font-weight: 600;
}

.status-screening {
  background: #f4e8e3;
  color: #a85f45;
}

.status-shortlist {
  background: #edf3ed;
  color: #62806a;
}

.status-interview {
  background: #f5efe1;
  color: #9b7a3f;
}

.candidate-arrow {
  border: none;
  background: transparent;
  color: #aaa19a;
  cursor: pointer;
  font-size: 1rem;
}

.candidate-arrow:hover {
  color: #d97757;
}

/* REQUIREMENTS */

.requirements-count {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 24px;
  height: 24px;
  padding: 0 7px;
  border-radius: 999px;
  background: #f4e5de;
  color: #d97757;
  font-size: 0.7rem;
  font-weight: 700;
}

.requirements-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.requirement-item {
  display: flex;
  gap: 11px;
  align-items: flex-start;
}

.requirement-check {
  width: 21px;
  height: 21px;
  flex-shrink: 0;
  border-radius: 50%;
  background: #edf3ed;
  color: #6b9f78;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.68rem;
  font-weight: 700;
}

.requirement-content strong {
  display: block;
  margin-bottom: 3px;
  color: #403932;
  font-size: 0.78rem;
}

.requirement-content p {
  margin: 0;
  color: #918b83;
  font-size: 0.7rem;
  line-height: 1.45;
}

.requirements-more {
  width: 100%;
  margin-top: 18px;
  padding: 9px;
  border: 1px solid #e7e0d7;
  border-radius: 7px;
  background: transparent;
  color: #d97757;
  cursor: pointer;
  font-family: inherit;
  font-size: 0.75rem;
}

.requirements-more:hover {
  background: #f4e8e3;
}

/* PROCESS */

.process-card h2 {
  margin: 0 0 22px;
  font-family: 'Crimson Pro', serif;
  font-size: 1.4rem;
  font-weight: 600;
}

.process-line {
  display: flex;
  flex-direction: column;
}

.process-step {
  display: grid;
  grid-template-columns: 30px 1fr;
  gap: 10px;
  position: relative;
  padding-bottom: 20px;
}

.process-step:last-child {
  padding-bottom: 0;
}

.process-step:not(:last-child)::after {
  content: '';
  position: absolute;
  left: 14px;
  top: 30px;
  width: 1px;
  height: calc(100% - 10px);
  background: #e7e0d7;
}

.process-number {
  width: 29px;
  height: 29px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #e1dad2;
  border-radius: 50%;
  background: #fffdfb;
  color: #918b83;
  font-size: 0.7rem;
  position: relative;
  z-index: 1;
}

.process-step.active .process-number {
  border-color: #d97757;
  background: #f4e5de;
  color: #d97757;
}

.process-step strong {
  display: block;
  margin-top: 3px;
  color: #403932;
  font-size: 0.78rem;
}

.process-step div span {
  display: block;
  margin-top: 3px;
  color: #918b83;
  font-size: 0.68rem;
}

/* RESPONSIVE */

@media (max-width: 1050px) {
  .position-page {
    padding: 24px;
  }

  .content-grid {
    grid-template-columns: 1fr;
  }

  .side-column {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 760px) {
  .position-header {
    flex-direction: column;
  }

  .metrics-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .side-column {
    display: flex;
  }

  .candidate-row {
    grid-template-columns: 40px minmax(0, 1fr) 28px;
  }

  .candidate-match,
  .candidate-status {
    display: none;
  }
}

@media (max-width: 520px) {
  .position-page {
    padding: 18px;
  }

  .position-heading h1 {
    font-size: 1.8rem;
  }

  .metrics-grid {
    grid-template-columns: 1fr 1fr;
  }

  .content-card {
    padding: 18px;
  }

  .details-grid {
    grid-template-columns: 1fr;
  }
}
</style>
