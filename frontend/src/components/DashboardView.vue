<script setup>
import { computed, onMounted, ref } from 'vue'
const emit = defineEmits(['new-position'])
import api from '../services/api'

import TaskForm from '../components/TaskForm.vue'
import TaskItem from '../components/TaskItem.vue'
import CreatePositionDialog from '../components/CreatePositionDialog.vue'
import SidebarMain from '../components/SidebarMain.vue'
const showTasksModal = ref(false)
const showPositionDialog = ref(false)
function openPositionDialog() {
  showPositionDialog.value = true
}
async function addPosition(position) {
  try {
    const payload = {
      title: position.title,
      description: position.description || null,
      country: position.country || null,
      currency: position.currency || null,
      salary_min: position.salaryMin ?? null,
      salary_max: position.salaryMax ?? null,
      requirements: position.requirements || []
    }
    const response = await api.post('/positions', payload)
    positions.value.push(response.data)
  } catch (error) {
    console.error('Error creando posición:', error)
  }
}
const tasks = ref([])
const positions = ref([])
async function getTasks() {
  try {
    const response = await api.get('/tasks')
    tasks.value = response.data
  } catch (error) {
    console.error('Error cargando tareas:', error)
  }
}
async function getPositions() {
  try {
    const response = await api.get('/positions')
    positions.value = response.data
  } catch (error) {
    console.error('Error cargando posiciones:', error)
  }
}
function openTasksModal() {
  showTasksModal.value = true
}

function closeTasksModal() {
  showTasksModal.value = false
}

function addTask(task) {
  tasks.value.push(task)
}

function updateTask(updatedTask) {
  const index = tasks.value.findIndex(task => task.id === updatedTask.id)

  if (index !== -1) {
    tasks.value[index] = updatedTask
  }
}

function removeTask(taskId) {
  tasks.value = tasks.value.filter(task => task.id !== taskId)
}

const pendingTasks = computed(() => {
  return tasks.value.filter(task => !task.completed).length
})

const activePositions = computed(() => {
  return positions.value.filter(p => p.status === 'active').length
})
const totalCandidates = computed(() => 0)
const totalShortlisted = computed(() => 0)

function statusLabel(status) {
  return status === 'active' ? 'Activa' : status === 'paused' ? 'Pausada' : status
}

onMounted(() => {
  getTasks()
  getPositions()
})
</script>

