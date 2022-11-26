<script setup lang="ts">
import { ref } from 'vue';
import { databaseGetProtected } from "../tools/databaseTools"
import { loginUser } from '../tools/jwtTools';

const username = ref("")
const password = ref("")
const isPassword = ref(true)
const validators = ref({ required: value => !!value || 'This field is required' })

const login = async () => {
    console.log("logging in user")
    let rJson = await loginUser(username.value, password.value)
    if (rJson.success) {
        console.log("user logged in successfully")
        whoAmI()
        return
    }
    console.log("Incorrect username or password")
}

const whoAmI = async () => {
    console.log("checking user token")
    let rJson = await databaseGetProtected("users/whoami")
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