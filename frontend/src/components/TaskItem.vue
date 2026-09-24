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
      <label class="checkbox-wrapper">
        <input type="checkbox" :checked="task.completed" @change="updateTask" />

        <span class="custom-checkbox">
          <span class="checkmark">✓</span>
        </span>
      </label>

      <div class="task-info">
        <span class="task-title">
          {{ task.title }}
        </span>

        <span class="task-status">
          {{ task.completed ? 'Completada' : 'Pendiente' }}
        </span>
      </div>
    </div>

    <button class="delete-button" title="Eliminar tarea" @click="deleteTask">
      <span>×</span>
    </button>
  </li>
</template>

<style scoped>
/* =========================================================
   TASK ITEM
   Estética: Infernal / Futurista / Premium
   ========================================================= */

li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 15px;
  min-height: 68px;
  padding: 12px 14px;
  margin-bottom: 10px;
  background: linear-gradient(145deg, rgba(30, 9, 12, 0.88), rgba(16, 9, 23, 0.88));
  border: 1px solid rgba(255, 69, 0, 0.14);
  border-radius: 14px;
  box-shadow:
    0 5px 18px rgba(0, 0, 0, 0.28),
    0 0 20px rgba(255, 61, 0, 0.025);
  backdrop-filter: blur(12px);
  transition:
    transform 0.25s ease,
    box-shadow 0.25s ease,
    border-color 0.25s ease,
    background 0.25s ease;
  position: relative;
  overflow: hidden;
}

/* Línea luminosa muy sutil en la parte superior */

li::before {
  content: '';
  position: absolute;
  top: 0;
  left: 8%;
  right: 8%;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 69, 0, 0.35),
    rgba(124, 58, 237, 0.35),
    transparent
  );
  opacity: 0.6;
  pointer-events: none;
}

/* Glow interior */

li::after {
  content: '';
  position: absolute;
  width: 120px;
  height: 120px;
  right: -70px;
  top: -60px;
  border-radius: 50%;
  background: rgba(124, 58, 237, 0.07);
  filter: blur(35px);
  pointer-events: none;
  transition:
    opacity 0.25s ease,
    transform 0.25s ease;
}

/* =========================================================
   HOVER
   ========================================================= */

li:hover {
  transform: translateY(-2px);
  border-color: rgba(255, 69, 0, 0.32);
  background: linear-gradient(145deg, rgba(40, 10, 12, 0.92), rgba(20, 10, 30, 0.92));
  box-shadow:
    0 9px 25px rgba(0, 0, 0, 0.4),
    0 0 22px rgba(255, 61, 0, 0.08),
    0 0 28px rgba(124, 58, 237, 0.06);
}

li:hover::after {
  opacity: 1;
  transform: scale(1.2);
}

/* =========================================================
   CONTENIDO
   ========================================================= */

.task-content {
  display: flex;
  align-items: center;
  gap: 13px;
  min-width: 0;
  position: relative;
  z-index: 1;
}

/* =========================================================
   CHECKBOX
   ========================================================= */

.checkbox-wrapper {
  position: relative;
  width: 22px;
  height: 22px;
  flex-shrink: 0;
  cursor: pointer;
}

.checkbox-wrapper input {
  position: absolute;
  width: 0;
  height: 0;
  opacity: 0;
}

.custom-checkbox {
  width: 22px;
  height: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid rgba(255, 255, 255, 0.18);
  border-radius: 7px;
  background: rgba(8, 5, 10, 0.75);
  transition:
    background 0.25s ease,
    border-color 0.25s ease,
    box-shadow 0.25s ease,
    transform 0.2s ease;
}

/* =========================================================
   CHECKMARK
   ========================================================= */

.checkmark {
  opacity: 0;
  color: white;
  font-size: 13px;
  font-weight: 700;
  transform: scale(0.5);
  transition:
    opacity 0.2s ease,
    transform 0.2s ease;
}

/* Checkbox completado */

.checkbox-wrapper input:checked + .custom-checkbox {
  background: linear-gradient(135deg, #ff3d00, #dc2626 55%, #7c3aed);
  border-color: rgba(255, 69, 0, 0.75);
  box-shadow:
    0 0 12px rgba(255, 61, 0, 0.25),
    0 0 18px rgba(124, 58, 237, 0.15);
}

.checkbox-wrapper input:checked + .custom-checkbox .checkmark {
  opacity: 1;
  transform: scale(1);
}

/* =========================================================
   INFORMACIÓN DE LA TAREA
   ========================================================= */

.task-info {
  display: flex;
  flex-direction: column;
  gap: 3px;
  min-width: 0;
}

.task-title {
  overflow: hidden;
  color: #f2e9eb;
  font-size: 15px;
  font-weight: 500;
  white-space: nowrap;
  text-overflow: ellipsis;
  transition:
    color 0.25s ease,
    opacity 0.25s ease;
}

.task-status {
  font-size: 11px;
  color: #81777d;
  transition: color 0.25s ease;
}

/* =========================================================
   BOTÓN ELIMINAR
   ========================================================= */

.delete-button {
  width: 34px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  border: 1px solid transparent;
  border-radius: 9px;
  background: transparent;
  color: #756b70;
  font-size: 22px;
  font-weight: 300;
  cursor: pointer;
  position: relative;
  z-index: 2;
  transition:
    background 0.25s ease,
    color 0.25s ease,
    border-color 0.25s ease,
    box-shadow 0.25s ease,
    transform 0.2s ease;
}

/* Hover eliminar */

.delete-button:hover {
  background: rgba(127, 29, 29, 0.22);
  border-color: rgba(239, 68, 68, 0.22);
  color: #ff5c4d;
  transform: scale(1.05);
  box-shadow: 0 0 15px rgba(239, 68, 68, 0.1);
}

/* =========================================================
   TAREA COMPLETADA
   ========================================================= */

.completed {
  background: linear-gradient(145deg, rgba(20, 9, 11, 0.72), rgba(15, 10, 21, 0.72));
  border-color: rgba(124, 58, 237, 0.12);
  opacity: 0.8;
}

.completed .task-title {
  color: #777077;
  text-decoration: line-through;
}

.completed .task-status {
  color: #9b7edb;
}

/* =========================================================
   HOVER SOBRE TAREA COMPLETADA
   ========================================================= */

.completed:hover {
  border-color: rgba(124, 58, 237, 0.25);
  box-shadow:
    0 8px 22px rgba(0, 0, 0, 0.35),
    0 0 20px rgba(124, 58, 237, 0.06);
}

/* =========================================================
   RESPONSIVE
   ========================================================= */

@media (max-width: 500px) {
  li {
    padding: 11px;
  }

  .task-title {
    max-width: 190px;
  }

  .task-status {
    font-size: 10px;
  }
}
</style>
