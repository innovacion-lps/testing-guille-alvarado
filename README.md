# Mi Lista Tareas — Vue + FastAPI + Supabase

## Contexto y objetivo
Proyecto de inducción de Guillermo Alvarado: construir una app web real de punta a punta para aprender cómo se conectan frontend, backend, APIs, base de datos, autenticación y seguridad, entendiendo cada pieza.

Empezó como lista de tareas y evolucionó a un mini ATS de reclutamiento:
- Login con Supabase Auth (`frontend/src/components/login.vue` → `supabase.auth.signInWithPassword`).
- Dashboard (`DashboardView.vue`): métricas (posiciones activas, candidatos, shortlist), lista de procesos de selección y modal "My tasks".
- Crear posición (`CreatePositionDialog.vue`): título, descripción, país/moneda, rango salarial, requisitos (jsonb).
- Backend FastAPI (`backend/src/main.py`): `GET /`, `GET /me`, `GET/POST /tasks`, `GET/POST /positions`, más `GET/PUT/DELETE /tasks/{id}`. Todo filtrado por `user_id` del token.
- Datos en Postgres/Supabase con RLS por usuario: `tasks`, `positions`, `categories`.

Stack: Vue 3 + Vite + axios + supabase-js / FastAPI + uvicorn + python-dotenv + supabase-py / Supabase local (`supabase status`) y remota.

## Único `.env` (raíz)
Solo existe `/.env`. Se carga así:
- Backend `backend/src/database.py`: `load_dotenv(dotenv_path=.../raíz/.env)` con `SUPABASE_URL` + `SUPABASE_KEY`.
- Frontend `frontend/vite.config.js`: `envDir: '../'` con `VITE_SUPABASE_URL` + `VITE_SUPABASE_ANON_KEY` (`frontend/src/services/supabase.js`).

Ver `/.env.example`. Copiar a `/.env` y rellenar. Para cambiar de entorno, comentar un bloque y descomentar el otro. Reiniciar backend y `npm run dev` (solo leen al arrancar).

## Keys: cuál va dónde
- Backend `SUPABASE_KEY` = `sb_secret_...` (bypassa RLS). Nunca con prefijo `VITE_`, nunca en frontend.
- Frontend `VITE_SUPABASE_ANON_KEY` = `sb_publishable_...` (respeta RLS, pública por diseño, queda en el JS).
- Local: `supabase status` → `Project URL`, `Publishable`, `Secret`. Las `Access/Secret Key` de `Storage (S3)` no sirven para Auth.
- Remoto: Dashboard → Settings → API.

## Seguridad / GitHub
- `/.gitignore` ignora `.env`, `.env.*` (permite `.env.example`), `supabase/.temp/`, `opencode.json`.
- Nunca se subió un `.env` real ni keys hardcodeadas (solo `os.getenv(...)`).
- En Railway/Vercel poner las 4 vars en `Variables` (Vite las incrusta en el build, no hay `.env` allá).
- Si se fuga una `secret`, rotarla en el Dashboard.

## Supabase local
```sh
supabase status
supabase db dump --local --schema public
```

## Migración `positions` (ejemplo)
La tabla no existía en remoto (`PGRST205`) y el `POST` fallaba por RLS (`42501`). Se creó en SQL Editor remoto con su policy `users own positions` (`auth.uid() = user_id`), grants e inserts remapeando `user_id` al id remoto. Estructura se migra, datos no se copian solos.

## Deploy Railway
Verificar commit desplegado, poner `Variables`, `Redeploy`, recarga dura `Ctrl+Shift+R`. Los logs de Caddy no son logs de la app.

## Troubleshooting
- `GET 200` vacío + `POST 500 42501` = backend con `publishable` en vez de `secret`.
- `500 PGRST205 Could not find table public.positions` = falta migración en ese proyecto.
- `CORS blocked` tras un `500` suele ser consecuencia, no causa.
- `401 handshake timed out` suelto = red a Supabase, reintentar.
- Quitar `print()` de debug en `backend/src/auth.py` y `backend/src/main.py` antes de producción.
