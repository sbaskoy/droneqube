import { useShowImageDialog } from "@/dialogs/show_images_dialog/useShowImageDialog";
import { useFilter } from "@/hooks/utils/useFilter";
import { Task } from "@/models/task.model";
import TaskService from "@/services/task_service";
import { defineStore } from "pinia";
import { ref } from "vue";
import { useLoadingStore } from "./loading.store";
import { useInfoToast } from "@/hooks/toast";



export const useTasksStore = defineStore("tasks_store", () => {
    const tasks = ref<Task[]>()
    const loading = ref(false)
    const pageIndex = ref(1);
    const imageDialogStore = useShowImageDialog();
    const loadingStore = useLoadingStore();

    const { filterText, filteredItems: filteredTasks } = useFilter({
        arr: tasks,
        fn: (task, searchTerm) => task.name.toLowerCase().includes(searchTerm) || task.description.toLowerCase().includes(searchTerm)
    })

    const loadTasks = async () => {
        loading.value = true;
        const response = await TaskService.getTasks(pageIndex.value);
        loading.value = false;
        if (response) {
            return response;
        }
    }
    const loadMore = async () => {
        if (loading.value) return;
        pageIndex.value = pageIndex.value + 1;
        var res = await loadTasks();
        if (res) {
            tasks.value?.push(...res);
        }
    }
    const addTask = (task: Task) => {
        if (!tasks.value?.some(i => i.id == task.id)) {
            tasks.value?.push(task);
        }
    }
    const showTaskImages = async (taskId: number) => {
        loadingStore.show();
        var res = await TaskService.listImages(taskId);

        if (res) {
            if (res.length == 0) {
                useInfoToast("Bu göreve ait resim bulunamadı")
            } else {
                imageDialogStore.showImagesDialog(res);
            }
        }
        loadingStore.hide();
    }
    (async () => {
        const res = await loadTasks();
        if (res) {
            tasks.value = res;
        }
    })();
    return { loading, filterText, filteredTasks, loadMore, addTask, showTaskImages }
})