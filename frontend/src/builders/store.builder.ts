import piniaPluginPersistedState from "pinia-plugin-persistedstate";
import { createPinia } from 'pinia'
import { App } from "vue";

const pinia = createPinia();
pinia.use(piniaPluginPersistedState)

export const storeBuilder = (app: App<Element>) => {
    app.use(pinia)
}