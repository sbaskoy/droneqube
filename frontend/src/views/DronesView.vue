<template>
    <div class=" flex flex-col gap-2 container m-auto h-full overflow-hidden  ">
        <div class="h-20 border-b flex items-center justify-between border-dark-text-disable border-opacity-40">
            <input class="search-input w-96" placeholder="Drone ara" v-model="filterText" />
            <div class="flex items-center">
                <button class="text-button flex items-center gap-2" @click="handleNewDroneButtonClick">
                    <PlusIcon class="size-5" />
                    Drone Ekle
                </button>
            </div>
        </div>
        <div
            class=" max-h-full overflow-auto grid lg:grid-cols-5 md:grid-cols-3 grid-cols-2 gap-3 scrollbar scrollbar-thumb-dark-bg scrollbar-track-dark-card">
            <template v-if="loading">
                <p class="col-span-full p-5">Dronelar yükleniyor..</p>
            </template>
            <template v-else-if="filteredDrones?.length == 0">
                <p class="col-span-full p-5">Drone bulunamadı</p>
            </template>
            <div v-else v-for="drone in filteredDrones" :key="drone.id"
                class="bg-dark-card p-4 h-40 max-w-96 flex flex-col items-start justify-center gap-2 rounded-md flex-1 overflow-hidden truncate hover:bg-dark-card-hover shadow-sm">
                <p class="font-semibold truncate">{{ drone.name }}</p>
                <p class="font-thin truncate">{{ drone.serial_number }}</p>
                <p class="font-thin rounded-md  bg-dark-card-active px-2 w-auto "
                    :class="[drone.status == DroneStatus.Available] ? 'text-dark-primary' : 'text-red-400'">
                    {{ drone.status }}</p>
                <div class="flex items-center justify-between w-full">
                    <p class="font-thin rounded-md text-dark-primary bg-dark-card-active px-2 w-auto ">
                        {{ `${drone.task_assignments?.length ?? 0} Görev` }}
                    </p>
                    <button class="text-button">
                        <PlusIcon class="size-5" />
                    </button>
                </div>
            </div>
            <p class="col-span-full p-5 hover:text-dark-primary text-center" role="button"
                @click="handleLoadMoreButtonClick">
                {{ filteredDrones?.length }} tane drone gösteriliyor. Daha fazla yüklemek için tıklayınız.
            </p>
        </div>
        <AddDroneDialog />
    </div>
</template>
<script setup lang="ts">
import { useDronesStore } from '@/stores/drones.store';
import { storeToRefs } from 'pinia';
import { PlusIcon } from '@heroicons/vue/24/solid';
import AddDroneDialog from "@/dialogs/add_drone_dialog/AddDroneDialog.vue";
import { useAddDroneDialog } from "@/dialogs/add_drone_dialog/useAddDroneDialog";
import { DroneStatus } from '@/models/drone.model';


const dronesStore = useDronesStore();
const addDroneDialogStore = useAddDroneDialog();

const { loading, filteredDrones, filterText } = storeToRefs(dronesStore);

const handleNewDroneButtonClick = (_: Event) => {
    addDroneDialogStore.showAddDroneDialog();
}
const handleLoadMoreButtonClick = (_: Event) => {
    dronesStore.loadMore();
}

</script>