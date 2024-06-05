<template>
    <div v-if="isImageError" class="flex size-full items-center justify-center">
        <ExclamationTriangleIcon class="size-8" />
    </div>
  <img v-bind="$attrs" :src="imageUrl" v-else @error="handleImageLoadError" />
</template>
<script setup lang="ts">
import { ref, watchEffect, computed } from "vue";
import { ExclamationTriangleIcon } from '@heroicons/vue/24/solid';

interface Props {
    url: string | undefined
}

const props = defineProps<Props>()

const isImageError=ref(false);
const imageUrl = ref<string>('');

const $url = computed(() => props.url);

const handleImageLoadError=()=> {
    isImageError.value=true;
}

const fetchImageUrl = async (url: string) => {
    if (!window.caches || !navigator.serviceWorker) {
        return url;
    }
    const cache = await window.caches.open('image-cache-v1');
    const cachedResponse = await cache.match(url);
    if (cachedResponse) {
        return cachedResponse.url;
    } else {
        cache.add(url);
        return url;
    }
};

watchEffect(async () => {
    if ($url.value) {
        imageUrl.value = await fetchImageUrl($url.value);
    }
    isImageError.value=false;
});

</script>