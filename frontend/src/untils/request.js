import axios from "axios";
export const http = axios.create({
  baseURL: 'http://localhost:3000/',
  timeout: 1000 * 60 * 2,
  withCredentials: true,
})
http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
