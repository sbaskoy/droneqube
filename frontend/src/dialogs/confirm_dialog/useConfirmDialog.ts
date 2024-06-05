import { defineStore } from "pinia";
import { computed, ref } from "vue";

type ShowConfirmData = {
    title: string,
    confirmCallback?: () => void
}

export const useConfirmDialog = defineStore("confirm_dialog", () => {
    const show = ref(false);
    const data = ref<ShowConfirmData>({ title: "", });
    const onConfirm = () => {
        data.value.confirmCallback?.();
        hideConfirmDialog();
    }
    const showConfirmDialog = ($data: ShowConfirmData) => {
        data.value = $data;
        show.value = true;
    }
    const hideConfirmDialog = () => {
        show.value = false;
    }
    const title = computed(() => data.value.title);
    return { show, title, onConfirm, showConfirmDialog, hideConfirmDialog }
})