<template>
  <div class="dashboard">
    <!-- SIDEBAR -->
    <SidebarMain />

    <!-- CONTENIDO PRINCIPAL -->
    <main class="main-content">
      <!-- TOPBAR -->
      <header class="topbar">
        <div class="breadcrumb">
          <span>Workspace</span>
          <span class="breadcrumb-separator"> / </span>

          <strong>Inicio</strong>
        </div>

        <div class="user-area">
          <button class="notification-button" aria-label="Notificaciones">
            ♧

            <span class="notification-dot"></span>
          </button>

          <div class="user-profile">
            <div class="avatar">GA</div>

            <div class="user-info">
              <span class="user-name"> Guillermo Alvarado </span>

              <span class="user-role"> Recruiter </span>
            </div>

            <span class="dropdown-arrow"> ⌄ </span>
          </div>
        </div>
      </header>

      <!-- CONTENIDO -->
      <div class="page-content">
        <!-- INTRO -->
        <section class="page-intro">
          <div>
            <p class="eyebrow">DASHBOARD</p>

            <h1>Buenos días, Guillermo</h1>

            <p class="intro-description">
              Gestiona tus procesos de selección y encuentra el talento adecuado.
            </p>
          </div>

          <div class="intro-actions">
            <button class="secondary-button" @click="openPositionDialog">New position modal</button>
            <button class="secondary-button" @click="openTasksModal">My tasks</button>

            <button class="primary-button" @click="emit('new-position')">+ Nueva posición</button>
          </div>
        </section>

        <!-- MÉTRICAS -->
        <section class="metrics-grid">
          <article class="metric-card">
            <div class="metric-header">
              <span class="metric-label"> Posiciones activas </span>

              <div class="metric-icon orange">▣</div>
            </div>

            <div class="metric-value">
              {{ activePositions }}
            </div>

            <p class="metric-description">Procesos actualmente abiertos</p>
          </article>

          <article class="metric-card">
            <div class="metric-header">
              <span class="metric-label"> Candidatos </span>

              <div class="metric-icon beige">◉</div>
            </div>

            <div class="metric-value">
              {{ totalCandidates }}
            </div>

            <p class="metric-description">Candidatos en tus procesos</p>
          </article>

          <article class="metric-card">
            <div class="metric-header">
              <span class="metric-label"> En shortlist </span>

              <div class="metric-icon green">✓</div>
            </div>

            <div class="metric-value">
              {{ totalShortlisted }}
            </div>

            <p class="metric-description">Candidatos preseleccionados</p>
          </article>
        </section>

        <!-- PROCESOS -->
        <section class="positions-section">
          <div class="section-header">
            <div>
              <h2>Procesos de selección</h2>

              <p>Revisa el estado de tus posiciones abiertas.</p>
            </div>

            <button class="text-button">
              Ver todas
              <span>→</span>
            </button>
          </div>

          <div class="positions-list">
            <article v-for="position in positions" :key="position.id" class="position-card">
              <div class="position-main">
                <div class="position-title-row">
                  <div class="position-icon">
                    {{ position.title.charAt(0) }}
                  </div>

                  <div>
                    <h3>
                      {{ position.title }}
                    </h3>

                    <span class="department">
                      {{ position.department }}
                    </span>
                  </div>
                </div>

                <div class="position-stats">
                  <div class="position-stat">
                    <span class="stat-number">
                      {{ position.candidates }}
                    </span>

                    <span class="stat-label"> candidatos </span>
                  </div>

                  <div class="stat-divider"></div>
                  <div class="position-stat">
                    <span class="stat-number">
                      {{ position.shortlisted }}
                    </span>

                    <span class="stat-label"> shortlist </span>
                  </div>
                </div>
              </div>

              <div class="position-footer">
                <div class="position-status">
                  <span class="status-dot" :class="position.status"></span>
                  <span>
                    {{ statusLabel(position.status) }}
                  </span>
                </div>

                <span class="updated">
                  {{ position.updated }}
                </span>

                <button class="view-button">
                  Ver proceso
                  <span>→</span>
                </button>
              </div>
            </article>
          </div>
        </section>
      </div>
    </main>
  </div>
  <!-- TASKS MODAL -->
  <Teleport to="body">
    <div v-if="showTasksModal" class="modal-overlay" @click.self="closeTasksModal">
      <div class="tasks-modal">
        <header class="tasks-modal-header">
          <div>
            <span class="modal-eyebrow"> PERSONAL </span>

            <h2>My tasks</h2>

            <p>Organiza tus tareas pendientes.</p>
          </div>

          <button class="modal-close" @click="closeTasksModal" aria-label="Cerrar">×</button>
        </header>

        <div class="tasks-modal-divider"></div>
        <div class="tasks-modal-content">
          <TaskForm @task-created="addTask" />

          <div v-if="tasks.length === 0" class="tasks-empty">
            <div class="tasks-empty-icon">✓</div>

            <h3>Todo está bajo control</h3>

            <p>No tienes tareas todavía.</p>
          </div>

          <ul v-else class="task-list">
            <TaskItem
              v-for="task in tasks"
              :key="task.id"
              :task="task"
              @task-updated="updateTask"
              @task-deleted="removeTask"
            />
          </ul>
        </div>

        <footer class="tasks-modal-footer">
          <span>
            {{ pendingTasks }}
            {{ pendingTasks === 1 ? 'tarea pendiente' : 'tareas pendientes' }}
          </span>

          <button class="modal-done-button" @click="closeTasksModal">Listo</button>
        </footer>
      </div>
    </div>
  </Teleport>
  <CreatePositionDialog v-model:visible="showPositionDialog" @create="addPosition" />
</template>

<style scoped>
.dashboard {
  min-height: 100vh;
  display: flex;
  background: #f7f3ed;
}

/* MAIN */

.main-content {
  flex: 1;
  min-width: 0;
}

/* TOPBAR */

.topbar {
  height: 72px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 40px;
  background: #fffdfb;
  border-bottom: 1px solid #e7e0d7;
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #918b83;
  font-size: 12px;
}

.breadcrumb strong {
  color: #29231e;
  font-weight: 500;
}

.breadcrumb-separator {
  color: #e6e3dd;
}

.user-area {
  display: flex;
  align-items: center;
  gap: 20px;
}

.notification-button {
  position: relative;
  width: 36px;
  height: 36px;
  border: 0;
  border-radius: 50%;
  background: transparent;
  color: #6b6560;
  cursor: pointer;
}

.notification-button:hover {
  background: #f4f2ee;
}

