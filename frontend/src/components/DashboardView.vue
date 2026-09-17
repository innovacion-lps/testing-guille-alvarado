<script setup>
import { computed, ref } from 'vue'

const positions = ref([
  {
    id: 1,
    title: 'Senior Backend Developer',
    department: 'Tecnología',
    candidates: 24,
    shortlisted: 6,
    status: 'active',
    updated: 'Hace 2 horas',
  },
  {
    id: 2,
    title: 'Product Designer',
    department: 'Diseño',
    candidates: 18,
    shortlisted: 4,
    status: 'active',
    updated: 'Hace 5 horas',
  },
  {
    id: 3,
    title: 'Talent Acquisition Specialist',
    department: 'Recursos Humanos',
    candidates: 31,
    shortlisted: 8,
    status: 'active',
    updated: 'Ayer',
  },
  {
    id: 4,
    title: 'Frontend Developer',
    department: 'Tecnología',
    candidates: 27,
    shortlisted: 6,
    status: 'paused',
    updated: 'Hace 2 días',
  },
])

const activePositions = computed(() => {
  return positions.value.filter(
    position => position.status === 'active'
  ).length
})

const totalCandidates = computed(() => {
  return positions.value.reduce(
    (total, position) => total + position.candidates,
    0
  )
})

const totalShortlisted = computed(() => {
  return positions.value.reduce(
    (total, position) => total + position.shortlisted,
    0
  )
})

function statusLabel(status) {
  const labels = {
    active: 'En proceso',
    paused: 'Pausada',
    closed: 'Cerrada',
  }

  return labels[status]
}
</script>

