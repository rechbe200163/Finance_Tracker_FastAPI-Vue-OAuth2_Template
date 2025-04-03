<template>
  <div class="p-4">
    <h2 class="text-xl font-bold mb-4">My Transactions</h2>

    <!-- Add Transaction Button -->
    <router-link to="/add-transaction">
      <button class="p-2 bg-green-500 text-white rounded mb-4">
        Add New Transaction
      </button>
    </router-link>

    <label class="block mb-2">Filter by Category:</label>
    <select v-model="selectedCategory" class="p-2 border rounded mb-4 w-full">
      <option value="">All Categories</option>
      <option
        v-for="category in categories"
        :key="category.category_id"
        :value="category.category_id"
      >
        {{ category.name }}
      </option>
    </select>

    <input
      type="text"
      v-model="searchQuery"
      placeholder="Search transactions..."
      class="p-2 border rounded mb-4 w-full"
    />

    <table class="w-full border-collapse border border-gray-300">
      <thead>
        <tr class="bg-gray-100">
          <th class="border p-2">Date</th>
          <th class="border p-2">Amount</th>
          <th class="border p-2">Description</th>
          <th class="border p-2">Type</th>
          <th class="border p-2">Category</th>
          <th class="border p-2">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="transaction in filteredTransactions"
          :key="transaction.transaction_id"
          class="hover:bg-gray-50"
        >
          <td class="border p-2">{{ formatDate(transaction.date) }}</td>
          <td class="border p-2">${{ transaction.amount }}</td>
          <td class="border p-2">{{ transaction.description }}</td>
          <td class="border p-2">{{ transaction.type }}</td>
          <td class="border p-2">
            {{ getCategoryName(transaction.category_id) }}
          </td>
          <td class="border p-2 flex space-x-2">
            <router-link
              :to="`/edit-transaction/${transaction.transaction_id}`"
            >
              <button class="p-2 bg-blue-500 text-white rounded">Edit</button>
            </router-link>
            <button
              @click="deleteTransaction(transaction.transaction_id)"
              class="p-2 bg-red-500 text-white rounded"
            >
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { apiGetTransactions, apiDeleteTransaction } from '../api/transactions';
import { apiGetCategories } from '../api/categories';

export default {
  setup() {
    const transactions = ref([]);
    const categories = ref([]);
    const searchQuery = ref('');
    const selectedCategory = ref('');

    const fetchTransactions = async () => {
      try {
        if (searchQuery.value) {
          const response = await apiGetTransactions(searchQuery.value);
          transactions.value = response.data;
          return;
        }
        const response = await apiGetTransactions();
        transactions.value = response.data;
      } catch (error) {
        console.error('Error fetching transactions:', error);
      }
    };

    const fetchCategories = async () => {
      try {
        const response = await apiGetCategories();
        categories.value = response.data;
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };

    const deleteTransaction = async (transactionId) => {
      try {
        const response = await apiDeleteTransaction(transactionId);

        if (response.status === 200) {
          transactions.value = transactions.value.filter(
            (tx) => tx.transaction_id !== transactionId
          );
        } else {
          console.error('Transaction could not be deleted:', response);
        }
      } catch (error) {
        console.error('Error deleting transaction:', error);
      }
    };

    onMounted(async () => {
      await fetchCategories();
      await fetchTransactions();
    });

    const filteredTransactions = computed(() => {
      let filtered = transactions.value;

      if (selectedCategory.value) {
        filtered = filtered.filter(
          (tx) => tx.category_id === selectedCategory.value
        );
      }

      return filtered.filter((tx) =>
        tx.description.toLowerCase().includes(searchQuery.value.toLowerCase())
      );
    });

    const getCategoryName = (categoryId) => {
      const category = categories.value.find(
        (cat) => cat.category_id === categoryId
      );
      return category ? category.name : 'Unknown';
    };

    const formatDate = (dateString) => {
      const options = { year: 'numeric', month: 'short', day: 'numeric' };
      return new Date(dateString).toLocaleDateString(undefined, options);
    };

    return {
      transactions,
      categories,
      searchQuery,
      selectedCategory,
      filteredTransactions,
      getCategoryName,
      formatDate,
      deleteTransaction,
    };
  },
};
</script>
