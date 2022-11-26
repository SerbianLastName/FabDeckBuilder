<script setup lang="ts">
import LoginVue from '../components/Login.vue';
</script>

<template>
    <w-card title="Router Test Home" title-class="blue-light3--bg" color="black">
        <router-link to="/">Go to Home</router-link>
        <br />
        <router-link to="/builder">Go to Builder</router-link>
        <LoginVue />
    </w-card>
</template>