<template>
  <div class="dashboard">

    <!-- SIDEBAR -->
    <aside class="sidebar">

      <div class="brand">

        <div class="brand-mark">
          S
        </div>

        <div>
          <span class="brand-name">
            SELECTIA
          </span>

          <span class="brand-subtitle">
            Talent Intelligence
          </span>
        </div>

      </div>

      <nav class="navigation">

        <div class="nav-section">

          <span class="nav-section-title">
            Workspace
          </span>

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

          <span class="nav-section-title">
            Sistema
          </span>

          <button class="nav-item">
            <span class="nav-icon">⚙</span>
            <span>Configuración</span>
          </button>

        </div>

      </nav>

      <div class="sidebar-footer">

        <div class="help-icon">
          ?
        </div>

        <div>
          <span class="help-title">
            ¿Necesitas ayuda?
          </span>

          <span class="help-text">
            Consulta el centro de ayuda
          </span>
        </div>

      </div>

    </aside>


    <!-- CONTENIDO PRINCIPAL -->
    <main class="main-content">

      <!-- TOPBAR -->
      <header class="topbar">

        <div class="breadcrumb">
          <span>Workspace</span>

          <span class="breadcrumb-separator">
            /
          </span>

          <strong>Inicio</strong>
        </div>


        <div class="user-area">

          <button
            class="notification-button"
            aria-label="Notificaciones"
          >
            ♧

            <span class="notification-dot"></span>
          </button>


          <div class="user-profile">

            <div class="avatar">
              GA
            </div>

            <div class="user-info">

              <span class="user-name">
                Guillermo Alvarado
              </span>

              <span class="user-role">
                Recruiter
              </span>

            </div>

            <span class="dropdown-arrow">
              ⌄
            </span>

          </div>

        </div>

      </header>


      <!-- CONTENIDO -->
      <div class="page-content">

        <!-- INTRO -->
        <section class="page-intro">

          <div>

            <p class="eyebrow">
              DASHBOARD
            </p>

            <h1>
              Buenos días, Guillermo
            </h1>

            <p class="intro-description">
              Gestiona tus procesos de selección y encuentra el talento adecuado.
            </p>

          </div>


          <button class="primary-button">

            <span class="plus-icon">
              +
            </span>

            Nueva posición

          </button>

        </section>


        <!-- MÉTRICAS -->
        <section class="metrics-grid">

          <article class="metric-card">

            <div class="metric-header">

              <span class="metric-label">
                Posiciones activas
              </span>

              <div class="metric-icon orange">
                ▣
              </div>

            </div>

            <div class="metric-value">
              {{ activePositions }}
            </div>

            <p class="metric-description">
              Procesos actualmente abiertos
            </p>

          </article>


          <article class="metric-card">

            <div class="metric-header">

              <span class="metric-label">
                Candidatos
              </span>

              <div class="metric-icon beige">
                ◉
              </div>

            </div>

            <div class="metric-value">
              {{ totalCandidates }}
            </div>

            <p class="metric-description">
              Candidatos en tus procesos
            </p>

          </article>


          <article class="metric-card">

            <div class="metric-header">

              <span class="metric-label">
                En shortlist
              </span>

              <div class="metric-icon green">
                ✓
              </div>

            </div>

            <div class="metric-value">
              {{ totalShortlisted }}
            </div>

            <p class="metric-description">
              Candidatos preseleccionados
            </p>

          </article>

        </section>


        <!-- PROCESOS -->
        <section class="positions-section">

          <div class="section-header">

            <div>

              <h2>
                Procesos de selección
              </h2>

              <p>
                Revisa el estado de tus posiciones abiertas.
              </p>

            </div>

            <button class="text-button">
              Ver todas
              <span>→</span>
            </button>

          </div>


          <div class="positions-list">

            <article
              v-for="position in positions"
              :key="position.id"
              class="position-card"
            >

              <div class="position-main">

                <div class="position-title-row">

                  <div class="position-icon">
                    {{ position.title.charAt(0) }}
                  </div>

                  <div>

                    <h3>
                      {{ position.title }}
                    </h3>

                    <span class="department">
                      {{ position.department }}
                    </span>

                  </div>

                </div>


                <div class="position-stats">

                  <div class="position-stat">

                    <span class="stat-number">
                      {{ position.candidates }}
                    </span>

                    <span class="stat-label">
                      candidatos
                    </span>

                  </div>

                  <div class="stat-divider"></div>

                  <div class="position-stat">

                    <span class="stat-number">
                      {{ position.shortlisted }}
                    </span>

                    <span class="stat-label">
                      shortlist
                    </span>

                  </div>

                </div>

              </div>


              <div class="position-footer">

                <div class="position-status">

                  <span
                    class="status-dot"
                    :class="position.status"
                  ></span>

                  <span>
                    {{ statusLabel(position.status) }}
                  </span>

                </div>

                <span class="updated">
                  {{ position.updated }}
                </span>

                <button class="view-button">
                  Ver proceso
                  <span>→</span>
                </button>

              </div>

            </article>

          </div>

        </section>

      </div>

    </main>

  </div>
</template>


<style scoped>

.dashboard {
  min-height: 100vh;

  display: flex;

  background: #f7f3ed;
}


/* SIDEBAR */

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


/* MAIN */

.main-content {
  flex: 1;

  min-width: 0;
}


/* TOPBAR */

.topbar {
  height: 72px;

  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: 0 40px;

  background: #fffdfb;

  border-bottom: 1px solid #e7e0d7;
}


.breadcrumb {
  display: flex;
  align-items: center;

  gap: 8px;

  color: #918b83;

  font-size: 12px;
}


.breadcrumb strong {
  color: #29231e;

  font-weight: 500;
}


.breadcrumb-separator {
  color: #e6e3dd;
}


.user-area {
  display: flex;
  align-items: center;

  gap: 20px;
}


.notification-button {
  position: relative;

  width: 36px;
  height: 36px;

  border: 0;

  border-radius: 50%;

  background: transparent;

  color: #6b6560;

  cursor: pointer;
}


.notification-button:hover {
  background: #f4f2ee;
}


