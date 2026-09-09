<script setup>
import { ref } from 'vue'
import api from '../services/api'

const newTaskTitle = ref('')

const emit = defineEmits(['task-created'])

async function createTask() {
  if (!newTaskTitle.value.trim()) {
    return
  }

  const response = await api.post('/tasks', {
    title: newTaskTitle.value
  })

  emit('task-created', response.data)

  newTaskTitle.value = ''
}
</script>

<template>
  <div class="form">
    <input
      v-model="newTaskTitle"
      type="text"
      placeholder="¿Qué necesitas hacer?"
      @keyup.enter="createTask"
    />

    <button @click="createTask">
      Agregar
    </button>
  </div>
</template>

<style scoped>
.form {
  display: flex;
  gap: 10px;
}

input {
  flex: 1;
  padding: 12px;
  border: 1px solid #d4d4d8;
  border-radius: 8px;
  font-size: 16px;
}

button {
  padding: 12px 18px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 15px;
}
</style>