<script setup></script>

<template>
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-mark">S</div>
      <div>
        <span class="brand-name"> SELECTIA </span>
        <span class="brand-subtitle"> Talent Intelligence </span>
      </div>
    </div>

    <nav class="navigation">
      <div class="nav-section">
        <span class="nav-section-title"> Workspace </span>
        <button class="nav-item active">
          <span class="nav-icon">⌂</span>
          <span>Inicio</span>
        </button>
        <button class="nav-item">
          <span class="nav-icon">▣</span>
          <span>Posiciones</span>
        </button>
        <button class="nav-item">
          <span class="nav-icon">◉</span>
          <span>Candidatos</span>
        </button>
        <button class="nav-item">
          <span class="nav-icon">◷</span>
          <span>Entrevistas</span>
        </button>
      </div>

      <div class="nav-section bottom-section">
        <span class="nav-section-title"> Sistema </span>
        <button class="nav-item">
          <span class="nav-icon">⚙</span>
          <span>Configuración</span>
        </button>
      </div>
    </nav>

    <div class="sidebar-footer">
      <div class="help-icon">?</div>
      <div>
        <span class="help-title"> ¿Necesitas ayuda? </span>
        <span class="help-text"> Consulta el centro de ayuda </span>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 248px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  padding: 28px 16px 18px;
  background: #fffdfb;
  border-right: 1px solid #e7e0d7;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 12px 32px;
}

.brand-mark {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  background: #d97757;
  color: white;
  font-family: Georgia, serif;
  font-size: 21px;
  font-weight: 700;
}

.brand-name {
  display: block;
  color: #29231e;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: 0.12em;
}

.brand-subtitle {
  display: block;
  margin-top: 1px;
  color: #918b83;
  font-size: 9px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.navigation {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.nav-section {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.nav-section-title {
  padding: 0 12px;
  margin-bottom: 8px;
  color: #918b83;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.nav-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 42px;
  padding: 0 12px;
  border: 0;
  border-radius: 8px;
  background: transparent;
  color: #6b6560;
  font-family: inherit;
  font-size: 13px;
  font-weight: 500;
  text-align: left;
  cursor: pointer;
  transition:
    background 150ms ease,
    color 150ms ease;
}

.nav-item:hover {
  background: #f4f2ee;
  color: #29231e;
}

.nav-item.active {
  background: #f4e5de;
  color: #d97757;
  font-weight: 600;
}

.nav-icon {
  width: 20px;
  text-align: center;
  font-size: 15px;
}

.bottom-section {
  margin-top: auto;
  margin-bottom: 24px;
}

.sidebar-footer {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 12px;
  border-top: 1px solid #f0ede7;
}

.help-icon {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #e6e3dd;
  border-radius: 50%;
  color: #6b6560;
  font-size: 12px;
}

.help-title,
.help-text {
  display: block;
}

.help-title {
  color: #29231e;
  font-size: 11px;
  font-weight: 600;
}

.help-text {
  margin-top: 1px;
  color: #918b83;
  font-size: 9px;
}

@media (max-width: 900px) {
  .sidebar {
    width: 210px;
  }
}

@media (max-width: 680px) {
  .sidebar {
    display: none;
  }
}
</style>
