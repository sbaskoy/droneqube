<template>
    <Teleport to="body">
        <transition name="dialog-fade">
            <div class="h-[100vh] w-[100vw] absolute top-0 left-0 flex items-center justify-center  gap-2 bg-dark-bg bg-opacity-60"
                v-show="show">
                <div class="w-96 h-auto  flex flex-col gap-5 bg-dark-container rounded-lg p-5" ref="confirmElement">
                    <div class="flex items-center justify-between w-full">
                        <h5> Yeni Drone Ekle </h5>
                        <button class="text-button" @click="handleCloseButtonClick">
                            <XMarkIcon class="size-5" />
                        </button>
                    </div>
                    <input @keypress.enter="handleAddButtonClick"  v-model="droneName" class="input w-full" placeholder="Drone adı" type="text" />
                    <input @keypress.enter="handleAddButtonClick" v-model="droneSerialNumber" class="input w-full" placeholder="Seri numarası" type="text" />
                    <button class="btn-primary" @click="handleAddButtonClick">Ekle</button>
                </div>
            </div>
        </transition>
    </Teleport>
</template>
<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { useAddDroneDialog } from './useAddDroneDialog';
import { XMarkIcon } from '@heroicons/vue/24/solid';

const addDroneDialogStore = useAddDroneDialog();
const { show, droneName, droneSerialNumber } = storeToRefs(addDroneDialogStore);


const handleCloseButtonClick = (_: Event) => {
    addDroneDialogStore.hideAddDroneDialog();
}

const handleAddButtonClick = (_: Event) => {
    addDroneDialogStore.addNewDrone();
}

</script>