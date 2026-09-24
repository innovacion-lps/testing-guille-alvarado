<template>
  <div class="login-page">
    <!-- Fondo decorativo -->
    <div class="background-glow glow-cyan"></div>
    <div class="background-glow glow-indigo"></div>
    <div class="login-card">
      <!-- Encabezado -->
      <div class="logo">
        <div class="logo-icon">✓</div>
        <span>Mi Lista de Tareas</span>
      </div>

      <div class="header">
        <h1>Bienvenidos!!</h1>
        <p>Inicia sesión para continuar</p>
      </div>

      <!-- Formulario -->
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="email">Correo electrónico</label>
          <input id="email" v-model="email" type="email" placeholder="tu@email.com" required />
        </div>

        <div class="form-group">
          <label for="password">Contraseña</label>
          <input id="password" v-model="password" type="password" placeholder="••••••••" required />
        </div>

        <!-- Error -->
        <div v-if="errorMessage" class="error-message">
          {{ errorMessage }}
        </div>

        <!-- Botón -->
        <button type="submit" :disabled="loading">
          {{ loading ? 'Iniciando sesión...' : 'Iniciar sesión' }}
        </button>
      </form>

      <p class="footer-text">Aprende Vue + FastAPI + Supabase 🚀</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { supabase } from '../services/supabase.js'
const emit = defineEmits(['login-success'])

const email = ref('')
const password = ref('')
const loading = ref(false)
const errorMessage = ref('')

async function handleLogin() {
  errorMessage.value = ''
  loading.value = true

  try {
    const { data, error } = await supabase.auth.signInWithPassword({
      email: email.value,
      password: password.value
    })

    if (error) {
      throw error
    }

    console.log('USUARIO:', data.user)
    console.log('SESION:', data.session)
    console.log('ACCESS TOKEN:', data.session?.access_token)

    emit('login-success')
  } catch (error) {
    console.error(error)
    errorMessage.value = error.message
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* =========================================================
   PÁGINA PRINCIPAL
   Estética: Infernal / Futurista / Premium
   ========================================================= */

.login-page {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
  background:
    radial-gradient(circle at 15% 15%, rgba(139, 0, 0, 0.35), transparent 30%),
    radial-gradient(circle at 85% 85%, rgba(124, 58, 237, 0.28), transparent 32%),
    radial-gradient(circle at 50% 110%, rgba(255, 69, 0, 0.22), transparent 38%),
    linear-gradient(135deg, #080303 0%, #120506 45%, #09050f 100%);
  font-family:
    Inter,
    ui-sans-serif,
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    sans-serif;
}

/* =========================================================
   TEXTURA / LUCES DEL FONDO
   ========================================================= */

.login-page::before {
  content: '';
  position: absolute;
  inset: 0;
  background:
    linear-gradient(rgba(255, 255, 255, 0.018) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.018) 1px, transparent 1px);
  background-size: 45px 45px;
  mask-image: linear-gradient(to bottom, transparent, black 25%, black 75%, transparent);
  pointer-events: none;
}

/* =========================================================
   GLOWS
   ========================================================= */

.background-glow {
  position: absolute;
  width: 420px;
  height: 420px;
  border-radius: 50%;
  filter: blur(110px);
  opacity: 0.45;
  pointer-events: none;
}

/* Glow rojo / fuego */

.glow-cyan {
  background: #ff2a00;
  top: -160px;
  left: -140px;
  box-shadow: 0 0 120px rgba(255, 42, 0, 0.55);
}

/* Glow violeta */

.glow-indigo {
  background: #7c3aed;
  bottom: -160px;
  right: -140px;
  box-shadow: 0 0 120px rgba(124, 58, 237, 0.55);
}

/* =========================================================
   CARD PRINCIPAL
   ========================================================= */

.login-card {
  width: 100%;
  max-width: 420px;
  padding: 40px;
  position: relative;
  z-index: 1;
  background: linear-gradient(145deg, rgba(28, 8, 10, 0.88), rgba(12, 7, 18, 0.88));
  border: 1px solid rgba(255, 69, 0, 0.22);
  border-radius: 24px;
  backdrop-filter: blur(24px);
  box-shadow:
    0 30px 90px rgba(0, 0, 0, 0.7),
    0 0 45px rgba(255, 42, 0, 0.08),
    0 0 80px rgba(124, 58, 237, 0.08);
  overflow: hidden;
}

/* Línea luminosa superior */

.login-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 12%;
  right: 12%;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 69, 0, 0.8),
    rgba(139, 92, 246, 0.8),
    transparent
  );
  box-shadow: 0 0 15px rgba(255, 69, 0, 0.5);
}

