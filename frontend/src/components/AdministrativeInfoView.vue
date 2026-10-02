<script setup>
import { ref } from 'vue'
import SidebarMain from './SidebarMain.vue'
import CustomSelect from './CustomSelect.vue'
import { NotebookPen, FilePen } from 'lucide-vue-next'

const fechaLlegada = ref('2026-09-15')
const fechaReclutamiento = ref('2026-09-16')
const categoria = ref('Tecnología')
const CATEGORIAS = ['Tecnología', 'Ventas', 'Marketing', 'Operaciones']
const gerencia = ref('Ingeniería')
const GERENCIAS = ['Ingeniería', 'Finanzas', 'RRHH']
const area = ref('Desarrollo')
const AREAS = ['Desarrollo', 'QA', 'Infraestructura']
const jefeInmediato = ref('Juan Pérez')
const JEFES = ['Juan Pérez', 'Ana Torres', 'Carlos López']
const motivo = ref('Nueva posición')
const MOTIVOS = ['Nueva posición', 'Reemplazo', 'Expansión']
const esReemplazo = ref(true)
const personaReemplazar = ref('María García')
const PERSONAS = ['María García', 'Pedro Torres']
const fechaCese = ref('2026-09-30')
</script>

<template>
  <section class="admin-card">
    <div class="card-header">
      <div class="section-title">
        <NotebookPen :size="30" color="#f97316" />
        <h2>Información Administrativa</h2>
      </div>

      <button class="edit-button">
        <FilePen :size="18" color="#f97316" />
        Editar
      </button>
    </div>

    <div class="grid">
      <div class="field">
        <label>Fecha de llegada del requerimiento</label>
        <input v-model="fechaLlegada" type="date" />
      </div>

      <div class="field">
        <label>Fecha de reclutamiento</label>
        <input v-model="fechaReclutamiento" type="date" />
      </div>

      <div class="field">
        <label>Categoría</label>

        <CustomSelect v-model="categoria" :options="CATEGORIAS" />
      </div>

      <div class="field">
        <label>Gerencia</label>

        <CustomSelect v-model="gerencia" :options="GERENCIAS" />
      </div>

      <div class="field">
        <label>Área</label>

        <CustomSelect v-model="area" :options="AREAS" />
      </div>

      <div class="field">
        <label>Jefe inmediato</label>

        <CustomSelect v-model="jefeInmediato" :options="JEFES" />
      </div>

      <div class="field">
        <label>Motivo del requerimiento</label>

        <CustomSelect v-model="motivo" :options="MOTIVOS" />
      </div>
    </div>

    <div class="bottom-grid">
      <div class="replacement-card">
        <label>¿Es reemplazo?</label>

        <div class="switch-row">
          <label class="switch">
            <input v-model="esReemplazo" type="checkbox" />

            <span class="slider"></span>
          </label>

          <span class="switch-label">{{ esReemplazo ? 'Sí' : 'No' }}</span>
        </div>
      </div>

      <div class="field">
        <label>Persona a reemplazar</label>

        <CustomSelect v-model="personaReemplazar" :options="PERSONAS" :disabled="!esReemplazo" />
      </div>

      <div class="field">
        <label>Fecha de cese</label>

        <input v-model="fechaCese" type="date" :disabled="!esReemplazo" />
      </div>
    </div>
  </section>
</template>

<style scoped>
.admin-card {
  background: white;
  border-radius: 18px;
  padding: 32px;
  margin-top: 30px;
  border: 1px solid #e6e3dd;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  margin-bottom: 30px;
}

h2 {
  margin: 0;
  font-family: var(--font-display);
  color: var(--color-text-primary);
}

.edit-button {
  background: white;
  border: 1px solid #e6e3dd;
  padding: 10px 18px;
  border-radius: 10px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  line-height: 1;
}

.edit-button svg {
  flex-shrink: 0;
  display: block;
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 8px;
}

.section-title h2 {
  margin: 0;
}

.grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 20px;
  align-items: start;
}

.bottom-grid {
  margin-top: 25px;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
  align-items: stretch;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-width: 0;
}

.field label,
.replacement-card > label {
  font-size: 14px;
  color: #4f4a45;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

input {
  width: 100%;
  height: 50px;
  box-sizing: border-box;
  border: 1px solid #e6e3dd;
  border-radius: 12px;
  padding: 0 15px;
  background-color: white;
  color: #4f4a45;
  font-size: 14px;
  font-family: inherit;
  min-width: 0;
}

input:focus {
  outline: none;
  border-color: #d97757;
  box-shadow: 0 0 0 3px rgba(217, 119, 87, 0.08);
}

/* Los desplegables ahora son CustomSelect (apertura/cierre controlados por Vue,
   ya no dependen del popup nativo del navegador) */

/* ¿Es reemplazo? en una sola fila: label a la izquierda, switch a la derecha */
.replacement-card {
  border: 1px solid #ece7df;
  border-radius: 16px;
  padding: 0 20px;
  background: #faf9f7;
  min-height: 50px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.switch-row {
  margin-top: 0;
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

.switch-label {
  min-width: 24px;
  font-size: 14px;
  color: #4f4a45;
}

.switch {
  position: relative;
  width: 50px;
  height: 28px;
  display: inline-block;
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
  background: #d8d4ce;
  border-radius: 30px;
  cursor: pointer;
  transition: 0.3s;
}

.slider::before {
  content: '';

  position: absolute;

  width: 22px;
  height: 22px;

  left: 3px;
  top: 3px;

  background: white;

  border-radius: 50%;

  transition: 0.3s;
}

.switch input:checked + .slider {
  background: #d97757;
}

.switch input:checked + .slider::before {
  transform: translateX(22px);
}

input:disabled {
  background-color: #f4f2ee;
  color: #aaa;
  cursor: not-allowed;
}

/* Responsive */
@media (max-width: 1100px) {
  .grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .bottom-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 800px) {
  .grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .bottom-grid {
    grid-template-columns: 1fr;
  }

  .admin-card {
    padding: 20px;
  }
}

@media (max-width: 520px) {
  .grid {
    grid-template-columns: 1fr;
  }

  .card-header {
    flex-direction: column;
    align-items: stretch;
  }

  .replacement-card {
    min-height: 64px;
  }
}
</style>
