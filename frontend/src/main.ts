import { createApp } from 'vue'

import App from './App.vue'
import { storeBuilder } from '@/builders/store.builder';
import { routeBuilder } from '@/builders/route.builder';
import { tippyBuilder } from '@/builders/tippy.builder';


import "@/assets/tailwind.css"
import 'vue3-toastify/dist/index.css';

const app = createApp(App);

storeBuilder(app);
routeBuilder(app);
tippyBuilder(app);

app.mount('#app')

if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/cache_worker.js', { scope: "/" }).then(registration => {
            console.log('ServiceWorker registration successful with scope: ', registration.scope);
        }, error => {
            console.log('ServiceWorker registration failed: ', error);
        });
    });
}
