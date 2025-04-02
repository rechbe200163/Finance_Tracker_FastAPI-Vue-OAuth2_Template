import { createRouter, createWebHashHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ProfileView from '../views/ProfileView.vue';
import LoginView from '../views/LoginView.vue';
import RegisterView from '../views/RegisterView.vue';
import LogoutView from '../views/LogoutView.vue';
import RefreshView from '../views/RefreshView.vue';
import TransactionsView from '../views/TransactionsView.vue';
import AddTransactionsView from '../views/AddTransactionView.vue';
import EditTransactionView from '../views/EditTransactionView.vue';
import EditCategoryView from '../views/EditCategoryView.vue';
import CategoriesView from '../views/CategoriesView.vue';
import AddCategoryView from '../views/AddCategoryView.vue';
import { useAuthStore } from '../store/auth';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: '/logout',
    name: 'Logout',
    component: LogoutView,
  },
  {
    path: '/refresh',
    name: 'Refresh',
    component: RefreshView,
  },
  {
    path: '/transactions',
    name: 'Transactions',
    component: TransactionsView,
    meta: { requiresAuth: true },
  },
  {
    path: '/add-transaction',
    name: 'AddTransaction',
    component: AddTransactionsView,
    meta: { requiresAuth: true },
  },
  {
    path: '/edit-transaction/:transaction_id', // Route for editing a specific transaction
    name: 'EditTransaction',
    component: EditTransactionView,
    meta: { requiresAuth: true },
  },
  {
    path: '/categories', // Route for editing a specific transaction
    name: 'CategoriesView',
    component: CategoriesView,
    meta: { requiresAuth: true },
  },
  {
    path: '/add-category',
    name: 'AddCategory',
    component: AddCategoryView,
    meta: { requiresAuth: true },
  },
  {
    path: '/edit-category/:category_id', // Route for editing a specific transaction
    name: 'EditTransaction',
    component: EditCategoryView,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
});

router.beforeEach((to, from, next) => {
  const auth = useAuthStore();
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (auth.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router;
