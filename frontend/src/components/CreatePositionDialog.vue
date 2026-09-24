<script setup>
import { ref, watch, nextTick, computed } from 'vue'

const props = defineProps({
  visible: { type: Boolean, default: false }
})

const emit = defineEmits(['update:visible', 'create'])

const title = ref('')
const description = ref('')
const requirements = ref([])
const overlayRef = ref(null)
const newFormRef = ref(null)
const loading = ref(false)
const error = ref(null)

const COUNTRIES = [
  { code: 'CO', name: 'Colombia', currency: 'COP', symbol: '$' },
  { code: 'MA', name: 'Marruecos', currency: 'MAD', symbol: 'DH' },
  { code: 'PE', name: 'Perú', currency: 'PEN', symbol: 'S/' },
  { code: 'ES', name: 'España', currency: 'EUR', symbol: '€' },
  { code: 'DE', name: 'Alemania', currency: 'EUR', symbol: '€' }
]

const CURRENCIES = ['COP', 'MAD', 'PEN', 'EUR', 'USD']

const country = ref('')
const currency = ref('')
const salaryMin = ref('')
const salaryMax = ref('')

watch(
  () => props.visible,
  async newVal => {
    if (newVal) {
      resetForm()
      await nextTick()
      overlayRef.value?.focus()
    }
  }
)

const CURRENCY_SYMBOLS = { COP: '$', MAD: 'DH', PEN: 'S/', EUR: '€', USD: '$' }

const currencySymbol = computed(() => CURRENCY_SYMBOLS[currency.value] || '')

function formatSalaryDisplay(value) {
  if (value === '' || value == null) return ''
  const digits = String(value).replace(/[^0-9]/g, '')
  if (!digits) return ''
  return Number(digits).toLocaleString('en-US') // 3500 -> 3,500
}

function parseSalary(value) {
  if (value === '' || value == null) return null
  const digits = String(value).replace(/[^0-9]/g, '')
  return digits ? Number(digits) : null
}

function allowOnlyNumbers(e) {
  const controlKeys = [
    'Backspace',
    'Delete',
    'Tab',
    'Escape',
    'Enter',
    'ArrowLeft',
    'ArrowRight',
    'ArrowUp',
    'ArrowDown',
    'Home',
    'End'
  ]
  if (controlKeys.includes(e.key)) return
  if (e.ctrlKey || e.metaKey) return // deja Ctrl+C, Ctrl+V, Ctrl+A
  if (!/^[0-9]$/.test(e.key)) e.preventDefault()
}

function onSalaryMinInput(e) {
  salaryMin.value = formatSalaryDisplay(e.target.value)
}

function onSalaryMaxInput(e) {
  salaryMax.value = formatSalaryDisplay(e.target.value)
}

const close = () => {
  if (loading.value) return
  emit('update:visible', false)
  resetForm()
}

const resetForm = () => {
  title.value = ''
  description.value = ''
  country.value = ''
  currency.value = ''
  salaryMin.value = ''
  salaryMax.value = ''
  requirements.value = []
  expandedReqIndex.value = null
  showNewReqForm.value = false
  error.value = null
}

const expandedReqIndex = ref(null)
const editReq = ref({ key: '', title: '', description: '', type: 'score' })

const salaryError = computed(() => {
  const min = parseSalary(salaryMin.value)
  const max = parseSalary(salaryMax.value)
  if (min == null || max == null) return ''
  return min > max ? 'El mínimo no puede ser mayor que el máximo' : ''
})

watch(country, newCountry => {
  const found = COUNTRIES.find(c => c.code === newCountry)
  if (found) currency.value = found.currency
})

const toggleExpandRequirement = index => {
  if (expandedReqIndex.value === index) {
    expandedReqIndex.value = null
    return
  }
  const req = requirements.value[index]
  editReq.value = {
    key: req.key,
    title: req.title,
    description: req.description,
    type: req.type
  }
  expandedReqIndex.value = index
}

