<script setup>
import api from '../services/api'

const props = defineProps({
  task: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['task-updated', 'task-deleted'])

async function updateTask() {
  const response = await api.put(`/tasks/${props.task.id}`, {
    title: props.task.title,
    completed: !props.task.completed
  })

  emit('task-updated', response.data)
}

async function deleteTask() {
  await api.delete(`/tasks/${props.task.id}`)

  emit('task-deleted', props.task.id)
}
</script>

<template>
  <li :class="{ completed: task.completed }">
    <div class="task-content">
      <input
        type="checkbox"
        :checked="task.completed"
        @change="updateTask"
      />

      <span>{{ task.title }}</span>
    </div>

    <button @click="deleteTask">
      Eliminar
    </button>
  </li>
</template>

<style scoped>
li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 15px;
  padding: 15px;
  margin-bottom: 10px;
  background: white;
  border-radius: 10px;
  border: 1px solid #e4e4e7;
}

.task-content {
  display: flex;
  align-items: center;
  gap: 10px;
}

.task-content span {
  font-size: 16px;
}

.completed .task-content span {
  text-decoration: line-through;
  opacity: 0.5;
}

button {
  border: none;
  background: transparent;
  cursor: pointer;
  font-size: 14px;
}
</style>