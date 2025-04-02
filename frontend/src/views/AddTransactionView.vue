<template>
  <div class="p-4">
    <h2 class="text-xl font-bold mb-4">Add New Transaction</h2>

    <form @submit.prevent="submitTransaction" class="p-4 border rounded">
      <input
        v-model="newTransaction.amount"
        type="number"
        placeholder="Amount"
        class="p-2 border rounded mb-2 w-full"
        required
      />
      <input
        v-model="newTransaction.description"
        type="text"
        placeholder="Description"
        class="p-2 border rounded mb-2 w-full"
        required
      />

      <select
        v-model="newTransaction.type"
        class="p-2 border rounded mb-2 w-full"
        required
      >
        <option value="income">Income</option>
        <option value="expense">Expense</option>
      </select>

      <select
        v-model="newTransaction.category_id"
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

      <button type="submit" class="p-2 bg-blue-500 text-white rounded w-full">
        Add Transaction
      </button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { apiGetCategories } from '../api/categories';
import { createTransaction } from '../api/transactions';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const categories = ref([]);
    const newTransaction = ref({
      amount: '',
      description: '',
      type: 'income',
      category_id: '',
    });

    const router = useRouter();

    // Fetch categories for the dropdown
    const fetchCategories = async () => {
      try {
        const response = await apiGetCategories();
        categories.value = response.data;
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };

    onMounted(() => {
      fetchCategories();
    });

    const submitTransaction = async () => {
      try {
        // Add current date
        const transactionData = {
          ...newTransaction.value,
          date: new Date().toISOString(),
        };

        await createTransaction(transactionData);
        router.push('/transactions'); // Redirect back to the transactions page
      } catch (error) {
        console.error('Error creating transaction:', error);
      }
    };

    return {
      newTransaction,
      categories,
      submitTransaction,
    };
  },
};
</script>

<style scoped>
/* Add some styling */
</style>