const saveEditReq = () => {
  if (!editReq.value.title.trim() || expandedReqIndex.value === null) return
  requirements.value[expandedReqIndex.value] = {
    key: editReq.value.key,
    title: editReq.value.title,
    description: editReq.value.description,
    type: editReq.value.type
  }
  expandedReqIndex.value = null
}

const cancelEditReq = () => {
  expandedReqIndex.value = null
}

const addRequirement = () => {
  expandedReqIndex.value = null
  newReq.value = { key: '', title: '', description: '', type: 'score' }
  showNewReqForm.value = true
  nextTick(() => {
    newFormRef.value?.scrollIntoView({ behavior: 'smooth', block: 'center' })
  })
}

const newReq = ref({ key: '', title: '', description: '', type: 'score' })
const showNewReqForm = ref(false)

const saveNewRequirement = () => {
  if (!newReq.value.title.trim()) return
  requirements.value.push({
    key: `req_${Date.now()}`,
    title: newReq.value.title,
    description: newReq.value.description,
    type: newReq.value.type
  })
  newReq.value = { key: '', title: '', description: '', type: 'score' }
  showNewReqForm.value = false
}

const cancelNewRequirement = () => {
  newReq.value = { key: '', title: '', description: '', type: 'score' }
  showNewReqForm.value = false
}

const removeRequirement = index => {
  requirements.value.splice(index, 1)
}

const submit = () => {
  if (!title.value.trim() || loading.value || salaryError.value) return
  emit('create', {
    id: Date.now(),
    title: title.value.trim(),
    description: description.value.trim(),
    country: country.value,
    currency: currency.value,
    salaryMin: parseSalary(salaryMin.value),
    salaryMax: parseSalary(salaryMax.value),
    requirements: [...requirements.value]
  })
  close()
}
</script>

