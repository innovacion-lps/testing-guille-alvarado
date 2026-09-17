<script setup>
import { computed, onMounted, ref } from 'vue'
import api from './services/api'
import TaskForm from './components/TaskForm.vue'
import TaskItem from './components/TaskItem.vue'
import login from './components/login.vue'

const isAuthenticated = ref(false)

const tasks = ref([])

async function getTasks() {
  const response = await api.get('/tasks')
  tasks.value = response.data
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

onMounted(() => {
  getTasks()
})
</script>
<template>
  <login
    v-if="!isAuthenticated"
    @login-success="isAuthenticated = true"
  />

  <main v-else class="app">
    <section class="container">

      <div class="main-card">

        <header class="header">

          <div class="title-section">

            <div class="icon-wrapper">
              ✓
            </div>

            <div class="title-content">
              <h1>Mi Lista de Tareas</h1>

              <p>
                Organiza tus tareas y mantén el control de tu día.
              </p>
            </div>

          </div>

          <div class="task-counter">

            <span class="counter-number">
              {{ pendingTasks }}
            </span>

            <span class="counter-label">
              pendientes
            </span>

          </div>

        </header>

        <div class="divider"></div>

        <TaskForm @task-created="addTask" />

        <div
          v-if="tasks.length === 0"
          class="empty-state"
        >

          <div class="empty-icon">
            ✓
          </div>

          <h2>
            Todo está bajo control
          </h2>

          <p>
            No tienes tareas todavía. Agrega una para comenzar.
          </p>

        </div>

        <ul
          v-else
          class="task-list"
        >

          <TaskItem
            v-for="task in tasks"
            :key="task.id"
            :task="task"
            @task-updated="updateTask"
            @task-deleted="removeTask"
          />

        </ul>

        <footer class="footer">

          <span>
            Mi Lista de Tareas
          </span>

          <span class="footer-dot">
            •
          </span>

          <span>
            {{ tasks.length }}
            {{ tasks.length === 1 ? 'tarea' : 'tareas' }}
          </span>

        </footer>

      </div>

    </section>
  </main>
</template>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;

  font-family:
    Inter,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    Arial,
    sans-serif;

  background:
    radial-gradient(
      circle at 10% 10%,
      rgba(139, 0, 0, 0.35),
      transparent 30%
    ),
    radial-gradient(
      circle at 90% 90%,
      rgba(124, 58, 237, 0.28),
      transparent 32%
    ),
    radial-gradient(
      circle at 50% 100%,
      rgba(255, 69, 0, 0.22),
      transparent 38%
    ),
    linear-gradient(
      135deg,
      #080303 0%,
      #120506 45%,
      #09050f 100%
    );

  color: #f5eeee;
}

.app {
  min-height: 100vh;

  display: flex;
  align-items: flex-start;
  justify-content: center;

  padding: 60px 20px;
}

.container {
  width: 100%;
  max-width: 720px;
}

.main-card {
  width: 100%;

  padding: 32px;

  position: relative;

  background:
    linear-gradient(
      145deg,
      rgba(28, 8, 10, 0.90),
      rgba(12, 7, 18, 0.90)
    );

  border: 1px solid rgba(255, 69, 0, 0.20);

  border-radius: 24px;

  box-shadow:
    0 30px 90px rgba(0, 0, 0, 0.65),
    0 0 45px rgba(255, 42, 0, 0.08),
    0 0 80px rgba(124, 58, 237, 0.08);

  backdrop-filter: blur(24px);

  overflow: hidden;
}

.header {
  display: flex;

  align-items: center;
  justify-content: space-between;

  gap: 20px;
}

.title-section {
  display: flex;

  align-items: center;

  gap: 15px;

  min-width: 0;
}

.icon-wrapper {
  width: 50px;
  height: 50px;

  flex-shrink: 0;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 15px;

  background:
    linear-gradient(
      135deg,
      #6366f1,
      #8b5cf6
    );

  color: white;

  font-size: 23px;
  font-weight: 700;
  text-shadow:
    0 0 25px rgba(255, 69, 0, 0.12);
  box-shadow:
    0 8px 20px rgba(99, 102, 241, 0.25);
}

.title-content {
  min-width: 0;
}

.header h1 {
  margin: 0 0 5px;

  color: #fff7f5;
  
  font-size: 25px;
  font-weight: 700;

  letter-spacing: -0.6px;
}

.header p {
  margin: 0;

  color: #a8a0a3;

  font-size: 14px;

  line-height: 1.5;
}

.task-counter {
  min-width: 78px;

  padding: 9px 12px;

  display: flex;
  flex-direction: column;
  align-items: center;

  background: #f8fafc;

  border: 1px solid #e2e8f0;

  border-radius: 14px;
}

.counter-number {
  color: #4f46e5;

  font-size: 21px;
  font-weight: 700;

  line-height: 1.2;
}

.counter-label {
  margin-top: 2px;

  color: #64748b;

  font-size: 11px;
}

.divider {
  width: 100%;
  height: 1px;

  margin: 28px 0;

  background: #e2e8f0;
}

.task-list {
  padding: 0;

  margin: 25px 0 0;

  list-style: none;
}

.empty-state {
  padding: 45px 20px 30px;

  text-align: center;
}

.empty-icon {
  width: 58px;
  height: 58px;

  margin: 0 auto 18px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 50%;

  background: #eef2ff;

  border: 1px solid #e0e7ff;

  color: #6366f1;

  font-size: 24px;
  font-weight: 700;
}

.empty-state h2 {
  margin: 0 0 8px;

  color: #334155;

  font-size: 18px;
  font-weight: 600;
}

.empty-state p {
  margin: 0;

  color: #94a3b8;

  font-size: 14px;
}

.footer {
  display: flex;

  align-items: center;
  justify-content: center;

  gap: 8px;

  margin-top: 28px;
  padding-top: 20px;

  border-top: 1px solid #f1f5f9;

  color: #94a3b8;

  font-size: 12px;
}

.footer-dot {
  color: #cbd5e1;
}

@media (max-width: 600px) {
  .app {
    padding: 25px 14px;
  }

  .main-card {
    padding: 22px;

    border-radius: 20px;
  }

  .header {
    align-items: flex-start;
  }

  .title-section {
    gap: 11px;
  }

  .icon-wrapper {
    width: 44px;
    height: 44px;

    border-radius: 13px;

    font-size: 20px;
  }

  .header h1 {
    font-size: 21px;
  }

  .header p {
    font-size: 12px;
  }

  .task-counter {
    min-width: 62px;

    padding: 8px 9px;
  }

  .counter-number {
    font-size: 18px;
  }

  .counter-label {
    font-size: 10px;
  }
}
</style>