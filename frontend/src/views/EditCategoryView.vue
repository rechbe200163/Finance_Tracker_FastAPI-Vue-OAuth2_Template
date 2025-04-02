<template>
  <div class="p-4">
    <h2 class="text-xl font-bold mb-4">Edit Category</h2>

    <form @submit.prevent="submitUpdateCategory" class="p-4 border rounded">
      <div class="mb-2">
        <label for="name" class="block">Name</label>
        <input
          v-model="categories.name"
          id="name"
          type="text"
          placeholder="Category Name"
          class="p-2 border rounded mb-2 w-full"
          required
        />
      </div>

      <div class="mb-2">
        <label for="type" class="block">Type</label>
        <select
          v-model="categories.type"
          id="type"
          class="p-2 border rounded mb-2 w-full"
          required
        >
          <option value="income" :selected="categories.type === 'income'">
            Income
          </option>
          <option value="expense" :selected="categories.type === 'expense'">
            Expense
          </option>
        </select>
      </div>

      <button type="submit" class="p-2 bg-blue-500 text-white rounded w-full">
        Update Category
      </button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import {
  apiGetCategories,
  apiUpdateCategoryType,
  apiUpdateCategoryName,
} from '../api/categories'; // Assuming you have these functions set up

export default {
  setup() {
    const categories = ref({
      name: '',
      type: '',
    });

    const route = useRoute();
    const router = useRouter();

    // Fetch the current category data using the ID from the route
    const fetchCategory = async () => {
      try {
        const response = await apiGetCategories(route.params.category_id); // Assuming this fetches the correct category
        if (response && response.data) {
          categories.value = response.data; // Prefill the category form with existing data
        }
      } catch (error) {
        console.error('Error fetching category:', error);
      }
    };

    // Submit the updated category data to the backend
    const submitUpdateCategory = async () => {
      try {
        const updatePayload = {
          name: categories.value.name,
          type: categories.value.type,
        };

        // Assuming you update the category using the API functions
        await apiUpdateCategoryName(route.params.category_id, updatePayload); // Update name
        await apiUpdateCategoryType(route.params.category_id, updatePayload); // Update type

        // After success, navigate back to the categories page
        router.push('/categories'); // Adjust to the correct route if needed
      } catch (error) {
        console.error('Error updating category:', error);
      }
    };

    // On component mount, fetch the category data
    onMounted(async () => {
      await fetchCategory();
    });

    return {
      categories,
      submitUpdateCategory,
    };
  },
};
</script>

<style scoped>
/* Add any custom styles here */
</style>
