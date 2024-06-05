<template>
    <Teleport to="body">
        <transition name="dialog-fade">
            <div class="h-[100vh] w-[100vw] absolute top-0 left-0 flex items-center justify-center  gap-2 bg-dark-bg bg-opacity-30"
                v-show="show">
                <div class="w-96 h-40 flex flex-col gap-5 bg-dark-card rounded-lg p-5" ref="confirmElement">
                    <h5> {{ title }} </h5>
                    <div class="flex items-center justify-end gap-5">
                        <button
                            class="w-28 py-1 hover:text-red-400 border rounded-md border-dark-text-disable border-opacity-40 font-semibold"
                            @click="confirmStore.hideConfirmDialog">Cancel</button>
                        <button @click="confirmStore.onConfirm"
                            class="w-28 py-1 hover:text-green-400 border rounded-md border-dark-text-disable border-opacity-40 font-semibold">Yes</button>
                    </div>
                </div>
            </div>
        </transition>
    </Teleport>
</template>
<script setup lang="ts">
import { storeToRefs } from "pinia";
import { useConfirmDialog } from "./useConfirmDialog";
import { ref, onMounted, onUnmounted } from "vue";
const confirmStore = useConfirmDialog();

const { show, title } = storeToRefs(confirmStore);

const confirmElement = ref<HTMLElement>();

const handleClickOutside = (_: MouseEvent) => {
    // const el = confirmElement.value;
    // if (el && (el != event.target && !el.contains(event.target as Node))) {
    //     confirmStore.hideConfirmDialog();
    // }
};
onMounted(() => {
    document.addEventListener('click', handleClickOutside);
})
onUnmounted(() => {
    document.removeEventListener("click", handleClickOutside);
})

</script>