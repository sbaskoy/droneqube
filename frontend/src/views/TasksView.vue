<template>
    <div class=" flex flex-col gap-2 container m-auto h-full overflow-hidden  ">
        <div class="h-20 border-b flex items-center justify-between border-dark-text-disable border-opacity-40">
            <input class="search-input w-96" placeholder="Görev ara" v-model="filterText" />
            <div class="flex items-center">
                <button class="text-button flex items-center gap-2" @click="handleNewTaskButtonClick">
                    <PlusIcon class="size-5" />
                    Görev Ekle
                </button>
            </div>
        </div>
        <div
            class=" max-h-full overflow-auto grid lg:grid-cols-5 md:grid-cols-3 grid-cols-2 gap-3 scrollbar scrollbar-thumb-dark-bg scrollbar-track-dark-card">
            <template v-if="loading">
                <p class="col-span-full p-5">Görevler yükleniyor..</p>
            </template>
            <template v-else-if="filteredTasks?.length == 0">
                <p class="col-span-full p-5">Görev bulunamadı</p>
            </template>
            <template v-else>
                <TaskItem v-for="task in filteredTasks" :key="task.id" :task="task" @on-show-images="onShowTaskImages" />
            </template>

            <p class="col-span-full p-5 hover:text-dark-primary text-center" role="button"
                @click="handleLoadMoreButtonClick">
                {{ filteredTasks?.length }} Görev gösteriliyor. Daha fazla yüklemek için tıklayınız
            </p>
        </div>
        <AddTaskDialog />
    </div>
</template>
<script setup lang="ts">
import { useTasksStore } from '@/stores/tasks.store';
import { storeToRefs } from 'pinia';
import TaskItem from '@/widgets/TaskItem.vue';
import AddTaskDialog from "@/dialogs/add_task_dialog/AddTaskDialog.vue";
import { useAddTaskDialog } from "@/dialogs/add_task_dialog/useAddTaskDialog";

import { Task } from '@/models/task.model';
import { PlusIcon } from '@heroicons/vue/24/solid';


const tasksStore = useTasksStore();
const addTaskDialogStore = useAddTaskDialog();

const { loading, filteredTasks, filterText } = storeToRefs(tasksStore);

const handleNewTaskButtonClick = (_: Event) => {
    addTaskDialogStore.showAddTaskDialog();
}
const handleLoadMoreButtonClick = (_: Event) => {
    tasksStore.loadMore();
}
const onShowTaskImages = (task: Task) => {
    tasksStore.showTaskImages(task.id);
}
</script>