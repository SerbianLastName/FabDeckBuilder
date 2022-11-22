import { createRouter, createWebHistory } from "vue-router";
import Home from "./pages/home.vue";
import Builder from "./pages/builder.vue";

export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: Home,
    },
    {
      path: "/builder",
      component: Builder,
    },
  ],
});