.notification-dot {
  position: absolute;

  top: 7px;
  right: 7px;

  width: 6px;
  height: 6px;

  border-radius: 50%;

  background: #d97757;
}


.user-profile {
  display: flex;
  align-items: center;

  gap: 10px;

  cursor: pointer;
}


.avatar {
  width: 34px;
  height: 34px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 50%;

  background: #f4e5de;

  color: #d97757;

  font-size: 11px;
  font-weight: 700;
}


.user-info {
  display: flex;
  flex-direction: column;
}


.user-name {
  color: #29231e;

  font-size: 12px;
  font-weight: 600;
}


.user-role {
  margin-top: 1px;

  color: #918b83;

  font-size: 10px;
}


.dropdown-arrow {
  color: #918b83;

  font-size: 14px;
}


/* PAGE */

.page-content {
  max-width: 1280px;

  margin: 0 auto;

  padding: 42px 40px 60px;
}


.page-intro {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;

  margin-bottom: 34px;
}


.eyebrow {
  margin-bottom: 8px;

  color: #d97757;

  font-size: 10px;
  font-weight: 700;

  letter-spacing: 0.14em;
}


h1 {
  color: #29231e;

  font-family: Georgia, serif;

  font-size: 34px;

  letter-spacing: -0.02em;
}


.intro-description {
  margin-top: 8px;

  color: #6b6560;

  font-size: 13px;
}


/* BUTTON */

.primary-button {
  display: inline-flex;
  align-items: center;

  gap: 8px;

  height: 42px;

  padding: 0 18px;

  border: 0;

  border-radius: 8px;

  background: #d97757;

  color: white;

  font-family: inherit;

  font-size: 12px;
  font-weight: 600;

  cursor: pointer;

  box-shadow: 0 1px 3px rgba(42, 37, 32, 0.08);

  transition:
    background 150ms ease,
    transform 150ms ease,
    box-shadow 150ms ease;
}


.primary-button:hover {
  background: #c96643;

  transform: translateY(-1px);

  box-shadow: 0 4px 12px rgba(42, 37, 32, 0.12);
}


.plus-icon {
  font-size: 18px;

  font-weight: 400;

  line-height: 1;
}


/* METRICS */

.metrics-grid {
  display: grid;

  grid-template-columns: repeat(3, 1fr);

  gap: 16px;

  margin-bottom: 44px;
}


.metric-card {
  padding: 20px;

  background: #fffdfb;

  border: 1px solid #e7e0d7;

  border-radius: 12px;

  box-shadow: 0 1px 3px rgba(42, 37, 32, 0.06);
}


.metric-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}


.metric-label {
  color: #6b6560;

  font-size: 11px;

  font-weight: 600;
}


.metric-icon {
  width: 32px;
  height: 32px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 8px;

  font-size: 13px;
}


.metric-icon.orange {
  background: #f4e5de;

  color: #d97757;
}


.metric-icon.beige {
  background: #f4f2ee;

  color: #6b6560;
}


.metric-icon.green {
  background: #edf4ee;

  color: #6b9f78;
}


.metric-value {
  margin-top: 14px;

  color: #29231e;

  font-family: Georgia, serif;

  font-size: 32px;

  font-weight: 600;

  line-height: 1;
}


.metric-description {
  margin-top: 7px;

  color: #918b83;

  font-size: 10px;
}


/* POSITIONS */

.positions-section {
  margin-top: 4px;
}


.section-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;

  margin-bottom: 18px;
}


.section-header h2 {
  color: #29231e;

  font-family: Georgia, serif;

  font-size: 23px;
}


.section-header p {
  margin-top: 5px;

  color: #918b83;

  font-size: 11px;
}


.text-button {
  display: inline-flex;
  align-items: center;

  gap: 8px;

  border: 0;

  background: transparent;

  color: #d97757;

  font-family: inherit;

  font-size: 12px;
  font-weight: 600;

  cursor: pointer;
}