<template>
  <div
    v-if="visible"
    ref="overlayRef"
    class="dialog-overlay"
    :class="{ loading }"
    tabindex="-1"
    @mousedown.self="close"
    @keydown.escape="close"
  >
    <div class="dialog">
      <div class="dialog-header">
        <div class="dialog-header-left">
          <svg class="dialog-icon" width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M22 13.478v4.522a3 3 0 0 1 -3 3h-14a3 3 0 0 1 -3 -3v-4.522l.553 .277a20.999 20.999 0 0 0 18.897 -.002l.55 -.275zm-8 -11.478a3 3 0 0 1 3 3v1h2a3 3 0 0 1 3 3v2.242l-1.447 .724a19.002 19.002 0 0 1 -16.726 .186l-.647 -.32l-1.18 -.59v-2.242a3 3 0 0 1 3 -3h2v-1a3 3 0 0 1 3 -3h4zm-2 8a1 1 0 0 0 -1 1a1 1 0 1 0 2 .01c0 -.562 -.448 -1.01 -1 -1.01zm2 -6h-4a1 1 0 0 0 -1 1v1h6v-1a1 1 0 0 0 -1 -1z"
            />
          </svg>
          <div class="dialog-header-text">
            <h2>Crear posición</h2>
            <p class="dialog-subtitle">Define la vacante y sus requisitos</p>
          </div>
        </div>
        <button class="btn-close" @click="close">×</button>
      </div>

      <div class="dialog-content">
        <div class="form-group">
          <label>Título <span class="required">*</span></label>
          <input
            v-model="title"
            type="text"
            placeholder="Ej. Senior Backend Developer"
            :disabled="loading"
          />
        </div>

        <div class="form-group">
          <label>Descripción</label>
          <textarea v-model="description" rows="3" placeholder="Describe el puesto..." />
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>País</label>
            <select v-model="country" :disabled="loading">
              <option value="">Seleccionar país</option>
              <option v-for="c in COUNTRIES" :key="c.code" :value="c.code">
                {{ c.name }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label>Moneda</label>
            <select v-model="currency" :disabled="loading">
              <option value="">Seleccionar moneda</option>
              <option v-for="cur in CURRENCIES" :key="cur" :value="cur">
                {{ cur }}
              </option>
            </select>
          </div>
        </div>

        <!-- RANGO SALARIAL -->
        <div class="form-row">
          <div class="form-group">
            <label>Salario mínimo</label>
            <div class="salary-wrapper">
              <span v-if="currencySymbol" class="salary-prefix">{{ currencySymbol }}</span>
              <input
                :value="salaryMin"
                type="text"
                inputmode="numeric"
                placeholder="Ej. 3,500"
                maxlength="13"
                :disabled="loading"
                @input="onSalaryMinInput"
                @keydown="allowOnlyNumbers"
              />
            </div>
          </div>
          <div class="form-group">
            <label>Salario máximo</label>
            <div class="salary-wrapper">
              <span v-if="currencySymbol" class="salary-prefix">{{ currencySymbol }}</span>
              <input
                :value="salaryMax"
                type="text"
                inputmode="numeric"
                placeholder="Ej. 5,000"
                maxlength="13"
                :disabled="loading"
                @input="onSalaryMaxInput"
                @keydown="allowOnlyNumbers"
              />
            </div>
          </div>
        </div>
        <p v-if="salaryError" class="error-message">{{ salaryError }}</p>

        <div class="form-group requirements-section">
          <div class="requirements-header">
            <div class="requirements-header-left">
              <label>Requisitos</label>
              <span class="count-badge">{{ requirements.length }}</span>
            </div>
            <button class="btn-add-req" @click="addRequirement" :disabled="showNewReqForm">
              <span v-if="showNewReqForm" class="btn-add-req-editing">Editando...</span>
              <span v-else>+ Agregar</span>
            </button>
          </div>

          <div v-if="requirements.length === 0 && !showNewReqForm" class="no-requirements">
            Sin requisitos. Agrega el primero.
          </div>

          <div class="req-chips">
            <div v-for="(req, index) in requirements" :key="req.key" class="req-chip-group">
              <div class="req-chip" @click="toggleExpandRequirement(index)">
                <button class="req-chip-expand" @click.stop="toggleExpandRequirement(index)">
                  <svg
                    class="toggle-icon"
                    :class="{ rotated: expandedReqIndex === index }"
                    width="14"
                    height="14"
                    viewBox="0 0 16 16"
                    fill="none"
                  >
                    <path
                      d="M4 6L8 10L12 6"
                      stroke="currentColor"
                      stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </svg>
                </button>
                <span class="req-chip-title">{{ req.title || 'Sin título' }}</span>
                <div class="req-chip-second">
                  <span class="req-chip-type">{{
                    req.type === 'score' ? 'Puntaje' : 'Sí/No'
                  }}</span>
                  <span v-if="req.description" class="req-chip-desc-sep">·</span>
                  <span v-if="req.description" class="req-chip-desc">{{ req.description }}</span>
                </div>
                <button
                  class="req-chip-remove"
                  @click.stop="removeRequirement(index)"
                  title="Eliminar requisito"
                >
                  <svg width="20" height="20" viewBox="0 0 16 16" fill="none">
                    <path
                      d="M2.5 4H13.5M5.5 4V3C5.5 2.45 5.95 2 6.5 2H9.5C10.05 2 10.5 2.45 10.5 3V4M12 4V13C12 13.55 11.55 14 11 14H5C4.45 14 4 13.55 4 13V4H12ZM6.5 7V11M9.5 7V11"
                      stroke="currentColor"
                      stroke-width="1.4"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </svg>
                </button>
              </div>
              <div v-if="expandedReqIndex === index" class="req-chip-edit-form">
                <div class="form-group">
                  <label>Título del requisito <span class="required">*</span></label>
                  <input
                    v-model="editReq.title"
                    type="text"
                    placeholder="Ej. Experiencia con Python"
                  />
                </div>
                <div class="form-group">
                  <label>Tipo</label>
                  <div class="type-toggle" role="group">
                    <button
                      type="button"
                      class="type-toggle-btn"
                      :class="{ active: editReq.type === 'score' }"
                      @click="editReq.type = 'score'"
                    >
                      Puntaje
                    </button>
                    <button
                      type="button"
                      class="type-toggle-btn"
                      :class="{ active: editReq.type === 'boolean' }"
                      @click="editReq.type = 'boolean'"
                    >
                      Sí/No
                    </button>
                  </div>
                </div>
                <div class="form-group">
                  <label>Descripción</label>
                  <textarea
                    v-model="editReq.description"
                    rows="2"
                    placeholder="Detalle opcional..."
                  />
                </div>
                <div class="req-chip-edit-actions">
                  <button class="btn-cancel" @click="cancelEditReq">Cancelar</button>
                  <button class="btn-submit" @click="saveEditReq" :disabled="!editReq.title.trim()">
                    Guardar
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div v-if="showNewReqForm" ref="newFormRef" class="req-chip-edit-form req-new-form">
            <div class="req-new-form-header">
              <h3>Nuevo requisito</h3>
            </div>
            <div class="form-group">
              <label>Título del requisito <span class="required">*</span></label>
              <input v-model="newReq.title" type="text" placeholder="Ej. Experiencia con Python" />
            </div>
            <div class="form-group">
              <label>Tipo</label>
              <div class="type-toggle" role="group">
                <button
                  type="button"
                  class="type-toggle-btn"
                  :class="{ active: newReq.type === 'score' }"
                  @click="newReq.type = 'score'"
                >
                  Puntaje
                </button>
                <button
                  type="button"
                  class="type-toggle-btn"
                  :class="{ active: newReq.type === 'boolean' }"
                  @click="newReq.type = 'boolean'"
                >
                  Sí/No
                </button>
              </div>
            </div>
            <div class="form-group">
              <label>
                Descripción
                <span class="tooltip-trigger">
                  <svg
                    width="17"
                    height="17"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                  >
                    <circle cx="12" cy="12" r="10" />
                    <path d="M12 16v-4" />
                    <path d="M12 8h.01" />
                  </svg>
                  <div class="tooltip-content">
                    <strong>Tip:</strong> Sé específico. <br /><br />
                    <strong>Ejemplo:</strong> 3 años con Vue.
                  </div>
                </span>
              </label>
              <textarea v-model="newReq.description" rows="2" placeholder="Detalle opcional..." />
            </div>
            <div class="req-chip-edit-actions">
              <button class="btn-cancel" @click="cancelNewRequirement">Cancelar</button>
              <button
                class="btn-submit"
                @click="saveNewRequirement"
                :disabled="!newReq.title.trim()"
              >
                Guardar
              </button>
            </div>
          </div>
        </div>

        <div v-if="error" class="error-message">{{ error }}</div>
        <div v-if="loading" class="loading-overlay">
          <div class="loading-spinner"></div>
          <span>Creando...</span>
        </div>
      </div>

      <div class="dialog-footer">
        <button class="btn-cancel" @click="close" :disabled="loading">Cancelar</button>
        <button
          class="btn-submit"
          @click="submit"
          :disabled="loading || !title.trim() || !!salaryError"
        >
          <span v-if="loading" class="loading-btn-text">Creando...</span>
          <span v-else>Crear</span>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.dialog-overlay.loading {
  pointer-events: none;
}

.dialog {
  background-color: #f5f5f5;
  border-radius: 8px;
  width: 550px;
  max-width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.dialog-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 1rem;
  background-color: #e0e0e0;
  border-radius: 8px 8px 0 0;
  border-bottom: 1px solid #ccc;
  position: sticky;
  top: 0;
  z-index: 10;
}

.dialog-header h2 {
  margin: 0;
  color: #333;
}

.dialog-header-left {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.dialog-icon {
  color: #666;
  flex-shrink: 0;
}

.dialog-header-text {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}

.dialog-subtitle {
  margin: 0;
  font-size: 0.8rem;
  color: #777;
  line-height: 1.3;
}

.btn-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #666;
  line-height: 1;
  padding: 0 0 0 0.5rem;
}

.btn-close:hover {
  color: #333;
}

.dialog-content {
  padding: 1.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
}

@media (max-width: 500px) {
  .form-row {
    grid-template-columns: 1fr;
  }
}

.form-group {
  margin-bottom: 1.25rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #555;
  font-weight: 500;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: white;
  font-size: 1rem;
  font-family: inherit;
  box-sizing: border-box;
}

.form-group select {
  appearance: none;
  -webkit-appearance: none;
  padding-right: 2.4rem;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 16 16' fill='none'%3E%3Cpath d='M4 6L8 10L12 6' stroke='%23999' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.9rem center;
  cursor: pointer;
}

.salary-wrapper {
  position: relative;
  width: 100%;
  display: flex;
  align-items: center;
}
.salary-prefix {
  position: absolute;
  left: 0.85rem;
  color: #555;
  font-size: 0.95rem;
  font-weight: 700;
  pointer-events: none;
}
/* El .form-group extra le da más especificidad para ganarle al padding shorthand */
.form-group .salary-wrapper input {
  width: 100%;
  box-sizing: border-box;
  padding-left: 2.8rem;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #888;
}

.form-group input:disabled,
.form-group select:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.form-group textarea {
  resize: vertical;
}

.requirements-section {
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 1rem;
  background-color: #fafafa;
}

.requirements-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.requirements-header-left {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.requirements-header label {
  margin-bottom: 0;
}

.count-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 20px;
  height: 18px;
  padding: 0 5px;
  font-size: 0.7rem;
  font-weight: 700;
  color: #d97757;
  background-color: #f4e8e3;
  border-radius: 999px;
}

.btn-add-req {
  padding: 0.4rem 0.8rem;
  background-color: #666;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.85rem;
  transition: opacity 0.15s ease;
}

.btn-add-req:hover {
  background-color: #555;
}

.btn-add-req:disabled {
  opacity: 0.45;
  cursor: not-allowed;
}

.btn-add-req:disabled:hover {
  background-color: #666;
}

.btn-add-req-editing {
  font-style: italic;
}

.no-requirements {
  color: #888;
  font-style: italic;
  text-align: center;
  padding: 1rem;
  background-color: #f0f0f0;
  border-radius: 4px;
}

.req-chips {
  display: flex;
  flex-direction: column;
}

.req-chip-group {
  margin-bottom: 0.5rem;
}

.req-chip-group:last-child {
  margin-bottom: 0;
}

.req-chip {
  display: grid;
  grid-template-columns: auto 1fr auto;
  grid-template-rows: auto auto;
  gap: 0;
  padding: 0.5rem 0.4rem 0.5rem 0.2rem;
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 0.85rem;
  cursor: pointer;
  transition: background-color 0.15s ease;
  width: 100%;
  box-sizing: border-box;
  align-items: center;
}

.req-chip-group:has(.req-chip-edit-form) .req-chip {
  border-radius: 6px 6px 0 0;
  border-bottom: none;
}

.req-chip:hover {
  background-color: #e4e4e4;
}

.req-chip-expand {
  grid-column: 1;
  grid-row: 1 / -1;
  align-self: center;
  background: none;
  border: none;
  cursor: pointer;
  color: #999;
  padding: 0.3rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  flex-shrink: 0;
}

.req-chip-expand:hover {
  color: #555;
  background-color: rgba(0, 0, 0, 0.06);
}

.req-chip-expand .toggle-icon {
  transition: transform 0.2s ease;
}

.req-chip-expand .toggle-icon.rotated {
  transform: rotate(180deg);
}

.req-chip-title {
  grid-column: 2;
  grid-row: 1;
  font-weight: 500;
  color: #333;
}

.req-chip-type {
  color: #666;
  font-size: 0.8rem;
  flex-shrink: 0;
}

.req-chip-desc-sep {
  color: #aaa;
  font-size: 0.8rem;
  flex-shrink: 0;
}

.req-chip-desc {
  color: #666;
  font-size: 0.8rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 0;
}

.req-chip-second {
  grid-column: 2;
  grid-row: 2;
  display: flex;
  align-items: center;
  gap: 0.25rem;
  overflow: hidden;
  margin-top: 0.1rem;
}

.req-chip-remove {
  grid-column: 3;
  grid-row: 1 / -1;
  align-self: center;
  background: none;
  border: none;
  cursor: pointer;
  color: #999;
  line-height: 1;
  padding: 0.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  flex-shrink: 0;
}

.req-chip-remove:hover {
  color: #c0392b;
  background-color: rgba(192, 57, 43, 0.08);
}

.req-chip-edit-form {
  padding: 0.75rem;
  background-color: #fff;
  border: 1px solid #ddd;
  border-top: none;
  border-radius: 0 0 6px 6px;
}

.req-new-form {
  border: 1px solid #ddd;
  border-radius: 6px;
  background-color: #f0f0f0;
  margin-top: 0.5rem;
}

.req-new-form-header {
  padding-bottom: 0.5rem;
  margin-bottom: 0.5rem;
  border-bottom: 1px solid #ddd;
}

.req-new-form-header h3 {
  margin: 0;
  font-size: 0.9rem;
  font-weight: 600;
  color: #555;
}

.req-chip-edit-form .form-group {
  margin-bottom: 0.5rem;
}

.req-chip-edit-form .form-group:last-child {
  margin-bottom: 0;
}

.req-chip-edit-actions {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
  margin-top: 0.75rem;
}

.req-chip-edit-actions .btn-cancel,
.req-chip-edit-actions .btn-submit {
  padding: 0.4rem 1rem;
  font-size: 0.85rem;
}

.tooltip-trigger {
  position: relative;
  display: inline-block;
  line-height: 1;
  margin-left: 4px;
  cursor: help;
  color: #999;
  vertical-align: middle;
}

.tooltip-content {
  display: none;
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  width: 280px;
  padding: 0.65rem 0.75rem;
  background-color: #333;
  color: #f0f0f0;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 400;
  line-height: 1.4;
  white-space: normal;
  z-index: 1000;
  pointer-events: none;
}

.tooltip-content::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 5px solid transparent;
  border-top-color: #333;
}

