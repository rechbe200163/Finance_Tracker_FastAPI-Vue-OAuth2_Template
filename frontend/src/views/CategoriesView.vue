<template>
  <div class="p-4">
    <h2 class="text-xl font-bold mb-4">My Transactions</h2>

    <!-- Add Transaction Button -->
    <router-link to="/add-category">
      <button class="p-2 bg-green-500 text-white rounded mb-4">
        Add New Category
      </button>
    </router-link>

    <input
      type="text"
      v-model="searchQuery"
      placeholder="Search categories..."
      class="p-2 border rounded mb-4 w-full"
    />

    <table class="w-full border-collapse border border-gray-300">
      <thead>
        <tr class="bg-gray-100">
          <th class="border p-2">Name</th>
          <th class="border p-2">Type</th>
          <th class="border p-2">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="category in categories"
          :key="category.id"
          class="hover:bg-gray-50"
        >
          <td class="border p-2">{{ category.name }}</td>
          <td class="border p-2">{{ category.type }}</td>
          <td class="border p-2 flex space-x-2">
            <router-link :to="`/edit-category/${category.category_id}`">
              <button class="p-2 bg-blue-500 text-white rounded">Edit</button>
            </router-link>
            <button
              @click="deleteCategory(category.category_id)"
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
import { ref, onMounted } from 'vue';
import { apiGetCategories, apiDeleteCategory } from '../api/categories';

export default {
  setup() {
    const categories = ref([]);
    const searchQuery = ref('');

    const fetchCategories = async () => {
      try {
        const response = await apiGetCategories();
        categories.value = response.data;
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };

    const deleteCategory = async (categoryId) => {
      try {
        await apiDeleteCategory(categoryId);
        categories.value = categories.value.filter(
          (category) => category.category_id !== categoryId
        );
      } catch (error) {
        console.error('Error deleting category:', error);
      }
    };

    onMounted(async () => {
      await fetchCategories();
    });

    return {
      categories,
      searchQuery,
      deleteCategory,
    };
  },
};
</script>
