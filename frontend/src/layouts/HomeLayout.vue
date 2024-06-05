
import { link } from 'fs';
<template>
    <div class="size-full flex flex-col gap-2">
        <div class="h-20 bg-dark-card flex items-center px-3 ">
            <h3 class="flex-1">DroneQube</h3>
            <div class="flex items-center px-2 gap-3">
                <CustomRouterLink :name="'Drones'">Drones</CustomRouterLink>
                <CustomRouterLink :name="'Tasks'">Tasks</CustomRouterLink>

                <div class=" border border-dark-container rounded-full p-2 hover:bg-dark-card-hover"
                    :class="{ 'bg-dark-card-hover': isVisible }" role="button" ref="targetElement" @click="toggle">
                    <UserIcon class="size-5" />
                </div>
                <Teleport to="body">
                    <div ref="popupElement" class="p-5 rounded-md absolute z-30 bg-dark-card-hover flex flex-col gap-2">
                        <p>{{ user?.user.username }} </p>
                        <p>{{ user?.user.name }} {{ user?.user.last_name }} </p>
                        <button class="hover:bg-dark-bg rounded-md border-none px-3 py-1 font-semibold">Cıkış Yap</button>
                    </div>
                </Teleport>
            </div>
        </div>
        <div class="flex-1 overflow-hidden">
            <RouterView name="home" />
        </div>
    </div>
    <ShowImageDialog/>
</template>
<script setup lang="ts">
import { UserIcon } from '@heroicons/vue/24/solid';
import { usePopup } from "@/hooks/utils/usePopup";
import { useAuthStore } from '@/stores/auth.store';
import { h } from 'vue';
import { RouterLink } from 'vue-router';
import ShowImageDialog from "@/dialogs/show_images_dialog/ShowImageDialog.vue"
const { isVisible, popupElement, targetElement, toggle } = usePopup();

const { user } = useAuthStore();

const CustomRouterLink = (props: any, { slots }: { slots: any }) => {
    return h(RouterLink, {
        to: { name: props.name },
        class: 'hover:text-dark-primary',
        activeClass: 'text-dark-primary'
    }, slots.default());
};

</script>