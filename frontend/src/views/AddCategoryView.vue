<template>
  <div class="p-4">
    <h2 class="text-xl font-bold mt-8 mb-4">Create New Category</h2>

    <!-- Category Form -->
    <form @submit.prevent="submitCategory" class="p-4 border rounded">
      <input
        v-model="newCategory.name"
        type="text"
        placeholder="Category Name"
        class="p-2 border rounded mb-2 w-full"
        required
      />

      <select
        v-model="newCategory.type"
        class="p-2 border rounded mb-2 w-full"
        required
      >
        <option value="sports">Sports</option>
        <option value="shopping">Shopping</option>
        <option value="food">Food</option>
        <option value="transport">Transport</option>
        <option value="bills">Bills</option>
        <option value="entertainment">Entertainment</option>
        <option value="other">Other</option>
      </select>

      <button type="submit" class="p-2 bg-blue-500 text-white rounded w-full">
        Create Category
      </button>
    </form>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { apiGetCategories } from '../api/categories';
import { createTransaction } from '../api/transactions';
import { createCategory } from '../api/categories'; // Import the createCategory function
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
    const newCategory = ref({
      name: '',
      type: 'sports', // Default to sports, but this can be adjusted
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

    // Filter categories based on the selected transaction type
    const filteredCategories = computed(() =>
      categories.value.filter(
        (category) => category.type === newTransaction.value.type
      )
    );

    // Submit new transaction
    const submitTransaction = async () => {
      try {
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

    // Submit new category
    const submitCategory = async () => {
      try {
        await createCategory(newCategory.value); // Call the createCategory function
        categories.value.push(newCategory.value); // Update the categories list locally after creating the category

        // Optionally clear the form after creation
        newCategory.value = {
          name: '',
          type: 'sports',
        };

        alert('Category created successfully!');
      } catch (error) {
        console.error('Error creating category:', error);
      }
    };

    // On mounted, fetch categories
    onMounted(() => {
      fetchCategories();
    });

    return {
      newTransaction,
      categories,
      filteredCategories,
      submitTransaction,
      newCategory,
      submitCategory,
    };
  },
};
</script>

<style scoped>
/* Add some custom styling if necessary */
</style>
