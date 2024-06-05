
<template>
    <Teleport to="body">
        <transition name="dialog-fade">
            <div class="h-[100vh] w-[100vw] absolute top-0 left-0 flex flex-col gap-2 bg-dark-bg bg-opacity-90 z-50 "
                v-if="show" @dblclick.stop>
                <div class="flex gap-3 p-4 h-20 justify-end bg-dark-bg">
                   <div class="flex flex-col flex-1">
                     <h5 v-if="title" class="flex-1">{{ title }}</h5>
                     <p class="text-sm">{{  selectedItem.name }}</p>
                   </div>
                    <IconButton @click="hideDialog" class="absolute top-5 right-2">
                        <XMarkIcon />
                    </IconButton>
                </div>

                <div class="flex-1 flex gap-3 overflow-hidden">

                    <div class="px-3 w-12 flex flex-col items-center justify-center">
                        <IconButton @click="previous" :class="[selectedIndex == 0 ? 'hidden' : '']">
                            <ArrowLeftIcon />
                        </IconButton>
                    </div>
                    <div class="flex-1 w-full flex items-center justify-center">
                        <transition name="image-fade" mode="out-in">
                            <CachedImage class="max-w-full max-h-full object-contain" :url="selectedItem.url" />
                        </transition>
                    </div>
                    <div class="px-3 w-12 flex flex-col items-center justify-center">
                        <IconButton @click="next" :class="[selectedIndex == images.length - 1 ? 'hidden' : '']">
                            <ArrowRightIcon />
                        </IconButton>
                    </div>
                </div>
                <div class="flex gap-3 items-center  overflow-auto scrollbar-thin scrollbar-track-dark-bg scrollbar-thumb-dark-card py-2 whitespace-nowrap"
                    ref="container">
                    <div v-for="(item, index) in  images " :key="index" ref="imageRefs" class="size-32"
                        style="flex: 0 0 auto;">
                        <CachedImage :url="item.url" class="object-fill rounded-md size-full"
                            :class="{ 'scale-110': index == selectedIndex }" role="button" @click="() => setIndex(index)" />
                    </div>
                </div>
            </div>
        </transition>
    </Teleport>
</template>
<script setup lang="ts">

import { computed, ref, watch } from "vue";
import { storeToRefs } from "pinia";
import { useShowImageDialog } from "./useShowImageDialog";

import { ArrowRightIcon, ArrowLeftIcon, XMarkIcon } from '@heroicons/vue/24/solid';
import IconButton from "@/widgets/IconButton.vue"
import CachedImage from "@/widgets/CachedImage.vue"




const dialogStore = useShowImageDialog();

const { images, title, selectedIndex, show } = storeToRefs(dialogStore);

const { next, previous, hideDialog, setIndex } = dialogStore;

const selectedItem = computed(() => images.value[selectedIndex.value])

const container = ref<HTMLElement | null>(null);
const imageRefs = ref<HTMLElement[]>([]);

watch(() => selectedIndex.value, (newIndex) => {
    const imageElement = imageRefs.value[newIndex];
    const containerElement = container.value;
    if (containerElement && imageElement) {

        const containerRect = containerElement.getBoundingClientRect();
        const imageRect = imageElement.getBoundingClientRect();
        const offset = imageRect.left - containerRect.left - containerRect.width / 2 + imageRect.width / 2;

        containerElement.scrollBy({
            left: offset,
            behavior: 'smooth'
        });
    }

});

</script>