.notification-dot {
  position: absolute;
  top: 7px;
  right: 7px;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #d97757;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}

.avatar {
  width: 34px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: #f4e5de;
  color: #d97757;
  font-size: 11px;
  font-weight: 700;
}

.user-info {
  display: flex;
  flex-direction: column;
}

.user-name {
  color: #29231e;
  font-size: 12px;
  font-weight: 600;
}

.user-role {
  margin-top: 1px;
  color: #918b83;
  font-size: 10px;
}

.dropdown-arrow {
  color: #918b83;
  font-size: 14px;
}

/* PAGE */

.page-content {
  max-width: 1280px;
  margin: 0 auto;
  padding: 42px 40px 60px;
}

.page-intro {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 34px;
}

.eyebrow {
  margin-bottom: 8px;
  color: #d97757;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
}

h1 {
  color: #29231e;
  font-family: Georgia, serif;
  font-size: 34px;
  letter-spacing: -0.02em;
}

.intro-description {
  margin-top: 8px;
  color: #6b6560;
  font-size: 13px;
}

/* BUTTON */

.primary-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  height: 42px;
  padding: 0 18px;
  border: 0;
  border-radius: 8px;
  background: #d97757;
  color: white;
  font-family: inherit;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 1px 3px rgba(42, 37, 32, 0.08);
  transition:
    background 150ms ease,
    transform 150ms ease,
    box-shadow 150ms ease;
}

.primary-button:hover {
  background: #c96643;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(42, 37, 32, 0.12);
}

.plus-icon {
  font-size: 18px;
  font-weight: 400;
  line-height: 1;
}

/* METRICS */

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 44px;
}

.metric-card {
  padding: 20px;
  background: #fffdfb;
  border: 1px solid #e7e0d7;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(42, 37, 32, 0.06);
}

.metric-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.metric-label {
  color: #6b6560;
  font-size: 11px;
  font-weight: 600;
}

.metric-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  font-size: 13px;
}

.metric-icon.orange {
  background: #f4e5de;
  color: #d97757;
}

.metric-icon.beige {
  background: #f4f2ee;
  color: #6b6560;
}

.metric-icon.green {
  background: #edf4ee;
  color: #6b9f78;
}

.metric-value {
  margin-top: 14px;
  color: #29231e;
  font-family: Georgia, serif;
  font-size: 32px;
  font-weight: 600;
  line-height: 1;
}

.metric-description {
  margin-top: 7px;
  color: #918b83;
  font-size: 10px;
}

/* POSITIONS */

.positions-section {
  margin-top: 4px;
}

.section-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 18px;
}

.section-header h2 {
  color: #29231e;
  font-family: Georgia, serif;
  font-size: 23px;
}

.section-header p {
  margin-top: 5px;
  color: #918b83;
  font-size: 11px;
}

.text-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 0;
  background: transparent;
  color: #d97757;
  font-family: inherit;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
}

.text-button:hover {
  color: #c96643;
}

/* POSITION CARD */

.positions-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.position-card {
  padding: 20px 22px;
  background: #fffdfb;
  border: 1px solid #e7e0d7;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(42, 37, 32, 0.06);
  transition:
    border-color 150ms ease,
    box-shadow 150ms ease,
    transform 150ms ease;
}

.position-card:hover {
  border-color: #dcd4ca;
  box-shadow: 0 4px 12px rgba(42, 37, 32, 0.08);
  transform: translateY(-1px);
}

.position-main {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 18px;
}

.position-title-row {
  display: flex;
  align-items: center;
  gap: 13px;
}

.position-icon {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  border-radius: 10px;
  background: #f4f2ee;
  color: #6b6560;
  font-family: Georgia, serif;
  font-size: 18px;
  font-weight: 600;
}

.position-card:first-child .position-icon {
  background: #f4e5de;
  color: #d97757;
}

.position-title-row h3 {
  color: #29231e;
  font-family: Georgia, serif;
  font-size: 16px;
  font-weight: 600;
}

.department {
  display: block;
  margin-top: 4px;
  color: #918b83;
  font-size: 10px;
}

.position-stats {
  display: flex;
  align-items: center;
  gap: 20px;
}

.position-stat {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.stat-number {
  color: #29231e;
  font-family: Georgia, serif;
  font-size: 19px;
  font-weight: 600;
}

.stat-label {
  margin-top: 2px;
  color: #918b83;
  font-size: 9px;
}

/* =========================================
   MY TASKS BUTTON
========================================= */

.intro-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.secondary-button,
.primary-button {
  border: none;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.2s ease;
}

.secondary-button {
  padding: 11px 17px;
  background: #fffdfb;
  border: 1px solid #e7e0d7;
  border-radius: 10px;
  color: #6b6560;
  font-size: 13px;
  font-weight: 600;
}

.secondary-button:hover {
  background: #f7f3ed;
  border-color: #d8cfc5;
  color: #29231e;
}

/* =========================================
   MODAL OVERLAY
========================================= */

.modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(42, 37, 32, 0.38);
  backdrop-filter: blur(8px);
}

/* =========================================
   MODAL
========================================= */

.tasks-modal {
  width: 100%;
  max-width: 680px;
  max-height: 85vh;
  display: flex;
  flex-direction: column;
  background: #fffdfb;
  border: 1px solid #e7e0d7;
  border-radius: 20px;
  box-shadow: 0 25px 80px rgba(42, 37, 32, 0.2);
  overflow: hidden;
}

