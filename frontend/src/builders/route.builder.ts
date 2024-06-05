import { App } from "@vue/runtime-dom";

import router from "@/routes";

export const routeBuilder = (app: App<Element>) => {
    app.use(router);
} 