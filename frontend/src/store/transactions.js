import { ref } from 'vue';
import {
  apiGetMyself,
  apiUpdatePass,
  apiUpdateBirth,
  apiDelateAccount,
} from '../api/me';
import { useLoadingStore } from './loading';
import { useDialogStore } from './dialog';
import { useAuthStore } from './auth';
import { apiGetTransactions } from '../api/transactions';

function transactions() {
  const loadingStore = useLoadingStore();
  const dialogStore = useDialogStore();
  const authStore = useAuthStore();

  // can't use `reactive` here
  // because `reactive` can only be used with `Array` ,`Map` or `Set`

  const getTransactions = async () => {
    loadingStore.setLoading();
    apiGetTransactions()
      .then((res) => {
        console.log(res.data);
        dialogStore.setSuccess({
          title: 'Load Data Success',
          firstLine: 'Successfully loaded your data',
          secondLine: 'This dialog will close in 1 seconds',
        });
      })
      .catch((err) => {
        console.log(err);
      })
      .finally(() => {
        loadingStore.clearLoading();
        setTimeout(() => {
          dialogStore.reset();
        }, 1000);
      });
  };

  // load data before component mounted
  getTransactions();

  return {
    getTransactions,
  };
}

export { transactions };
