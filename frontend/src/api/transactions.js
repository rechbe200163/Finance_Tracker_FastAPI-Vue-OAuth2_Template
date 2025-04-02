import axios from 'axios';
import { useAuthStore } from '../store/auth';

export const apiGetTransactions = () => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.get('/transactions', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    withCredentials: true, // Ensures cookies are sent if using session-based auth
  });
};
// description as a query parameter
export const apiGetTransactionsByDesc = (description) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;

  return axios.get('/transactions', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    params: {
      description,
    },
    withCredentials: true, // Ensures cookies are sent if using session-based auth
  });
};

export const getTransactionsByCategory = (categoryId) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.get(`/transactions/category/${categoryId}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    withCredentials: true, // Ensures cookies are sent if using session-based auth
  });
};

export const getTransactionById = (transactionId) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.get(`/transactions/${transactionId}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    withCredentials: true, // Ensures cookies are sent if using session-based auth
  });
};

export const createTransaction = (transactionData) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.post('/transactions', transactionData, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    withCredentials: true, // Ensures cookies are sent if using session-based auth
  });
};

export const updateTransactionAmount = (transactionId, amount) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.patch(
    `/transactions/${transactionId}/amount`,
    { amount },
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
      withCredentials: true,
    }
  );
};

export const updateTransactionDescription = (transactionId, description) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.patch(
    `/transactions/${transactionId}/description`,
    { description },
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
      withCredentials: true,
    }
  );
};

export const updateTransactionCategory = (transactionId, categoryId) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.patch(
    `/transactions/${transactionId}/category`,
    { category_id: categoryId },
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
      withCredentials: true,
    }
  );
};

export const updateTransactionType = (transactionId, type) => {
  const authStore = useAuthStore();
  const token = authStore.get_access_token;
  return axios.patch(
    `/transactions/${transactionId}/type`,
    { type },
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
      withCredentials: true,
    }
  );
};
