import request from './req';
import axios from 'axios';
import { useAuthStore } from '../store/auth';

export const apiGetCategories = () => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.get('/categories', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    withCredentials: true, // Ensures cookies are sent if using session-based auth
  });
};

export const createCategory = (categoryData) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.post('/categories', categoryData, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    withCredentials: true, // Ensures cookies are sent if using session-based auth
  });
};

// by Id
export const apiGetCategoryById = (category_id) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.get(`/categories/${category_id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    withCredentials: true, // Ensures cookies are sent if using session-based auth
  });
};

// by Name
export const apiGetCategoryByName = (category_name) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.get(`/categories/${category_name}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    withCredentials: true, // Ensures cookies are sent if using session-based auth
  });
};

//update type
export const apiUpdateCategoryType = (category_id, category) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.put(`/categories/${category_id}`, category, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    withCredentials: true, // Ensures cookies are sent if using session-based auth
  });
};

//update name
export const apiUpdateCategoryName = (category_id, category_name) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.put(`/categories/${category_id}`, category_name, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    withCredentials: true, // Ensures cookies are sent if using session-based auth
  });
};

export const apiDeleteCategory = (category_id) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.delete(`/categories/${category_id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    withCredentials: true, // Ensures cookies are sent if using session-based auth
  });
};
