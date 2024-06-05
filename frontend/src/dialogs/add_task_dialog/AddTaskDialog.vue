<template>
    <Teleport to="body">
        <transition name="dialog-fade">
            <div class="h-[100vh] w-[100vw] absolute top-0 left-0 flex items-center justify-center  gap-2 bg-dark-bg bg-opacity-60"
                v-show="show">
                <div class="w-96 h-auto  flex flex-col gap-5 bg-dark-container rounded-lg p-5" ref="confirmElement">
                    <div class="flex items-center justify-between w-full">
                        <h5> Yeni Görev Ekle </h5>
                        <button class="text-button" @click="addTaskDialogStore.hideAddTaskDialog">
                            <XMarkIcon class="size-5" />
                        </button>
                    </div>
                    <input v-model="taskName" class="input w-full" placeholder="Görev adı" type="text" />
                    <input v-model="taskDescription" class="input w-full" placeholder="Görev acıklaması" type="text" />
                    <button class="btn-primary" @click="handleAddButtonClick">Ekle</button>
                </div>
            </div>
        </transition>
    </Teleport>
</template>
<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { useAddTaskDialog } from './useAddTaskDialog';
import { XMarkIcon } from '@heroicons/vue/24/solid';

const addTaskDialogStore = useAddTaskDialog();
const { show,taskName,taskDescription } = storeToRefs(addTaskDialogStore);


const handleAddButtonClick = (_: Event) => {
    addTaskDialogStore.addNewTask();
}

</script>