```vue
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
    <div class="input-wrapper">
      <span class="input-icon">+</span>

      <input
        v-model="newTaskTitle"
        type="text"
        placeholder="¿Qué necesitas hacer?"
        @keyup.enter="createTask"
      />
    </div>

    <button @click="createTask">
      <span>Agregar tarea</span>
      <span class="button-icon">→</span>
    </button>
  </div>
</template>

```css
<style scoped>

/* =========================================================
   TASK FORM
   Estética: Infernal / Futurista / Premium
   ========================================================= */

.form {
  display: flex;

  gap: 10px;

  width: 100%;

  position: relative;
}


/* =========================================================
   INPUT WRAPPER
   ========================================================= */

.input-wrapper {
  position: relative;

  flex: 1;

  min-width: 0;
}


/* =========================================================
   ICONO +
   ========================================================= */

.input-icon {
  position: absolute;

  left: 15px;
  top: 50%;

  transform: translateY(-50%);

  color: #ff5a36;

  font-size: 20px;

  font-weight: 500;

  pointer-events: none;

  text-shadow:
    0 0 12px rgba(255, 69, 0, 0.35);

  transition:
    color 0.25s ease,
    text-shadow 0.25s ease;
}


/* =========================================================
   INPUT
   ========================================================= */

input {
  width: 100%;

  height: 48px;

  box-sizing: border-box;

  padding: 0 16px 0 42px;

  border: 1px solid rgba(255, 255, 255, 0.09);

  border-radius: 12px;

  background:
    linear-gradient(
      145deg,
      rgba(27, 8, 11, 0.9),
      rgba(16, 9, 23, 0.9)
    );

  color: #f7eeee;

  font-size: 14px;

  outline: none;

  backdrop-filter: blur(10px);

  transition:
    border-color 0.25s ease,
    box-shadow 0.25s ease,
    background 0.25s ease;
}


/* Placeholder */

input::placeholder {
  color: #71676d;
}


/* =========================================================
   INPUT FOCUS
   ========================================================= */

input:focus {
  background:
    linear-gradient(
      145deg,
      rgba(35, 9, 11, 0.95),
      rgba(21, 10, 31, 0.95)
    );

  border-color:
    rgba(255, 69, 0, 0.55);

  box-shadow:
    0 0 0 3px rgba(255, 69, 0, 0.07),
    0 0 20px rgba(255, 69, 0, 0.10),
    0 0 28px rgba(124, 58, 237, 0.08);
}


input:focus + .input-icon {
  color: #ff704d;

  text-shadow:
    0 0 15px rgba(255, 69, 0, 0.5);
}


/* =========================================================
   BOTÓN AGREGAR
   ========================================================= */

button {
  height: 48px;

  display: flex;

  align-items: center;

  gap: 10px;

  padding: 0 18px;

  border: 1px solid rgba(255, 255, 255, 0.06);

  border-radius: 12px;

  background:
    linear-gradient(
      135deg,
      #ff3d00 0%,
      #dc2626 48%,
      #7c3aed 100%
    );

  color: white;

  font-size: 14px;

  font-weight: 600;

  cursor: pointer;

  box-shadow:
    0 7px 20px rgba(255, 61, 0, 0.16),
    0 0 25px rgba(124, 58, 237, 0.10);

  transition:
    transform 0.2s ease,
    box-shadow 0.25s ease,
    filter 0.25s ease;
}


/* =========================================================
   HOVER BOTÓN
   ========================================================= */

button:hover {
  transform: translateY(-2px);

  filter: brightness(1.08);

  box-shadow:
    0 10px 26px rgba(255, 61, 0, 0.24),
    0 0 30px rgba(124, 58, 237, 0.18);
}


/* =========================================================
   ACTIVE
   ========================================================= */

button:active {
  transform: translateY(0);
}


/* =========================================================
   ICONO →
   ========================================================= */

.button-icon {
  font-size: 18px;

  transition:
    transform 0.2s ease;
}


button:hover .button-icon {
  transform: translateX(3px);
}


/* =========================================================
   RESPONSIVE
   ========================================================= */

@media (max-width: 520px) {

  .form {
    flex-direction: column;
  }

  button {
    justify-content: center;
  }

}

</style>

