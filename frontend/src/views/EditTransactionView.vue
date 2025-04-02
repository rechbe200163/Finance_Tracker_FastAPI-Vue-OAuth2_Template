<template>
  <div class="p-4">
    <h2 class="text-xl font-bold mb-4">Edit Transaction</h2>

    <form @submit.prevent="submitUpdateTransaction" class="p-4 border rounded">
      <div class="mb-2">
        <label for="amount" class="block">Amount</label>
        <input
          v-model="transaction.amount"
          id="amount"
          type="number"
          placeholder="Amount"
          class="p-2 border rounded mb-2 w-full"
          required
        />
      </div>

      <div class="mb-2">
        <label for="description" class="block">Description</label>
        <input
          v-model="transaction.description"
          id="description"
          type="text"
          placeholder="Description"
          class="p-2 border rounded mb-2 w-full"
          required
        />
      </div>

      <div class="mb-2">
        <label for="type" class="block">Type</label>
        <select
          v-model="transaction.type"
          id="type"
          class="p-2 border rounded mb-2 w-full"
          required
        >
          <option value="income">Income</option>
          <option value="expense">Expense</option>
        </select>
      </div>

      <div class="mb-2">
        <label for="category" class="block">Category</label>
        <select
          v-model="transaction.category_id"
          id="category"
          class="p-2 border rounded mb-2 w-full"
          required
        >
          <option
            v-for="category in categories"
            :key="category.category_id"
            :value="category.category_id"
          >
            {{ category.name }}
          </option>
        </select>
      </div>

      <button type="submit" class="p-2 bg-blue-500 text-white rounded w-full">
        Update Transaction
      </button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { apiGetCategories } from '../api/categories';
import {
  getTransactionById,
  updateTransactionAmount,
  updateTransactionDescription,
  updateTransactionCategory,
  updateTransactionType,
} from '../api/transactions';
import axios from 'axios'; // You can use your axios instance or the default axios

export default {
  setup() {
    const categories = ref([]);
    const transaction = ref({
      amount: '',
      description: '',
      type: 'income',
      category_id: '',
    });

    const route = useRoute();
    const router = useRouter();

    // Fetch the available categories for the dropdown
    const fetchCategories = async () => {
      try {
        const response = await apiGetCategories();
        categories.value = response.data;
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };

    // Fetch the current transaction data using the ID from the route
    const fetchTransaction = async () => {
      try {
        const response = await getTransactionById(route.params.transaction_id);
        // Ensure the response data is properly set to `transaction`
        if (response && response.data) {
          transaction.value = response.data; // Prefill the transaction form with existing data
        }
      } catch (error) {
        console.error('Error fetching transaction:', error);
      }
    };

    // Submit the updated transaction data to the backend
    const submitUpdateTransaction = async () => {
      try {
        // Update each field using respective PUT requests
        const updatePayload = {
          amount: transaction.value.amount,
          description: transaction.value.description,
          type: transaction.value.type,
          category_id: transaction.value.category_id,
        };

        await updateTransactionAmount(
          route.params.transaction_id,
          updatePayload.amount
        );
        await updateTransactionDescription(
          route.params.transaction_id,
          updatePayload.description
        );
        await updateTransactionType(
          route.params.transaction_id,
          updatePayload.type
        );
        await updateTransactionCategory(
          route.params.transaction_id,
          updatePayload.category_id
        );

        // After success, navigate back to the transactions page
        router.push('/transactions');
      } catch (error) {
        console.error('Error updating transaction:', error);
      }
    };

    // On component mount, fetch categories and transaction data
    onMounted(async () => {
      await fetchCategories();
      await fetchTransaction();
    });

    return {
      transaction,
      categories,
      submitUpdateTransaction,
    };
  },
};
</script>

<style scoped>
/* Add any custom styles here */
</style>