.text-button:hover {
  color: #c96643;
}


/* POSITION CARD */

.positions-list {
  display: flex;
  flex-direction: column;

  gap: 10px;
}


.position-card {
  padding: 20px 22px;

  background: #fffdfb;

  border: 1px solid #e7e0d7;

  border-radius: 12px;

  box-shadow: 0 1px 3px rgba(42, 37, 32, 0.06);

  transition:
    border-color 150ms ease,
    box-shadow 150ms ease,
    transform 150ms ease;
}


.position-card:hover {
  border-color: #dcd4ca;

  box-shadow: 0 4px 12px rgba(42, 37, 32, 0.08);

  transform: translateY(-1px);
}


.position-main {
  display: flex;
  align-items: center;
  justify-content: space-between;

  padding-bottom: 18px;
}


.position-title-row {
  display: flex;
  align-items: center;

  gap: 13px;
}


.position-icon {
  width: 40px;
  height: 40px;

  display: flex;
  align-items: center;
  justify-content: center;

  flex-shrink: 0;

  border-radius: 10px;

  background: #f4f2ee;

  color: #6b6560;

  font-family: Georgia, serif;

  font-size: 18px;

  font-weight: 600;
}


.position-card:first-child .position-icon {
  background: #f4e5de;

  color: #d97757;
}


.position-title-row h3 {
  color: #29231e;

  font-family: Georgia, serif;

  font-size: 16px;

  font-weight: 600;
}


.department {
  display: block;

  margin-top: 4px;

  color: #918b83;

  font-size: 10px;
}


.position-stats {
  display: flex;
  align-items: center;

  gap: 20px;
}


.position-stat {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}


.stat-number {
  color: #29231e;

  font-family: Georgia, serif;

  font-size: 19px;

  font-weight: 600;
}


.stat-label {
  margin-top: 2px;

  color: #918b83;

  font-size: 9px;
}


.stat-divider {
  width: 1px;
  height: 30px;

  background: #e7e0d7;
}


.position-footer {
  display: flex;
  align-items: center;

  padding-top: 14px;

  border-top: 1px solid #f0ede7;
}


.position-status {
  display: flex;
  align-items: center;

  gap: 7px;

  color: #6b6560;

  font-size: 10px;

  font-weight: 500;
}


.status-dot {
  width: 7px;
  height: 7px;

  border-radius: 50%;
}


.status-dot.active {
  background: #6b9f78;
}


.status-dot.paused {
  background: #e5a85b;
}


.status-dot.closed {
  background: #918b83;
}


.updated {
  margin-left: 18px;

  color: #918b83;

  font-size: 9px;
}


.view-button {
  margin-left: auto;

  display: inline-flex;
  align-items: center;

  gap: 7px;

  border: 0;

  background: transparent;

  color: #d97757;

  font-family: inherit;

  font-size: 10px;

  font-weight: 600;

  cursor: pointer;
}


.view-button:hover {
  color: #c96643;
}


/* RESPONSIVE */

@media (max-width: 900px) {

  .sidebar {
    width: 210px;
  }

  .topbar {
    padding: 0 24px;
  }

  .page-content {
    padding: 32px 24px 50px;
  }

  .metrics-grid {
    grid-template-columns: 1fr;
  }

  .page-intro {
    align-items: flex-start;

    flex-direction: column;

    gap: 20px;
  }

}


@media (max-width: 680px) {

  .sidebar {
    display: none;
  }

  .topbar {
    padding: 0 18px;
  }

  .breadcrumb {
    display: none;
  }

  .page-content {
    padding: 28px 18px 40px;
  }

  h1 {
    font-size: 28px;
  }

  .user-info,
  .dropdown-arrow {
    display: none;
  }

  .position-main {
    align-items: flex-start;

    flex-direction: column;

    gap: 18px;
  }

  .position-stats {
    align-self: flex-start;
  }

}

</style>