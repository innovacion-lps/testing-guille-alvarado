import axios from 'axios'
import { supabase } from './supabase'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8007'
})

api.interceptors.request.use(async config => {
  const { data } = await supabase.auth.getSession()

  console.log('SESION DESDE AXIOS:', data.session)

  const token = data.session?.access_token

  console.log('TOKEN DESDE AXIOS:', token)

  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }

  return config
})

export default api
