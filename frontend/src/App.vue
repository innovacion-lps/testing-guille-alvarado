<script setup>
import { onMounted, ref } from 'vue'
import api from './services/api'
import TaskForm from './components/TaskForm.vue'
import TaskItem from './components/TaskItem.vue'

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

onMounted(() => {
  getTasks()
})
</script>

<template>
  <main class="app">
    <section class="container">
      <header class="header">
        <h1>Mi Lista de Tareas</h1>
        <p>Organiza tus tareas de forma sencilla.</p>
      </header>

      <TaskForm @task-created="addTask" />

      <ul class="task-list">
        <TaskItem
          v-for="task in tasks"
          :key="task.id"
          :task="task"
          @task-updated="updateTask"
          @task-deleted="removeTask"
        />
      </ul>
    </section>
  </main>
</template>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f4f4f5;
}

.app {
  min-height: 100vh;
  padding: 40px 20px;
}

.container {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
}

.header {
  margin-bottom: 25px;
}

.header h1 {
  margin-bottom: 8px;
}

.header p {
  margin: 0;
  color: #666;
}

.task-list {
  padding: 0;
  margin-top: 25px;
  list-style: none;
}
</style>