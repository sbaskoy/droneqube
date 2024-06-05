<template>
    <div class="w-full h-full flex items-center justify-center">
        <div class="w-auto h-auto bg-dark-container p-5 rounded-lg flex flex-col gap-3">
            <div class="space-y-4 ">
                <h5>DroneQube</h5>
                <div class="bg-dark-text-disable text-dark-text-disable h-[1px]"></div>
                <p>Giriş yap</p>
            </div>
            <input v-model="username" class="input w-96" type="email" placeholder="text" />
            <input v-model="password" class="input w-96" type="password" placeholder="Password"
                @keypress.enter="handleLoginButton" />
            <div class="h-2"></div>
            <button class="btn-primary" @click="handleLoginButton">Giriş Yap</button>
        </div>
    </div>
</template>
<script setup lang="ts">
import { useLoginView } from '@/hooks/auth/useLoginView';


const { username, password, handleLoginButton } = useLoginView();

</script>