.tooltip-trigger:hover .tooltip-content {
  display: block;
}

.type-toggle {
  display: inline-flex;
  border: 1px solid #ccc;
  border-radius: 4px;
  overflow: hidden;
  background-color: #fff;
  width: fit-content;
}

.type-toggle-btn {
  padding: 0.4rem 0.75rem;
  background: transparent;
  border: none;
  cursor: pointer;
  font: inherit;
  font-size: 0.85rem;
  color: #555;
  transition:
    background-color 0.15s ease,
    color 0.15s ease;
}

.type-toggle-btn + .type-toggle-btn {
  border-left: 1px solid #ccc;
}

.type-toggle-btn:hover:not(.active) {
  background-color: #f0f0f0;
  color: #333;
}

.type-toggle-btn.active {
  background-color: #d97757;
  color: white;
}

.dialog-footer {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
  padding: 1rem;
  background-color: #e8e8e8;
  border-radius: 0 0 8px 8px;
  border-top: 1px solid #ccc;
  position: sticky;
  bottom: 0;
}

.btn-cancel {
  padding: 0.75rem 1.5rem;
  background-color: #999;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-cancel:hover {
  background-color: #888;
}

.btn-submit {
  padding: 0.75rem 1.5rem;
  background-color: #d97757;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-submit:hover {
  background-color: #c06548;
}

.btn-submit:disabled,
.btn-cancel:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.error-message {
  margin-top: 0.75rem;
  color: #d32f2f;
  font-size: 0.85rem;
  padding: 0.5rem 0.75rem;
  background: rgba(211, 47, 47, 0.08);
  border-radius: 6px;
}

.loading-overlay {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem;
  margin-top: 0.5rem;
  background-color: #f0f7ff;
  border: 1px solid #b8d4f0;
  border-radius: 4px;
  color: #555;
  font-size: 0.875rem;
}

.loading-spinner {
  width: 18px;
  height: 18px;
  border: 2px solid #b8d4f0;
  border-top-color: #666;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
