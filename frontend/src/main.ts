import { createApp } from 'vue'

import App from './App.vue'
import { storeBuilder } from '@/builders/store.builder';
import { routeBuilder } from '@/builders/route.builder';


import "@/assets/tailwind.css"
import 'vue3-toastify/dist/index.css';

const app = createApp(App);

storeBuilder(app);
routeBuilder(app);
app.mount('#app')
