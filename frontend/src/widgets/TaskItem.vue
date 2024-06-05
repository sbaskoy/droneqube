<template>
    <div
        class=" p-4 h-40 max-w-96 flex flex-col items-start justify-center gap-2 rounded-md flex-1 overflow-hidden truncate hover:bg-dark-card-hover shadow-sm"
        :class="[isVisible ? 'bg-dark-card-hover' : 'bg-dark-card' ]"
        >
        <p class="font-semibold truncate">{{ task.name }}</p>
        <p class="font-thin truncate">{{ task.description }}</p>
        <div class="flex items-center justify-between w-full group" role="button" ref="targetElement"
            @click="handleShowDronesClick">
            <p class="font-thin rounded-md text-dark-primary bg-dark-card-active px-2 w-auto ">{{
                `${assignments.length} Drones` }}</p>
            <ChevronDownIcon class="size-4 hidden group-hover:block" v-if="assignments.length > 0" />
            <Teleport to="body">
                <div ref="popupElement" class="p-3 rounded-md absolute z-30 bg-dark-card flex flex-col gap-2">
                    <div v-for="assignment in assignments" :key="assignment.id">
                        <p >{{ assignment.drone?.name }} </p>

                    </div>
                </div>
            </Teleport>
        </div>
        <div class="flex items-center justify-between w-full">
            <button class="text-button flex items-center gap-2" @click="handleImageButtonClick">
                <PhotoIcon class="size-5" />
                Resimler
            </button>
            <button class="text-button flex items-center gap-2">
                <PlusIcon class="size-5" />
                Drone Ata
            </button>
        </div>
    </div>
</template>
<script setup lang="ts">
import { usePopup } from '@/hooks/utils/usePopup';
import { Task } from '@/models/task.model';
import { PlusIcon, PhotoIcon, ChevronDownIcon } from '@heroicons/vue/24/solid';
import { computed } from 'vue';

interface Props {
    task: Task
}

const props = defineProps<Props>()

interface Emits {
    (e: 'onShowImages', val: Task): void
}
const emit = defineEmits<Emits>();

const assignments = computed(() => props.task.drone_assignments ?? []);

const handleImageButtonClick = (_: Event) => {
    emit('onShowImages', props.task)
}

const { toggle, popupElement, targetElement,isVisible } = usePopup({ isWidthFull: true })

const handleShowDronesClick = (_: Event) => {
    if (assignments.value.length > 0) {
        toggle();
    }
}

</script>