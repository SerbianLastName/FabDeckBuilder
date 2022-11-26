<script setup lang="ts">
import { ref } from 'vue';
import { loginUser, databaseGetProtected } from "../tools/databaseTools"

const username = ref("")
const password = ref("")
const isPassword = ref(true)
const validators = ref({ required: value => !!value || 'This field is required' })

const login = async () => {
    let rJson = await loginUser(username.value, password.value)
    if (rJson.success) {
        whoAmI()
        return
    }
    console.log("Incorrect username or password")
}

const whoAmI = async () => {
    let rJson = await databaseGetProtected("https://localhost:5000/users/whoami/")
    console.log(rJson)

}

</script>

<template>
    <w-form>
        <w-input label="Username" static-label v-model="username" :validators="[validators.required]">
        </w-input>
        <w-input class="mb2" label="Password" :type="isPassword ? 'password' : 'text'"
            :inner-icon-left="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
            :inner-icon-right="isPassword ? 'mdi mdi-eye-off' : 'mdi mdi-eye'"
            @click:inner-icon-right="isPassword = !isPassword" v-model="password" :validators="[validators.required]">
        </w-input>
        <w-button :disabled="username == '' || password == ''" @click="login()"> Submit</w-button>
    </w-form>
</template>