

import { useAuthStore } from '@/stores/auth.store'
import { createRouter, createWebHistory } from 'vue-router'



const routes = [
    {
        path: '/',
        name: "AppLyaout",
        components: {
            app: () => import("../layouts/AppLayout.vue")
        },
        children: [
            {
                path: "",
                name: "HomeLayout",
                components: {
                    app: () => import("../layouts/HomeLayout.vue")
                },
                children: [
                    {
                        path: "",
                        name: "Home",
                        components: {
                            home: () => import("../views/HomeView.vue")
                        },
                    },
                    {
                        path: "tasks",
                        name: "Tasks",
                        components: {
                            home: () => import("../views/TasksView.vue")
                        },
                    },
                    {
                        path: "drones",
                        name: "Drones",
                        components: {
                            home: () => import("../views/DronesView.vue")
                        },
                    }
                ]
            },
            {
                path: "login",
                name: "Login",
                components: {
                    app: () => import("../views/LoginView.vue")
                },
            }
        ]
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, _, next) => {
    const { user } = useAuthStore();
    if (to.name != "Login" && !user?.access_token) {
        return next({ name: "Login" })
    }
    next();
})


export default router;