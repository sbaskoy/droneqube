<template>
    <div v-bind="$attrs"
        class="bg-dark-card rounded-full size-10 p-2 text-sm transition-all ease-in duration-100 hover:bg-dark-card-hover flex items-center justify-center"
        role="button">
        <slot />
    </div>
</template>