/* Glow interior */

.login-card::after {
  content: '';
  position: absolute;
  width: 180px;
  height: 180px;
  top: -100px;
  right: -100px;
  border-radius: 50%;
  background: rgba(124, 58, 237, 0.12);
  filter: blur(60px);
  pointer-events: none;
}

/* =========================================================
   LOGO
   ========================================================= */

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 35px;
  color: #f5f5f5;
  font-size: 16px;
  font-weight: 600;
  letter-spacing: 0.2px;
}

/* Icono */

.logo-icon {
  width: 38px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  background: linear-gradient(135deg, #ff3d00, #b91c1c 50%, #7c3aed);
  color: white;
  font-size: 20px;
  box-shadow:
    0 0 20px rgba(255, 61, 0, 0.35),
    0 0 35px rgba(124, 58, 237, 0.18);
  position: relative;
}

/* =========================================================
   HEADER
   ========================================================= */

.header {
  margin-bottom: 30px;
  display: flex;
  flex-direction: column;
}

.header h1 {
  margin: 0 0 8px;
  color: #fff7f5;
  font-size: 32px;
  font-weight: 700;
  letter-spacing: -0.4px;
  text-shadow: 0 0 25px rgba(255, 69, 0, 0.12);
}

.header p {
  margin: 0;
  color: #a8a0a3;
  font-size: 14px;
}

/* =========================================================
   FORMULARIO
   ========================================================= */

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  color: #d6cdd0;
  font-size: 14px;
  font-weight: 500;
}

/* Inputs */

input {
  width: 100%;
  box-sizing: border-box;
  padding: 13px 15px;
  border: 1px solid rgba(255, 255, 255, 0.09);
  border-radius: 12px;
  outline: none;
  background: linear-gradient(145deg, rgba(18, 9, 11, 0.9), rgba(15, 10, 21, 0.9));
  color: #fff5f5;
  font-size: 15px;
  transition:
    border-color 0.25s ease,
    box-shadow 0.25s ease,
    background 0.25s ease;
}

input::placeholder {
  color: #655d62;
}

/* Focus */

input:focus {
  border-color: rgba(255, 69, 0, 0.65);
  background: linear-gradient(145deg, rgba(31, 10, 10, 0.95), rgba(20, 10, 30, 0.95));
  box-shadow:
    0 0 0 3px rgba(255, 69, 0, 0.08),
    0 0 20px rgba(255, 69, 0, 0.12),
    0 0 30px rgba(124, 58, 237, 0.08);
}

/* =========================================================
   BOTÓN
   ========================================================= */

button {
  width: 100%;
  margin-top: 8px;
  padding: 14px;
  border: none;
  border-radius: 12px;
  background: linear-gradient(135deg, #ff3d00 0%, #dc2626 45%, #7c3aed 100%);
  color: white;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition:
    transform 0.2s ease,
    box-shadow 0.25s ease,
    filter 0.25s ease,
    opacity 0.2s ease;
  box-shadow:
    0 10px 30px rgba(255, 61, 0, 0.18),
    0 0 25px rgba(124, 58, 237, 0.12);
}

/* Hover */

button:hover {
  transform: translateY(-2px);
  filter: brightness(1.08);
  box-shadow:
    0 14px 35px rgba(255, 61, 0, 0.25),
    0 0 35px rgba(124, 58, 237, 0.22);
}

/* Click */

button:active {
  transform: translateY(0);
}

/* Disabled */

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

/* =========================================================
   ERROR
   ========================================================= */

.error-message {
  margin-bottom: 15px;
  padding: 10px 12px;
  border-radius: 10px;
  background: linear-gradient(135deg, rgba(127, 29, 29, 0.25), rgba(76, 29, 149, 0.12));
  border: 1px solid rgba(248, 113, 113, 0.22);
  color: #fca5a5;
  font-size: 13px;
  box-shadow: 0 0 20px rgba(239, 68, 68, 0.05);
}

/* =========================================================
   FOOTER
   ========================================================= */

.footer-text {
  margin: 25px 0 0;
  text-align: center;
  color: #6f686c;
  font-size: 12px;
  letter-spacing: 0.2px;
}

/* =========================================================
   RESPONSIVE
   ========================================================= */

@media (max-width: 500px) {
  .login-card {
    margin: 20px;
    padding: 30px 24px;
  }
}
</style>