/* =========================================
   MODAL HEADER
========================================= */

.tasks-modal-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 20px;
  padding: 28px 30px 24px;
}

.modal-eyebrow {
  display: block;
  margin-bottom: 6px;
  color: #d97757;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.5px;
}

.tasks-modal-header h2 {
  margin: 0 0 5px;
  color: #29231e;
  font-size: 25px;
  font-weight: 600;
  letter-spacing: -0.5px;
}

.tasks-modal-header p {
  margin: 0;
  color: #918b83;
  font-size: 13px;
}

.modal-close {
  width: 34px;
  height: 34px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  border-radius: 9px;
  background: #f7f3ed;
  color: #6b6560;
  font-size: 22px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.modal-close:hover {
  background: #f4e5de;
  color: #d97757;
}

/* =========================================
   DIVIDER
========================================= */

.tasks-modal-divider {
  width: 100%;
  height: 1px;
  background: #eee9e3;
}

/* =========================================
   MODAL CONTENT
========================================= */

.tasks-modal-content {
  flex: 1;
  overflow-y: auto;
  padding: 24px 30px 10px;
}

/* =========================================
   TASK LIST
========================================= */

.task-list {
  padding: 0;
  margin: 22px 0 0;
  list-style: none;
}

/* =========================================
   EMPTY STATE
========================================= */

.tasks-empty {
  padding: 45px 20px;
  text-align: center;
}

.tasks-empty-icon {
  width: 52px;
  height: 52px;
  margin: 0 auto 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: #f4e5de;
  color: #d97757;
  font-size: 21px;
  font-weight: 700;
}

.tasks-empty h3 {
  margin: 0 0 6px;
  color: #29231e;
  font-size: 16px;
  font-weight: 600;
}

.tasks-empty p {
  margin: 0;
  color: #918b83;
  font-size: 13px;
}

/* =========================================
   MODAL FOOTER
========================================= */

.tasks-modal-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 15px;
  padding: 18px 30px;
  border-top: 1px solid #eee9e3;
  background: #faf8f5;
  color: #918b83;
  font-size: 12px;
}

.modal-done-button {
  padding: 9px 17px;
  border: none;
  border-radius: 9px;
  background: #d97757;
  color: white;
  font-family: inherit;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s ease;
}

.modal-done-button:hover {
  background: #c96643;
}

/* =========================================
   RESPONSIVE
========================================= */

@media (max-width: 680px) {
  .intro-actions {
    width: 100%;
  }

  .secondary-button,
  .primary-button {
    flex: 1;
  }

  .modal-overlay {
    padding: 12px;
  }

  .tasks-modal {
    max-height: 92vh;
    border-radius: 16px;
  }

  .tasks-modal-header {
    padding: 22px 20px 18px;
  }

  .tasks-modal-content {
    padding: 20px 20px 10px;
  }

  .tasks-modal-footer {
    padding: 15px 20px;
  }
}

.stat-divider {
  width: 1px;
  height: 30px;
  background: #e7e0d7;
}

.position-footer {
  display: flex;
  align-items: center;
  padding-top: 14px;
  border-top: 1px solid #f0ede7;
}

.position-status {
  display: flex;
  align-items: center;
  gap: 7px;
  color: #6b6560;
  font-size: 10px;
  font-weight: 500;
}

.status-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}

.status-dot.active {
  background: #6b9f78;
}

.status-dot.paused {
  background: #e5a85b;
}

.status-dot.closed {
  background: #918b83;
}

.updated {
  margin-left: 18px;
  color: #918b83;
  font-size: 9px;
}

.view-button {
  margin-left: auto;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  border: 0;
  background: transparent;
  color: #d97757;
  font-family: inherit;
  font-size: 10px;
  font-weight: 600;
  cursor: pointer;
}

.view-button:hover {
  color: #c96643;
}

/* RESPONSIVE */

@media (max-width: 900px) {
  .topbar {
    padding: 0 24px;
  }

  .page-content {
    padding: 32px 24px 50px;
  }

  .metrics-grid {
    grid-template-columns: 1fr;
  }

  .page-intro {
    align-items: flex-start;
    flex-direction: column;
    gap: 20px;
  }
}

@media (max-width: 680px) {
  .topbar {
    padding: 0 18px;
  }

  .breadcrumb {
    display: none;
  }

  .page-content {
    padding: 28px 18px 40px;
  }

  h1 {
    font-size: 28px;
  }

  .user-info,
  .dropdown-arrow {
    display: none;
  }

  .position-main {
    align-items: flex-start;
    flex-direction: column;
    gap: 18px;
  }

  .position-stats {
    align-self: flex-start;
  }
}
</style>
