<script setup>
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'

const props = defineProps({
  modelValue: { type: String, default: '' },
  // Acepta ['COP', ...] o [{ value: 'CO', label: 'Colombia' }, ...]
  options: { type: Array, default: () => [] },
  placeholder: { type: String, default: 'Seleccionar' },
  disabled: { type: Boolean, default: false }
})

const emit = defineEmits(['update:modelValue'])

const rootRef = ref(null)
const isOpen = ref(false)

const normalizedOptions = computed(() =>
  props.options.map(option =>
    typeof option === 'string' ? { value: option, label: option } : option
  )
)

const selectedLabel = computed(
  () => normalizedOptions.value.find(option => option.value === props.modelValue)?.label || ''
)

function toggle() {
  if (props.disabled) return
  isOpen.value = !isOpen.value
}

function close() {
  isOpen.value = false
}

function choose(option) {
  if (props.disabled) return
  emit('update:modelValue', option)
  close()
}

function onDocumentClick(e) {
  if (rootRef.value && !rootRef.value.contains(e.target)) close()
}

function onKeydown(e) {
  // Si la lista está abierta, Escape solo la cierra y no deja que el
  // overlay del modal también se cierre (evita el doble cierre).
  if (e.key === 'Escape' && isOpen.value) {
    close()
    e.stopPropagation()
  }
}

onMounted(() => {
  document.addEventListener('click', onDocumentClick)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', onDocumentClick)
})
</script>

<template>
  <div
    ref="rootRef"
    class="custom-select"
    :class="{ open: isOpen, disabled }"
    @keydown="onKeydown"
  >
    <button
      type="button"
      class="select-trigger"
      :disabled="disabled"
      @click="toggle"
    >
      <span class="select-value" :class="{ empty: !selectedLabel }">
        {{ selectedLabel || placeholder }}
      </span>
      <svg
        class="select-chevron"
        :class="{ rotated: isOpen }"
        width="16"
        height="16"
        viewBox="0 0 16 16"
        fill="none"
      >
        <path
          d="M4 6L8 10L12 6"
          stroke="currentColor"
          stroke-width="1.6"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </svg>
    </button>

    <ul v-if="isOpen" class="select-options">
      <li
        v-for="option in normalizedOptions"
        :key="option.value"
        class="select-option"
        :class="{ selected: option.value === modelValue }"
        @click="choose(option.value)"
      >
        {{ option.label }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
.custom-select {
  position: relative;
  width: 100%;
  min-width: 0;
}

.select-trigger {
  width: 100%;
  height: 50px;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 0 14px;
  background: white;
  border: 1px solid #e6e3dd;
  border-radius: 12px;
  color: #4f4a45;
  font-size: 14px;
  font-family: inherit;
  cursor: pointer;
  text-align: left;
}

.select-trigger:hover {
  border-color: #d8cfc5;
}

.custom-select.open .select-trigger {
  border-color: #d97757;
  box-shadow: 0 0 0 3px rgba(217, 119, 87, 0.08);
}

.select-value {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.select-value.empty {
  color: #b0aaa2;
}

.select-chevron {
  flex-shrink: 0;
  color: #999;
  transition: transform 0.2s ease;
}

.select-chevron.rotated {
  transform: rotate(180deg);
}

.select-options {
  position: absolute;
  top: calc(100% + 6px);
  left: 0;
  right: 0;
  z-index: 50;
  margin: 0;
  padding: 6px;
  list-style: none;
  background: white;
  border: 1px solid #e6e3dd;
  border-radius: 12px;
  box-shadow: 0 12px 32px rgba(42, 37, 32, 0.12);
  max-height: 220px;
  overflow-y: auto;
}

.select-option {
  padding: 10px 12px;
  border-radius: 8px;
  font-size: 14px;
  color: #4f4a45;
  cursor: pointer;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.select-option:hover {
  background: #f7f3ed;
}

.select-option.selected {
  background: #f4e5de;
  color: #b65e43;
  font-weight: 600;
}

.custom-select.disabled .select-trigger {
  background: #f4f2ee;
  color: #aaa;
  cursor: not-allowed;
}
</style>
