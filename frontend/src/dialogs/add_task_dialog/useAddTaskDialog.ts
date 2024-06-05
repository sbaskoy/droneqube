import { useInfoToast } from "@/hooks/toast";
import TaskService from "@/services/task_service";
import { useLoadingStore } from "@/stores/loading.store";
import { useTasksStore } from "@/stores/tasks.store";
import { defineStore } from "pinia";
import { ref } from "vue";

export const useAddTaskDialog = defineStore("add_task_dialog", () => {
    const show = ref(false);
    const taskName = ref("");
    const taskDescription = ref("");
    const loadingStore = useLoadingStore();
    const tasksStore = useTasksStore();
    const showAddTaskDialog = () => {
        show.value = true;
    }
    const hideAddTaskDialog = () => {
        show.value = false;
    }
    const addNewTask = async () => {
        loadingStore.show();
        var res = await TaskService.createTask({
            name: taskName.value,
            description: taskDescription.value
        });
        console.log(res);
        if (res) {
            tasksStore.addTask(res);
            taskName.value = "";
            taskDescription.value = "";
            useInfoToast("Görev başarıyla eklendi.")
        }
        loadingStore.hide();
    }
    return { show, taskName,taskDescription, showAddTaskDialog, hideAddTaskDialog, addNewTask }
})